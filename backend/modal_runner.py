import modal
import subprocess
import sys
import tempfile
import os

app = modal.App("aico-code-runner")


def _prepare_klue_ynat_data():
    import os
    import pandas as pd
    from datasets import load_dataset

    ds = load_dataset("klue", "ynat", trust_remote_code=True)
    os.makedirs("/root/data/klue_ynat", exist_ok=True)
    for split, filename in [("train", "train.tsv"), ("validation", "test.tsv")]:
        df = ds[split].to_pandas()[["title", "label"]]
        df.to_csv(f"/root/data/klue_ynat/{filename}", sep="\t", index=False)


image = modal.Image.debian_slim().pip_install(
    "torch", "torchvision", "transformers",
    "scikit-learn", "numpy", "Pillow", "pandas", "sentencepiece", "datasets<4.0"
).run_function(_prepare_klue_ynat_data)


@app.function(image=image, gpu="T4", timeout=120)
def run_code_gpu_stream(code: str):
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write(code)
            tmp_path = f.name

        process = subprocess.Popen(
            [sys.executable, "-u", tmp_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        for line in iter(process.stdout.readline, ""):
            yield {"type": "stdout", "line": line.rstrip("\n")}
        process.wait()
        stderr = process.stderr.read()
        if stderr:
            for line in stderr.split("\n"):
                if line:
                    yield {"type": "stderr", "line": line}
        yield {"type": "done", "returncode": process.returncode}
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)


@app.function(image=image, gpu="T4", timeout=120)
def run_code_gpu(code: str) -> dict:
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
            f.write(code)
            tmp_path = f.name

        result = subprocess.run(
            [sys.executable, tmp_path],
            capture_output=True,
            text=True,
            timeout=110,
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)