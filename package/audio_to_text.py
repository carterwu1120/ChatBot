"""

Whisper ref:
https://openai.com/index/whisper/
https://blog.csdn.net/qq_34840129/article/details/89388897
https://ithelp.ithome.com.tw/m/articles/10347524
"""
import speech_recognition as sr

class AutioToText:
    def __init__(self, model: str = "turbo"):
        self.model = None
