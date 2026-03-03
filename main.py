from fastapi import FastAPI
import uvicorn
from ui.gradio_app import demo
import gradio as gr

app = FastAPI(title="Smart Contract/Book Assistant API")

app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)