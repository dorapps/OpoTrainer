import re

def clean_boe_text(text: str):

    text = re.sub(r"\[Bloque.*?\]", "", text)
    text = re.sub(r"Subir", "", text)
    text = re.sub(r"Jurisprudencia", "", text)

    text = re.sub(r"\n\s*\n", "\n\n", text)
  
    # eliminar cabecera del BOE
    if "Artículo 1" in text:
        text = text.split("Artículo 1", 1)[1]
        text = "Artículo 1 " + text

    return text.strip()