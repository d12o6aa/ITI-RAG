from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from app.core.constants import VECTOR_DB_PATH

# اختيارنا لـ all-MiniLM-L6-v2 لأنه خفيف على جهازك Dell G12 [cite: 51]
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vector_store(chunks):
    # تحويل النص لأرقام وتخزينه [cite: 29, 30]
    vector_db = FAISS.from_documents(chunks, embeddings)
    
    # حفظ القاعدة محلياً (Local Storage) 
    vector_db.save_local(VECTOR_DB_PATH)
    return vector_db

def load_vector_store():
    # تحميل القاعدة عند الحاجة [cite: 32]
    return FAISS.load_local(VECTOR_DB_PATH, embeddings, allow_dangerous_deserialization=True)