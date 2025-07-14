CREATE EXTENSION IF NOT EXISTS timescaledb;
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE blocks (
    block_hash TEXT PRIMARY KEY,
    block_height INT UNIQUE,
    timestamp TIMESTAMPTZ,
    num_tx INT,
    size_bytes INT,
    miner_address TEXT,
    embedding VECTOR(384)
);
SELECT create_hypertable('blocks', 'timestamp');

CREATE TABLE transactions (
    txid TEXT PRIMARY KEY,
    block_height INT REFERENCES blocks(block_height),
    block_time TIMESTAMPTZ,
    fee_sat BIGINT,
    input_total_sat BIGINT,
    output_total_sat BIGINT,
    input_count INT,
    output_count INT,
    input_addresses TEXT[],
    output_addresses TEXT[],
    script_types TEXT[],
    is_coinbase BOOLEAN DEFAULT FALSE,
    embedding VECTOR(384)
);
SELECT create_hypertable('transactions', 'block_time');
CREATE INDEX ON transactions USING ivfflat (embedding vector_cosine_ops);
