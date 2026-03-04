from fastapi import FastAPI
from app.api import exams
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
import time
from sqlalchemy.exc import OperationalError
from app.api import questions

app = FastAPI(
    title="OpoTrainer API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego lo restringimos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    # Esperar a que la DB esté lista
    retries = 5
    while retries:
        try:
            Base.metadata.create_all(bind=engine)
            print("Database connected ✅")
            break
        except OperationalError:
            retries -= 1
            print("Database not ready, retrying...")
            time.sleep(2)

app.include_router(exams.router)
app.include_router(questions.router)

@app.get("/")
def root():
    return {"message": "OpoTrainer backend running 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}