import requests
from pathlib import Path
from bs4 import BeautifulSoup

from app.rag.ingest import build_index
from app.rag.bm25_index import build_bm25


DATA_PATH = Path("app/data/sources/boe")

BOE_CONSTITUCION_URL = "https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229"


def download_constitution():

    DATA_PATH.mkdir(parents=True, exist_ok=True)

    response = requests.get(BOE_CONSTITUCION_URL)

    file_path = DATA_PATH / "constitucion.html"

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response.text)

    print("Constitución descargada")

    return file_path


def clean_html(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text()

    cleaned_path = file_path.with_suffix(".txt")

    with open(cleaned_path, "w", encoding="utf-8") as f:
        f.write(text)

    print("Texto limpio generado")

    return cleaned_path


def run_pipeline():

    html_file = download_constitution()

    clean_html(html_file)

    build_index()
    
    build_bm25()

    print("Pipeline completado")