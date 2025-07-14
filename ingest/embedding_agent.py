import openai
from config import OPENAI_KEY, EMBEDDING_MODEL

openai.api_key = OPENAI_KEY

def embed_tx(text: str) -> list[float]:
    try:
        response = openai.Embedding.create(
            input=[text],
            model=EMBEDDING_MODEL
        )
        return response["data"][0]["embedding"]
    except Exception as e:
        print(f"[Embedding Error] {e}")
        return [0.0] * 384
