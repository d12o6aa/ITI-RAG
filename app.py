import streamlit as st
import os
from app.services.ingestion import load_and_split_book
from app.services.vector_store import create_vector_store
from app.services.llm_service import get_rag_chain
from app.core.constants import TEST_DATA_DIR
st.set_page_config(page_title="Smart Assistant", layout="wide")
st.title("Smart Book Assistant")



if not os.path.exists(TEST_DATA_DIR):
    os.makedirs(TEST_DATA_DIR)

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Google API Key", type="password")
    

    upload_option = st.radio("Choose PDF Source:", ["Select from Test Data", "Upload New File"])
    
    selected_file_path = None
    
    if upload_option == "Select from Test Data":

        existing_files = [f for f in os.listdir(TEST_DATA_DIR) if f.endswith('.pdf')]
        if existing_files:
            selected_file = st.selectbox("Select a file:", existing_files)
            selected_file_path = os.path.join(TEST_DATA_DIR, selected_file)
        else:
            st.warning("No PDF files found in test_data folder.")
    else:
        pdf_file = st.file_uploader("Upload PDF", type="pdf")
        if pdf_file:
            selected_file_path = os.path.join(TEST_DATA_DIR, pdf_file.name)
            with open(selected_file_path, "wb") as f:
                f.write(pdf_file.getvalue())

if selected_file_path and api_key:
    if "current_file" not in st.session_state or st.session_state.current_file != selected_file_path:
        with st.spinner(f"Processing {os.path.basename(selected_file_path)}..."):
            chunks = load_and_split_book(selected_file_path)
            st.session_state.vector_db = create_vector_store(chunks)
            st.session_state.current_file = selected_file_path
            st.success(f"Loaded: {os.path.basename(selected_file_path)}")

    query = st.text_input("Ask about the book:")
    if query:
        with st.spinner("Thinking..."):
            chain = get_rag_chain(st.session_state.vector_db, api_key)
            response = chain.invoke({"query": query})
            st.write("### Response:")
            st.write(response["result"])
else:
    st.info("Please provide an API Key and select/upload a PDF.")