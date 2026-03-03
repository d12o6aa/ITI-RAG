import streamlit as st
import os

# --- حل سحري لمشكلة الـ Event Loop في Gemini ---
import asyncio
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())
# ----------------------------------------------

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="Smart Assistant", layout="wide")
st.title("📚 Smart Assistant")

with st.sidebar:
    api_key = st.text_input("Google API Key", type="password")
    pdf_file = st.file_uploader("Upload PDF", type="pdf")

if pdf_file and api_key:
    if "vector_db" not in st.session_state:
        with open("temp.pdf", "wb") as f:
            f.write(pdf_file.getvalue())
        
        loader = PyMuPDFLoader("temp.pdf")
        chunks = RecursiveCharacterTextSplitter(chunk_size=1000).split_documents(loader.load())
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        st.session_state.vector_db = FAISS.from_documents(chunks, embeddings)
        st.success("Document ready!")

    query = st.text_input("Ask about the book:")
    if query:
        docs = st.session_state.vector_db.similarity_search(query, k=3)
        context = "\n".join([d.page_content for d in docs])
        
        # تعريف الموديل هنا بيحل مشاكل الـ Async
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
        prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
        
        response = llm.invoke(prompt)
        st.write("### Response:")
        st.write(response.content)