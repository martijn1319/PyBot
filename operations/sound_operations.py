import sounddevice as sd
import soundfile as sf
import numpy as np

def add_distortion(audio, gain=1.0, threshold=0.5):
    # Apply gain
    audio = audio * gain

    # Clip the signal
    audio = np.clip(audio, -threshold, threshold)

    return audio

def play_distorted_audio(file_path, gain=2.0, threshold=0.5, buffer_size=1024):
    # Load the audio file
    audio, fs = sf.read(file_path)

    # Apply distortion (this is just a placeholder; your actual distortion code may differ)
    distorted_audio = audio * gain
    distorted_audio[distorted_audio > threshold] = threshold
    distorted_audio[distorted_audio < -threshold] = -threshold

    # Convert to float32 to match sounddevice requirements
    distorted_audio = distorted_audio.astype(np.float32)

    # Handle 1D (mono) or 2D (stereo) audio
    channels = 1 if len(distorted_audio.shape) == 1 else distorted_audio.shape[1]

    # Play the distorted audio
    with sd.OutputStream(samplerate=fs, channels=channels, blocksize=buffer_size) as stream:
        stream.write(distorted_audio)

# Example usage
play_distorted_audio('./operations/media/audio/test.wav', gain=10.0, threshold=0.5)
