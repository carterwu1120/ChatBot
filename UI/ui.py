import os
from pathlib import Path
import gradio as gr
from package.audio_recorder import AudioRecorder
from package.audio_to_text import AutioToText

class UI:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent
        self.audio_recorder = AudioRecorder()
        self.audio_to_text = AutioToText()

    def __start_record(self):
        gr.Info('Recording has started')
        self.audio_recorder.start_recording()

    def __stop_record(self):
        gr.Info('Recording has stopped')
        audio_chunks = self.audio_recorder.stop_recording()
        self.audio_recorder.save_audio(audio_chunks=audio_chunks)
        texts = self.audio_to_text.autio_to_text(audio_chunks=audio_chunks)
        print(texts)

        return gr.update(value = os.path.join(self.root_dir, 'result', 'output.wav'))

    def create_interface(self):
        start_record_btn = gr.Button(value = "Start")
        start_record_btn.click(
            fn = self.__start_record
        )
        stop_record_btn = gr.Button(value = "Stop")

        user_audio = gr.Audio(
            value = None
        )
        stop_record_btn.click(
            fn = self.__stop_record,
            inputs = None,
            outputs = user_audio
        )