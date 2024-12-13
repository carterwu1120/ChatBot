"""

Whisper ref:
https://openai.com/index/whisper/
https://blog.csdn.net/qq_34840129/article/details/89388897
https://ithelp.ithome.com.tw/m/articles/10347524
"""
import os
from pathlib import Path
import speech_recognition as sr

class AutioToText:
    def __init__(self, sample_rate: int = 4410):
        self.root_dir = Path(__file__).parent.parent
        self.result_path = os.path.join(self.root_dir, 'result')
        self.sr_recognizer = sr.Recognizer()
        self.sample_rate = sample_rate

    def autio_to_text(self, audio_chunks):

        audio_file = os.path.join(self.result_path, 'output.wav')
        audio_ex = sr.AudioFile(audio_file)
        with audio_ex as source:
            audio_data = self.sr_recognizer.record(source=source)
        try:
            text = self.sr_recognizer.recognize_google(audio_data=audio_data, language = 'en-US')
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

if __name__ == '__main__':
    root_dir = Path(__file__).parent.parent
    autio_to_text = AutioToText()
    wave_path = os.path.join(root_dir, 'result', 'output3.wav')
    audio_ex = sr.AudioFile(wave_path)
    with audio_ex as source:
        audio_data = autio_to_text.sr_recognizer.record(audio_ex)
    print(autio_to_text.autio_to_text(audio_data))


