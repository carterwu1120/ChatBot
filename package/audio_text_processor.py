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
# from .grammar_analyzer import GrammarAnalyzer
from .pronunciation_analyzer import PronunciationAnalyzer

class AudioTextProcessor:
    """
    class of Audio To Text
    """
    def __init__(self, model: str = "turbo"):
        self.root_dir = Path(__file__).parent.parent
        self.audio_user_path = os.path.join(self.root_dir, 'audio_user')
        self.audio_tutor_path = os.path.join(self.root_dir, 'audio_tutor')
        self.model = whisper.load_model(model)

    def audio_to_text(self, audio_file=None):
        """
        convert audio to text
        """
        if audio_file is None:
            audio_file = os.path.join(self.audio_user_path, 'output.wav')
            
        result = self.model.transcribe(audio=audio_file)
        text = result["text"]
        
        # Analyze grammar and pronunciation
        # grammar_feedback = self.analyze_grammar(text)
        # pronunciation_feedback = self.analyze_pronunciation(audio_file)
        
        return text
        
    # def analyze_grammar(self, text):
    #     """Analyze grammar in the text."""
    #     analyzer = GrammarAnalyzer()
    #     return analyzer.analyze_grammar(text)
        
    # def analyze_pronunciation(self, audio_file):
    #     """Analyze pronunciation in the audio."""
    #     analyzer = PronunciationAnalyzer()
    #     return analyzer.analyze_pronunciation(audio_file)
    
    def text_to_audio(self, text):
        """Convert text to audio (placeholder for future implementation)"""
        pass

    def test_audio_to_text(self, file_name):
        """Test method for audio to text conversion"""
        audio_file = os.path.join(self.audio_user_path, file_name)
        result = self.audio_to_text(audio_file)
        return result