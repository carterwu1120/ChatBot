# from AudioRecorder.audio_recorder import AudioRecorder

# recorder = AudioRecorder()

# recorder.start_recording()

# recorded_audio = recorder.stop_recording()

# if recorded_audio is not None:
#     recorder.save_audio(recording=recorded_audio)
import gradio as gr
from UI.ui import UI

class DemoPage:

    def __init__(self):
        self.ui = UI()

    def create_interface(self):
        with gr.Blocks() as demo_interface:
            self.ui.create_interface()

        return demo_interface

if __name__ == "__main__":
    demo = DemoPage()
    demo.create_interface().launch()