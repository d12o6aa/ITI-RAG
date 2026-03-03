import streamlit as st
import os
from app.services.ingestion import load_and_split_book
from app.services.vector_store import create_vector_store
from app.services.llm_service import get_rag_chain

st.set_page_config(page_title="Smart Assistant", layout="wide")

with st.sidebar:
    api_key = st.text_input("Google API Key", type="password")
    pdf_file = st.file_uploader("Upload PDF", type="pdf")

if pdf_file and api_key:
    if "vector_db" not in st.session_state:
        file_path = f"test_data/{pdf_file.name}"
        with open(file_path, "wb") as f:
            f.write(pdf_file.getvalue())
        
        chunks = load_and_split_book(file_path)
        st.session_state.vector_db = create_vector_store(chunks)
        st.success("Document Ready (Modular Version)!")

    query = st.text_input("Ask about the book:")
    if query:
        chain = get_rag_chain(st.session_state.vector_db, api_key)
        response = chain.invoke({"query": query})
        st.write(response["result"])