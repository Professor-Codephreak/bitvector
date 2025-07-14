from fastapi import FastAPI
from pydantic import BaseModel
from llm.vector_search import search_transactions

app = FastAPI()

class Query(BaseModel):
    vector: list[float]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/search")
def vector_search(q: Query):
    results = search_transactions(q.vector)
    return {"results": results}
