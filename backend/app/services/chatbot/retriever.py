import re
from app.services.chatbot.indexer import get_collection


def _chapter_range(chapter: str) -> list[str]:
    match = re.search(r'\d+', chapter)
    if not match:
        return [chapter]
    prefix = chapter[:match.start()]  # "ch"
    n = int(match.group())
    return [f"{prefix}{i}" for i in range(1, n + 1)]


def search(query: str, track: str, chapter: str, n_results: int = 4) -> list[str]:
    collection = get_collection()

    if collection.count() == 0:
        return []

    chapters = _chapter_range(chapter)  

    try:
        results = collection.query(
            query_texts=[query],
            n_results=n_results,
            where={"$and": [{"track": track}, {"chapter": {"$in": chapters}}]},
        )
        return results.get("documents", [[]])[0]
    except Exception:
        pass

    try:
        total = collection.count()
        results = collection.query(
            query_texts=[query],
            n_results=min(n_results, total),
        )
        return results.get("documents", [[]])[0]
    except Exception:
        return []
