import os
from langchain_google_genai import ChatGoogleGenerativeAI

# حطي المفتاح بتاعك هنا للتجربة
os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_API_KEY"

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
print(llm.invoke("Say Hello!").content)