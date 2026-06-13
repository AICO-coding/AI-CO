from pathlib import Path
from bs4 import BeautifulSoup
import chromadb
from chromadb.utils import embedding_functions
from app.core.config import OPENAI_API_KEY, OPENAI_EMBEDDING_MODEL

MD_DIR = Path(__file__).resolve().parents[4] / "frontend" / "public" / "static" / "md"
CHROMA_DIR = Path(__file__).resolve().parents[3] / "chroma_db"

_collection = None


def _embedding_function():
    return embedding_functions.OpenAIEmbeddingFunction(
        api_key=OPENAI_API_KEY,
        model_name=OPENAI_EMBEDDING_MODEL,
    )


def _strip_html(text: str) -> str:
    return BeautifulSoup(text, "html.parser").get_text(separator="\n", strip=True)


def build_index(force: bool = False) -> chromadb.Collection:
    global _collection

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    ef = _embedding_function()

    if force:
        try:
            client.delete_collection("lessons")
        except Exception:
            pass

    collection = client.get_or_create_collection(
        name="lessons",
        embedding_function=ef,
        metadata={"hnsw:space": "cosine"},
    )

    if collection.count() > 0 and not force:
        _collection = collection
        return collection

    documents, metadatas, ids = [], [], []

    for md_file in sorted(MD_DIR.rglob("*.md")):
        parts = md_file.relative_to(MD_DIR).parts
        if len(parts) < 3:
            continue

        track, chapter, lesson = parts[0], parts[1], md_file.stem
        clean_text = _strip_html(md_file.read_text(encoding="utf-8"))

        if not clean_text.strip():
            continue

        documents.append(clean_text)
        metadatas.append({"track": track, "chapter": chapter, "lesson": lesson})
        ids.append(f"{track}/{chapter}/{lesson}")

    if documents:
        collection.add(documents=documents, metadatas=metadatas, ids=ids)
        print(f"[Indexer] {len(documents)}개 레슨 인덱싱 완료")

    _collection = collection
    return collection


def get_collection() -> chromadb.Collection:
    global _collection
    if _collection is None:
        _collection = build_index()
    return _collection
