def transaction_summary_prompt(tx):
    return f"""Transaction Summary:
- TxID: {tx['txid']}
- Inputs: {tx['input_count']}, Outputs: {tx['output_count']}
- Total Output: {tx['output_total_sat']} sats
- Script Types: {tx['script_types']}
"""
