import gradio as gr
from UI.dev_ui import DevUI
from UI.toeic_ui import ToeicUI
from UI.chat_ui import ChatUI

class DemoPage:
    """
    class of Demo Page
    """
    def __init__(self):
        self.dev_ui = DevUI()
        self.toeic_ui = ToeicUI()
        self.chat_ui = ChatUI()

    def create_interface(self):
        """
        create all user interface
        """
        with gr.Blocks() as demo_interface:
            with gr.Tab("Dev UI"):
                self.dev_ui.create_interface()
            with gr.Tab("Chat UI"):
                self.chat_ui.create_interface()
            with gr.Tab("TOEIC UI"):
                self.toeic_ui.create_interface()

        return demo_interface

if __name__ == "__main__":
    demo = DemoPage()
    demo.create_interface().launch(server_name='0.0.0.0')
