import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from app.services.vector_store import load_vector_store

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key="YOUR_GEMINI_API_KEY",
    temperature=0 
)

def get_book_assistant_chain(mode="Explain"):
    vector_db = load_vector_store()
    retriever = vector_db.as_retriever(search_kwargs={"k": 5})

    if mode == "Explain":
        template = """You are an expert tutor. Use the provided context to explain the concept simply.
        Context: {context}
        Question: {question}
        Explanation:"""
    else:
        template = """Based on the following text, generate 3 multiple-choice questions with answers.
        Context: {context}
        Question: {question}
        Questions:"""

    QA_PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_PROMPT}
    )