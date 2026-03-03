# 📚 Smart Book Assistant (RAG System)

## 🎯 Project Overview

The core idea of this project is a robust RAG (Retrieval-Augmented Generation) System. It allows users to upload a PDF file, process it through a professional RAG pipeline, and interact with the content. The ultimate goal is to query the assistant about any information within the file and receive accurate, context-aware responses.

## 🏗️ Architecture & Tools

- **Modular Structure**: The project is built using a clean, modular Python structure rather than notebooks for better maintainability and scalability.
- **Framework**: Developed strictly using LangChain to orchestrate the RAG components.
- **LLM**: Google Gemini 1.5 Flash (Chosen for its high speed, large context window, and multilingual support).
- **Vector Database (VDB)**: FAISS (Chosen for its efficiency in local similarity search and lightweight footprint).
- **Frontend**: Streamlit (Chosen for its seamless integration with Python and superior user experience).

## 📁 Project Structure

```
├── app/
│   ├── services/
│   │   ├── ingestion.py      # PDF Processing & Chunking
│   │   └── vector_store.py   # FAISS & Embeddings Management
├── ui/
│   └── app.py                # Streamlit Interface
├── test_data/                # Sample PDFs for testing
├── requirements.txt          # Project Dependencies
└── README.md                 # Documentation
```

## 🛠️ Usage

1. Open the local URL provided by Streamlit (usually `http://localhost:8501`).
2. Enter your Google Gemini API Key in the sidebar.
3. Upload a PDF from the `test_data/` folder.
4. Wait for the "Document ready!" message.
5. Start asking questions about your file!
