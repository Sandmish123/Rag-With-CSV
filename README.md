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
    INPUT_FILE= sample_data.xlsx
    OUTPUT_FILE=output.json
```

---

---


