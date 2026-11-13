
import pyaudio
import numpy as np
from openwakeword.model import Model


# Audio configuration
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1280
THRESHOLD = 0.5


def initialize_wakeword():
    """Load Helen's custom ONNX wake-word model."""

    model = Model(
        wakeword_models=["models/helen.onnx"],
        inference_framework="onnx"
    )

    return model


def initialize_microphone():
    """Initialize PyAudio and open the microphone stream."""

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    return audio, stream


def listen_for_wakeword(model, stream):
    """Read one audio chunk and check for Helen's wake word."""

    audio_data = stream.read(
        CHUNK,
        exception_on_overflow=False
    )

    audio_array = np.frombuffer(
        audio_data,
        dtype=np.int16
    )

    prediction = model.predict(audio_array)
    score = prediction["helen"]

    if score > THRESHOLD:
        print(f"Helen detected! Confidence: {score:.3f}")
        model.reset()
        return True

    return False


def start_wakeword_detection():

    model = initialize_wakeword()
    audio, stream = initialize_microphone()

    print("Helen is listening...")

    try:
        while True:

            if listen_for_wakeword(model, stream):
                return True
    except KeyboardInterrupt:
        print("\nStopping Helen...")
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        

