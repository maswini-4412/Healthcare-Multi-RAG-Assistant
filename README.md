# 🏥 Healthcare Multi-RAG Assistant

A Healthcare Multi-RAG (Retrieval-Augmented Generation) Chatbot that answers medical-related queries by intelligently retrieving information from multiple knowledge sources.

The system uses separate RAG pipelines for Medical Documents, Drug Information, Symptoms Database, and WHO Guidelines. A router selects the correct knowledge source based on the user query and generates responses using Groq Llama LLM.

---

## 🚀 Project Overview

Traditional RAG systems retrieve information from a single knowledge base.

This project implements a Multi-RAG architecture where multiple independent retrievers work together:

- Medical Document RAG
- Drug Information RAG
- Symptom Database RAG
- WHO Guidelines RAG

The chatbot automatically routes user questions to the correct RAG pipeline.

---

## 🏗️ Architecture

```text
User Question
      |
      v
Query Router
      |
      |
--------------------------------
|              |               |
Medical RAG   Drug RAG   Symptom RAG
|              |               |
FAISS         FAISS          FAISS
Vector DB     Vector DB      Vector DB
--------------------------------
      |
      v
Retrieved Context
      |
      v
Groq Llama 3 LLM
      |
      v
Generated Answer
```

---

## 📂 Project Structure

```text
Healthcare_MultiRAG_Assistant/

│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── src/
│
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrievers.py
│   ├── router.py
│   ├── llm.py
│   └── rag_chain.py
│
├── data/
│
│   ├── medical_pdfs/
│   │       ├── dengue.txt
│   │       ├── malaria.txt
│   │       └── typhoid.txt
│   │
│   ├── drug_csv/
│   │       └── medicines.csv
│   │
│   ├── symptoms/
│   │       └── symptoms.json
│   │
│   └── who_guidelines/
│           └── who_guidelines.txt
│
└── faiss_indexes/

    ├── medical_index/
    ├── drug_index/
    ├── symptom_index/
    └── who_index/
```

---

# ⚙️ Tech Stack

## Programming Language
- Python 3.10

## Frameworks

- LangChain
- Streamlit

## LLM

- Groq Llama 3

## Embeddings

- HuggingFace Sentence Transformers

Model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

## Vector Database

- FAISS

## Data Sources

- Medical Documents
- Medicine CSV Dataset
- Symptoms JSON Dataset
- WHO Guidelines

---

# 🔥 Features

✔ Multiple RAG pipelines

✔ Intelligent query routing

✔ FAISS semantic search

✔ HuggingFace embeddings

✔ Structured + Unstructured data retrieval

✔ Groq Llama based answer generation

✔ Streamlit chatbot interface


---

# 🧠 Multi-RAG Workflow


## 1. Document Loading

Healthcare documents are loaded from:

```text
Medical TXT/PDF
CSV files
JSON files
WHO documents
```

---

## 2. Embedding Creation

Documents are converted into vector embeddings:

Example:

```text
"Symptoms of dengue fever"

        ↓

[0.23, 0.54, 0.76....]
```

---

## 3. FAISS Index Creation

Separate vector stores are created:

```text
medical_index

drug_index

symptom_index

who_index
```

---

## 4. Query Routing

Example:

User:

```text
What are symptoms of dengue?
```

Router selects:

```text
Symptom RAG
```

---

User:

```text
Which medicine is used for malaria?
```

Router selects:

```text
Drug RAG
```

---

## 5. LLM Response Generation


Retrieved Context + Question

↓

Groq Llama 3

↓

Healthcare Response


---

# 🛠️ Installation

Clone repository:

```bash
git clone <repository-url>

cd Healthcare_MultiRAG_Assistant
```

---

Create Python environment:

```bash
py -3.10 -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create:

```text
.env
```

Add:

```env
GROQ_API_KEY=your_api_key_here
```

---

# 🧬 Create FAISS Indexes


Run:

```bash
python -m src.vector_store
```


Expected output:


```text
FAISS indexes created successfully
```

---

# ▶️ Run Application


Start Streamlit:


```bash
streamlit run app.py
```


Application opens:

```text
http://localhost:8501
```

---

# 💬 Example Questions


### Disease Information

```text
Explain dengue disease
```


### Symptoms

```text
What are symptoms of malaria?
```


### Medicine

```text
Which medicine is used for fever?
```


### WHO Guidelines

```text
What does WHO recommend for malaria prevention?
```

---

# 📌 Concepts Covered

- Retrieval Augmented Generation (RAG)

- Multi-RAG Architecture

- Vector Databases

- Semantic Search

- Embeddings

- FAISS Indexing

- Retriever Routing

- Prompt Engineering

- LLM Integration

- Streamlit Deployment

---

# Future Improvements

- Add real WHO PDF documents

- Add Medical APIs

- Add SQL database RAG

- Add Agentic RAG using LangGraph

- Add conversation memory

---

