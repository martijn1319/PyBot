import sounddevice as sd
import soundfile as sf

def play_audio(file_path):
    # Load the audio file
    audio, fs = sf.read(file_path, dtype='float32')

    # Play the audio
    sd.play(audio, fs)
    sd.wait()  # Wait until the sound has finished playing

# Example usage
play_audio('/phrases/countdown/one.wav')
