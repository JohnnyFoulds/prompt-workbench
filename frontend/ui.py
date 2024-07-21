import gradio as gr


def create_ui(fn):
    inputs = gr.Textbox(lines=2, placeholder="Enter your text here...")
    outputs = gr.Textbox()

    return gr.Interface(fn=fn, inputs=inputs, outputs=outputs)

