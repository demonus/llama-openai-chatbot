import gradio as gr
from llama_index import StorageContext, \
    load_index_from_storage


def chatbot(input_text):
    return index.as_query_engine().query(input_text)


iface = gr.Interface(fn=chatbot,
                     inputs=gr.components.Textbox(lines=7, label="Enter your text"),
                     outputs="text",
                     title="Custom-trained AI Chatbot")

storage_context = StorageContext.from_defaults(persist_dir='./data')
index = load_index_from_storage(storage_context)

iface.launch(share=True)
