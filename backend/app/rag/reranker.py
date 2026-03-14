from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(query, results, top_k=5):

    pairs = [(query, r["text"]) for r in results]

    scores = model.predict(pairs)

    ranked = list(zip(scores, results))

    ranked.sort(key=lambda x: x[0], reverse=True)

    return [r for _, r in ranked[:top_k]]