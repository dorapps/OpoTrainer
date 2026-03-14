from rank_bm25 import BM25Okapi
import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

VECTOR_PATH = BASE_DIR / "data" / "vector"

DOCS_PATH = VECTOR_PATH / "docs.pkl"
BM25_PATH = VECTOR_PATH / "bm25.pkl"


def build_bm25():

    with open(DOCS_PATH, "rb") as f:
        docs = pickle.load(f)

    tokenized = [doc.lower().split() for doc in docs]

    bm25 = BM25Okapi(tokenized)

    with open(BM25_PATH, "wb") as f:
        pickle.dump(bm25, f)

    print("BM25 index creado")