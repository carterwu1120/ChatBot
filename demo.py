import gradio as gr
from UI.dev_ui import DevUI
from UI.ui import UI

class DemoPage:

    def __init__(self):
        self.dev_ui = DevUI()

    def create_interface(self):
        with gr.Blocks() as demo_interface:
            self.dev_ui.create_interface()

        return demo_interface

if __name__ == "__main__":
    demo = DemoPage()
    demo.create_interface().launch()