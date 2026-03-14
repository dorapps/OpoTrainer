import faiss
import numpy as np
import pickle
from pathlib import Path
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi
from app.rag.reranker import rerank

BASE_DIR = Path(__file__).resolve().parent.parent

VECTOR_PATH = BASE_DIR / "data" / "vector"

INDEX_PATH = VECTOR_PATH / "index.faiss"
DOCS_PATH = VECTOR_PATH / "docs.pkl"
META_PATH = VECTOR_PATH / "meta.pkl"
BM25_PATH = VECTOR_PATH / "bm25.pkl"


# modelo embeddings (debe ser el mismo usado en ingest)
model = SentenceTransformer("BAAI/bge-m3")


# -----------------------------
# cargar índices
# -----------------------------
def load_index():

    index = faiss.read_index(str(INDEX_PATH))

    with open(DOCS_PATH, "rb") as f:
        docs = pickle.load(f)

    with open(META_PATH, "rb") as f:
        meta = pickle.load(f)

    with open(BM25_PATH, "rb") as f:
        bm25 = pickle.load(f)

    return index, docs, meta, bm25


# -----------------------------
# búsqueda híbrida
# -----------------------------
def retrieve(query: str, top_k: int = 30):

    index, docs, meta, bm25 = load_index()

    # ----- embedding search -----

    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    embedding_hits = list(indices[0])

    # ----- BM25 search -----

    tokenized_query = query.lower().split()

    bm25_scores = bm25.get_scores(tokenized_query)

    bm25_indices = np.argsort(bm25_scores)[::-1][:top_k]

    # ----- combinar resultados -----

    combined_indices = list(set(embedding_hits + list(bm25_indices)))

    results = []

    for i in combined_indices:

        results.append({
            "text": docs[i],
            "metadata": meta[i]
        })

    return results


# -----------------------------
# construir contexto para LLM
# -----------------------------
def build_context(query: str, top_k: int = 5):

    results = retrieve(query, top_k=30)

    # reranking con cross-encoder
    results = rerank(query, results, top_k=top_k)

    context_parts = []

    seen_articles = set()

    for r in results:

        text = r["text"]
        meta = r["metadata"]

        source = meta.get("source", "desconocido")
        article = meta.get("article")

        # evitar repetir el mismo artículo
        if article in seen_articles:
            continue

        seen_articles.add(article)

        header = f"[Fuente: {source} | Artículo {article}]"

        context_parts.append(f"{header}\n{text}")

    return "\n\n".join(context_parts)