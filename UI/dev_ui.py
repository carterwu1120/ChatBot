import os
from pathlib import Path
import gradio as gr
from package.audio_recorder import AudioRecorder
from package.audio_to_text import AudioToText

class DevUI:
    """
    class of UI for development
    """
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent
        self.audio_recorder = AudioRecorder()
        self.audio_to_text = AudioToText()

    def __start_record(self):
        gr.Info('Recording has started')
        self.audio_recorder.start_recording()

    def __stop_record(self):
        gr.Info('Recording has stopped')
        audio_chunks = self.audio_recorder.stop_recording()
        self.audio_recorder.save_audio(audio_chunks=audio_chunks)
        texts = self.audio_to_text.audtio_to_text()

        return [gr.update(value = os.path.join(self.root_dir, 'result', 'output.wav')), gr.update(value = texts)]

    def __test_result_audio(self, audio_name: str):
        """
        test audio which have been saved at result
        """
        text = self.audio_to_text.test_audio_to_text(audio_name)

        return gr.update(value = text)
        
    def create_interface(self):
        audio_file_list = os.listdir(os.path.join(self.root_dir, "audio"))

        start_record_btn = gr.Button(value = "Start Record")
        start_record_btn.click(
            fn = self.__start_record
        )
        stop_record_btn = gr.Button(value = "Stop Record")

        audio_file_dropdown = gr.Dropdown(
            choices = audio_file_list,
            label = "Select Audio",
            info = "Select a audio"
        )
        test_btn = gr.Button(
            value = "Test"
        )

        user_audio = gr.Audio(
            value = None
        )
        user_textarea = gr.TextArea(
            value = ""
        )
        stop_record_btn.click(
            fn = self.__stop_record,
            inputs = None,
            outputs = [user_audio, user_textarea]
        )

        audio_file_dropdown.change(
            fn = lambda x: gr.update(value = os.path.join(self.root_dir, 'result', x)),
            inputs = audio_file_dropdown,
            outputs = user_audio
        )
        test_btn.click(
            fn = self.__test_result_audio,
            inputs = [audio_file_dropdown],
            outputs = user_textarea
        )