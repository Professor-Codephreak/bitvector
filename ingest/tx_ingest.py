import json, requests, psycopg2
from config import BITCOIN_RPC, PG_URI
from embedding_agent import embed_tx

def rpc_call(method, params=[]):
    r = requests.post(BITCOIN_RPC, json={"method": method, "params": params})
    return r.json()["result"]

def ingest_block(height: int):
    conn = psycopg2.connect(PG_URI)
    cur = conn.cursor()

    block_hash = rpc_call("getblockhash", [height])
    block = rpc_call("getblock", [block_hash, 2])

    for tx in block["tx"]:
        txid = tx["txid"]
        input_addresses = [vin.get("txid", "coinbase") for vin in tx.get("vin", [])]
        output_addresses = []
        output_total = 0
        script_types = []

        for vout in tx.get("vout", []):
            val = vout.get("value", 0)
            output_total += val
            addresses = vout.get("scriptPubKey", {}).get("addresses", ["unknown"])
            output_addresses.extend(addresses)
            script_types.append(vout.get("scriptPubKey", {}).get("type", "unknown"))

        prompt = f"""TXID: {txid}
Inputs: {len(input_addresses)}, Outputs: {len(output_addresses)}
Total Out: {output_total:.8f} BTC
Script Types: {script_types}"""

        embedding = embed_tx(prompt)

        cur.execute("""
            INSERT INTO transactions (
                txid, block_height, block_time, fee_sat,
                input_total_sat, output_total_sat, input_count,
                output_count, input_addresses, output_addresses,
                script_types, embedding
            ) VALUES (%s,%s,TO_TIMESTAMP(%s),%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT DO NOTHING
        """, (
            txid, height, block["time"], 0, 0, int(output_total * 1e8),
            len(input_addresses), len(output_addresses),
            input_addresses, output_addresses, script_types, embedding
        ))

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    for h in range(841000, 841010):
        ingest_block(h)
