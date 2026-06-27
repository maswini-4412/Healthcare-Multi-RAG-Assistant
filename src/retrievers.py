from pathlib import Path
from langchain_community.vectorstores import FAISS

from src.embeddings import get_embeddings

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

FAISS_DIR = BASE_DIR / "faiss_indexes"


def load_retrievers():

    embeddings = get_embeddings()

    medical_db = FAISS.load_local(
        str(FAISS_DIR / "medical_index"),
        embeddings,
        allow_dangerous_deserialization=True
    )

    drug_db = FAISS.load_local(
        str(FAISS_DIR / "drug_index"),
        embeddings,
        allow_dangerous_deserialization=True
    )

    symptom_db = FAISS.load_local(
        str(FAISS_DIR / "symptom_index"),
        embeddings,
        allow_dangerous_deserialization=True
    )

    who_db = FAISS.load_local(
        str(FAISS_DIR / "who_index"),
        embeddings,
        allow_dangerous_deserialization=True
    )

    return {
        "medical": medical_db.as_retriever(search_kwargs={"k": 3}),
        "drug": drug_db.as_retriever(search_kwargs={"k": 3}),
        "symptom": symptom_db.as_retriever(search_kwargs={"k": 3}),
        "who": who_db.as_retriever(search_kwargs={"k": 3}),
    } 