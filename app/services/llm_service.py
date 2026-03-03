from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def get_rag_chain(vector_db, api_key, mode="Explain"):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=api_key)
    
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