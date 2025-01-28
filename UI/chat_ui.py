import os
from pathlib import Path
import gradio as gr
from package.audio_recorder import AudioRecorder
from package.audio_text_processor import AudioTextProcessor

class ChatUI:
    """
    class of UI for development
    """
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent
        self.audio_recorder = AudioRecorder()
        self.audio_text_processor = AudioTextProcessor()

    def __start_record(self):
        gr.Info('Recording has started')
        self.audio_recorder.start_recording()

    def __stop_record(self):
        gr.Info('Recording has stopped')
        audio_chunks = self.audio_recorder.stop_recording()
        self.audio_recorder.save_audio(audio_chunks=audio_chunks)
        texts = self.audio_text_processor.audio_to_text()

        return [gr.update(value = os.path.join(self.root_dir, 'result', 'output.wav')), gr.update(value = texts)]
 
    def create_interface(self):

        start_record_btn = gr.Button(value = "Start Record")
        start_record_btn.click(
            fn = self.__start_record
        )
        stop_record_btn = gr.Button(value = "Stop Record")

        with gr.Row():
            with gr.Column():
                user_audio = gr.Audio(
                    value = None
                )
                user_textarea = gr.TextArea(
                    value = ""
                )

            with gr.Column():
                tutor_audio = gr.Audio(
                    value = None
                )
                tutor_textarea = gr.TextArea(
                    value = ""
                )
        stop_record_btn.click(
            fn = self.__stop_record,
            inputs = None,
            outputs = [user_audio, user_textarea, tutor_audio, tutor_textarea]
        )  
