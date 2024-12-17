"""

Whisper ref:
https://openai.com/index/whisper/
https://blog.csdn.net/qq_34840129/article/details/89388897
https://ithelp.ithome.com.tw/m/articles/10347524
https://www.koc.com.tw/archives/520051
https://ithelp.ithome.com.tw/articles/10311957
"""
import os
from pathlib import Path
import whisper

class AudioToText:
    """
    class of Audio To Text
    """
    def __init__(self, model: str = "turbo"):
        self.root_dir = Path(__file__).parent.parent
        self.result_path = os.path.join(self.root_dir, 'audio')
        self.model = whisper.load_model(model)

    def audtio_to_text(self):
        audio_file = os.path.join(self.result_path, 'audio.wav')

        result = self.model.transcribe(audio=audio_file)

        return result["text"]

    def test_audio_to_text(self, file_name):
        audio_file = os.path.join(self.result_path, file_name)

        result = self.model.transcribe(audio=audio_file)

        return result["text"]

if __name__ == '__main__':
    pass
