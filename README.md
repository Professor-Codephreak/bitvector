# 🧠 BitVector
**Semantic Blockchain Intelligence with Vector Search + Temporal Inference**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Build](https://img.shields.io/badge/build-stable-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Timescale-blue)
![Embedding](https://img.shields.io/badge/LLM-OpenAI-ff69b4)

```txt
bitvector/
├── .env.example
├── README.md
├── requirements.txt
├── docker-compose.yml
├── init/
│   └── init_timescale.sql
├── ingest/
│   ├── tx_ingest.py
│   ├── embedding_agent.py
│   └── config.py
├── llm/
│   ├── prompt_templates.py
│   └── vector_search.py
├── api/
│   └── server.py
└── dashboards/
    └── grafana_setup.json
```



---

BitVector is an advanced blockchain AI analytics system that transforms Bitcoin transaction data into high-dimensional vector embeddings, enabling:

- 🔍 **Semantic transaction search**
- 📊 **Time-series block & fee analysis**
- 🤖 **LLM-powered behavioral inference**
- ⚡ **FastAPI + Grafana-powered querying and dashboards**

Built on PostgreSQL + TimescaleDB + pgvector with OpenAI embeddings.

---

## 📐 Architecture

+--------------+ +---------------------+ +---------------------+
| Bitcoin Core| ==> | ETL + Vectorizer | ==> | PostgreSQL + Vector |
| (bitcoind) | | (tx_ingest.py) | | (Timescale + pgvec)|
+--------------+ +---------------------+ +---------------------+
||
||
+---------+
| FastAPI |
| /search |
+---------+
||
+----------+
| Grafana |
| Dashboards |
+----------+

yaml
Copy
Edit

---

## 🛠️ Features

| Feature                          | Description                                              |
|----------------------------------|----------------------------------------------------------|
| 🔍 Vector Search                 | Nearest-neighbor semantic tx matching with pgvector      |
| 📈 Time Series Analysis          | Transaction + fee flows over time with TimescaleDB       |
| 🤖 Embedding Agent               | Generates LLM embeddings for transaction behavior        |
| 📊 Grafana Dashboards            | Live visualization of blockchain behavior & stats        |
| 🧪 FastAPI Interface             | Query embeddings via REST (`/search`)                    |

---

## ⚙️ Setup Instructions

### 1. 📦 Clone and Configure

```bash
git clone https://github.com/your-org/bitvector.git
cd bitvector
cp .env.example .env
Edit .env to include:

Bitcoin Core RPC credentials

PostgreSQL URI

OpenAI API key

2. 🐳 Run with Docker
bash
Copy
Edit
docker-compose up --build
This launches:

🐘 PostgreSQL with Timescale + pgvector

🌐 FastAPI for embedding search

📊 Grafana dashboard UI

3. 🧬 Ingest Blockchain Data
bash
Copy
Edit
cd ingest
python tx_ingest.py
This will:

Connect to your local Bitcoin Core node

Ingest recent blocks

Vectorize transactions

Store them in transactions table

📡 API Overview
GET /health
Returns status of the inference engine.

POST /search
Submit a 384-dim vector and receive nearest transaction matches.

Example Input
json
Copy
Edit
{
  "vector": [0.038, 0.284, ..., 0.092]
}
📊 Dashboards
Transactions per 10min

Average Fee Trend

High-Value TX Count

Vector Embedding Drift

Stat Panels: Block height, vectorized tx count, hourly volume

To import:

Open Grafana

Go to Dashboards > Import

Use dashboards/bitvector_dashboard.json

🧠 Extend the Mind
Add ZMQ live mempool ingestion

Build a custom LLM fine-tuned on chain heuristics

Enable risk scoring + anomaly detection

Integrate embedding drift monitoring for market phase tracking

📜 License
MIT License © 2025 BitVector Contributors
