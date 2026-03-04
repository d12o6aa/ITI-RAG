# 📚 Smart Book Assistant (RAG System)

## 🌐 Live Demo
You can try the live application here: [**Smart Book Assistant on Streamlit Cloud**](https://smart-book-assistant.streamlit.app/)

## 🎯 Project Overview
The core idea of this project is a robust **RAG (Retrieval-Augmented Generation) System**. It allows users to upload a PDF file, process it through a professional RAG pipeline, and interact with its content. The ultimate goal is to query the assistant about any information within the file and receive accurate, context-aware responses.

## 🏗️ Architecture & Tools
- **Modular Structure**: The project is built using a clean, modular Python structure for better maintainability and scalability.
- **Framework**: Developed strictly using **LangChain** to orchestrate the RAG components.
- **LLM**: **Google Gemini 1.5 Flash** (Chosen for its high speed, large context window, and multilingual support).
- **Vector Database (VDB)**: **FAISS** (Chosen for its efficiency in local similarity search and lightweight footprint).
- **Frontend**: **Streamlit** (Chosen for its seamless integration with Python and superior user experience).

## 📁 Project Structure
```text
ITI-RAG/
├── app/
│   ├── core/
│   │   └── constants.py      # Configuration & Constants (Chunk size, Paths)
│   └── services/
│       ├── ingestion.py      # PDF Processing & Semantic Chunking
│       ├── vector_store.py   # FAISS & Embeddings Management
│       └── llm_service.py    # Gemini Integration & RAG Chain Logic
├── test_data/                # Dedicated folder for sample PDFs
├── app.py                    # Streamlit Interface (Main Entry Point)
├── Dockerfile                # Docker Image configuration
├── docker-compose.yml        # Docker Compose orchestration
├── requirements.txt          # Project Dependencies
└── README.md                 # Project Documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Docker & Docker Compose (optional)
- Google Gemini API Key

### Installation

**Clone the repository:**
```bash
git clone https://github.com/d12o6aa/ITI-RAG.git
cd ITI-RAG
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

### Run Locally

**Option 1: Direct Python**
```bash
streamlit run app.py
```

**Option 2: Docker**
```bash
docker-compose up --build
```

## 🛠️ Usage
1. Open the application (locally or via the Live Demo link).
2. Enter your Google Gemini API Key in the sidebar.
3. Select a file from the `test_data/` folder or upload a new PDF.
4. Wait for the "Document ready!" message.
5. Start asking questions about your file!

---
