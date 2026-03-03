import gradio as gr
from app.services.ingestion import load_and_split_book
from app.services.vector_store import create_vector_store
from app.services.llm_service import get_book_assistant_chain

def handle_upload(file):
    if file is None:
        return "Please upload a file first."
    
    chunks = load_and_split_book(file.name)
    
    create_vector_store(chunks)
    
    return "✅ Document processed successfully! You can now go to the Chat tab." 

def handle_chat(user_question, mode):
    qa_chain = get_book_assistant_chain(mode=mode)
    
    result = qa_chain({"query": user_question})
    
    answer = result["result"]
    sources = "\n\n📌 Sources:\n" + "\n".join([doc.metadata.get('source', 'Unknown') for doc in result["source_documents"]])
    
    return answer + sources

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📚 Smart Book & Contract Assistant")
    
    with gr.Tabs():
        with gr.TabItem("⬆️ Upload Document"):
            file_input = gr.File(label="Upload PDF or DOCX", file_types=[".pdf", ".docx"])
            upload_btn = gr.Button("Process Document", variant="primary")
            status_output = gr.Textbox(label="Status", interactive=False)
            upload_btn.click(handle_upload, inputs=file_input, outputs=status_output)
            
        with gr.TabItem("💬 Explanation & Q&A"):
            mode_radio = gr.Radio(
                choices=["Explain", "Generate Questions"], 
                label="Interaction Mode", 
                value="Explain"
            )
            chat_input = gr.Textbox(label="Ask a question or request a summary/questions")
            chat_btn = gr.Button("Submit", variant="primary")
            chat_output = gr.Textbox(label="AI Assistant Response", lines=12) 
            
            chat_btn.click(handle_chat, inputs=[chat_input, mode_radio], outputs=chat_output)

if __name__ == "__main__":
    demo.launch()