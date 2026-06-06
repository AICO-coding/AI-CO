import modal
import subprocess
import sys
import tempfile
import os

app = modal.App("aico-code-runner")

image = modal.Image.debian_slim().pip_install(
    "torch", "torchvision", "transformers",
    "scikit-learn", "numpy", "Pillow"
)


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
