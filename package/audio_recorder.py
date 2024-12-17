import os
import queue
import threading
from pathlib import Path
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

class AudioRecorder:
    """
    class of Audio Recorder
    """
    def __init__(self, sample_rate=44100, channels=1):
        self.root_dir = Path(__file__).parent.parent
        self.result_path = os.path.join(self.root_dir, 'audio')
        self.sample_rate = sample_rate
        self.channels = channels
        self.record_thread = threading.Thread(target=self.__record_audio, daemon=True)
        self.is_recording = False
        self.audio_queue = queue.Queue()

    def start_recording(self):
        """
        Start recording audio in a separate thread
        """
        self.is_recording = True
        if not self.record_thread.is_alive():
            self.record_thread = threading.Thread(target=self.__record_audio, daemon=True)
        self.record_thread.start()
        print("Recording started. Use stop_recording() to end.")

    def __record_audio(self):
        """
        Continuous audio recording method
        """

        while self.is_recording:
            # record for a short chunk (e.g., 0.5s)
            chunk = sd.rec(
                int(3*self.sample_rate),
                samplerate=self.sample_rate,
                channels=self.channels,
                dtype='float64'
            )
            sd.wait()
            self.audio_queue.put(chunk)

    def stop_recording(self):
        """
        Stop the recording and collect all audio chunks
        """
        if not self.is_recording:
            print("No recording in progress.")
            return None

        self.is_recording = False
        self.record_thread.join()

        # Collect all audio chunks
        audio_chunks = []
        while not self.audio_queue.empty():
            audio_chunks.append(self.audio_queue.get())

        # # Concatenate the chunks
        audio_chunks = np.concatenate(audio_chunks)
        print("Recording stopped.")
        return audio_chunks

    def save_audio(self, audio_chunks, filename='audio.wav'):
        """
        Save recorded audio to a WAV file
        """
        if audio_chunks is None:
            print("No audio to save.")
            return

        # # Normalize the audio
        normalized_recording = audio_chunks / np.max(np.abs(audio_chunks))

        # Save the recording
        os.makedirs(self.result_path, exist_ok=True)
        output_path = os.path.join(self.result_path, filename)

        write(output_path, self.sample_rate, (normalized_recording * 32767).astype(np.int16))
        print(f"Audio saved to {output_path}")

