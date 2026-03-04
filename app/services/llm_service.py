import asyncio

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from app.core.constants import MODEL_NAME

def get_rag_chain(vector_db, api_key, mode="Explain"):
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())
    llm = ChatGoogleGenerativeAI(model=MODEL_NAME, google_api_key=api_key)
    
    template = """You are an expert tutor. Use the context to answer.
    Context: {context}
    Question: {question}
    Answer:"""
    
    if mode == "Generate Questions":
        template = "Based on context: {context}, generate 3 MCQs for: {question}"

    prompt = PromptTemplate(template=template, input_variables=["context", "question"])

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_db.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )