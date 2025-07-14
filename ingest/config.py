import os
from dotenv import load_dotenv

load_dotenv()

BITCOIN_RPC = os.getenv("BITCOIN_RPC")
PG_URI = os.getenv("PG_URI")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")
