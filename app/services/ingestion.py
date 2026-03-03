from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.core.constants import CHUNK_SIZE, CHUNK_OVERLAP

def load_and_split_book(file_path):
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len
    )
    chunks = text_splitter.split_documents(documents)
    
    print(f"Book splited to {len(chunks)}")
    return chunks