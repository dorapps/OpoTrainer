import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path
import pickle

from app.rag.article_parser import split_by_articles
from app.rag.clean_boe import clean_boe_text

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "sources" / "boe"
VECTOR_PATH = BASE_DIR / "data" / "vector"

INDEX_PATH = VECTOR_PATH / "index.faiss"
DOCS_PATH = VECTOR_PATH / "docs.pkl"
META_PATH = VECTOR_PATH / "meta.pkl"

model = SentenceTransformer("BAAI/bge-m3")


def build_index():

    documents = []
    metadatas = []

    for file in DATA_PATH.glob("*.txt"):

        print("Procesando:", file)

        text = clean_boe_text(file.read_text(encoding="utf-8"))

        chunks = split_by_articles(text)

        print("Artículos detectados:", len(chunks))

        for chunk in chunks:

            documents.append(chunk["text"])

            metadatas.append({
                "source": file.name,
                "article": chunk["article"]
            })

    print("Total chunks:", len(documents))

    embeddings = model.encode(
    [f"passage: {doc}" for doc in documents],
    normalize_embeddings=True
)

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)

    index.add(np.array(embeddings))

    VECTOR_PATH.mkdir(parents=True, exist_ok=True)

    faiss.write_index(index, str(INDEX_PATH))

    with open(DOCS_PATH, "wb") as f:
        pickle.dump(documents, f)

    with open(META_PATH, "wb") as f:
        pickle.dump(metadatas, f)

    print("Índice vectorial creado")