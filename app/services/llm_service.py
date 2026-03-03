import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from app.services.vector_store import load_vector_store

llm = ChatGroq(
    temperature=0,
    model_name="llama3-8b-8192",
    api_key="YOUR_GROQ_API_KEY"
)

def get_book_assistant_chain(mode="شرح"):
    vector_db = load_vector_store()
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})

    if mode == "شرح":
        template = """أنت معلم خبير. استخدم النصوص التالية فقط لشرح المفهوم المطلوب بأسلوب مبسط.
        Context: {context}
        Question: {question}
        الشرح (باللغة العربية):"""
    else:
        template = """بناءً على النص التالي، قم بتوليد 3 أسئلة اختيار من متعدد (MCQs) مع ذكر الإجابة الصحيحة لكل سؤال.
        Context: {context}
        Question: {question}
        الأسئلة:"""

    QA_PROMPT = PromptTemplate(template=template, input_variables=["context", "question"])

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": QA_PROMPT}
    )
    return qa_chain