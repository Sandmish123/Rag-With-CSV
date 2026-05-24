# Rag-With-CSV

A Retrieval-Augmented Generation (RAG) system for querying CSV data using semantic search and LLMs.

---

## Features

* CSV ingestion
* Embedding generation
* Vector database storage
* Semantic retrieval
* LLM-powered Q&A
* FastAPI backend
* Production-ready structure

---

## Architecture

```txt id="4bd6v7"
CSV → Chunking → Embeddings → Vector DB → Retrieval → LLM → Answer
```

---

## Project Structure

```txt id="33x1nr"
rag-with-csv/
│
├── apps/
├── configs/
├── data/
├── src/
├── tests/
├── .env
├── pyproject.toml
└── README.md
```

---

## Installation

```bash id="04t8p2"
git clone https://github.com/your-username/rag-with-csv.git

cd rag-with-csv

pip install -r requirements.txt
```

---

## Environment Variables

Create `.env`

```env id="2b9flj"
OPENAI_API_KEY=your_key
QDRANT_URL=http://localhost:6333
```

---

---

## Add CSV

Place CSV files inside:

```txt id="68w6cl"
data/raw/
```

---

## Ingest Data

```bash id="xw9mrf"
python scripts/ingest_csv.py
```

---

## Start API

```bash id="v8m3we"
uvicorn apps.api.main:app --reload
```

---

## Example Query

```json id="lmj9y4"
{
  "query": "Which customer generated highest revenue?"
}
```


---


