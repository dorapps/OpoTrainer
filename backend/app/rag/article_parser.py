import re

def split_by_articles(text):

    pattern = r"(Artículo\s+\d+[\s\S]*?)(?=Artículo\s+\d+|$)"
    matches = re.findall(pattern, text)

    chunks = []

    for article in matches:

        article = article.strip()

        # extraer número de artículo
        m = re.search(r"Artículo\s+(\d+)", article)
        article_num = int(m.group(1)) if m else None

        # dividir por párrafos
        paragraphs = re.split(r"\n\s*\n", article)

        for p in paragraphs:

            p = p.strip()

            if len(p) < 40:
                continue

            chunks.append({
                "text": p,
                "article": article_num
            })

    return chunks
