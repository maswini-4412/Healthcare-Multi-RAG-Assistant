from fastapi import FastAPI
from pydantic import BaseModel

from src.rag_chain import ask_question

app = FastAPI(
    title="Healthcare Multi-RAG API"
)

# Request Body
class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Healthcare Multi-RAG API is Running"
    }


@app.post("/ask")
def ask(request: QuestionRequest):

    result = ask_question(request.question)

    return {
        "rag_used": result["rag_used"],
        "answer": result["answer"]
    } 