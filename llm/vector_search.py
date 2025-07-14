import psycopg2
from config import PG_URI

def search_transactions(vector: list[float], limit=5):
    conn = psycopg2.connect(PG_URI)
    cur = conn.cursor()
    cur.execute("""
        SELECT txid, block_height, output_total_sat, block_time
        FROM transactions
        ORDER BY embedding <-> %s
        LIMIT %s
    """, (vector, limit))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
