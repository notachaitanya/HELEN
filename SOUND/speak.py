
from kokoro import KPipeline
import pyaudio
import numpy as np
import time

print("Loading Helen's voice...")

pipeline = KPipeline(
    lang_code='a',
    device='cuda'
)

# Warm up Kokoro
print("Warming up Helen's voice...")

for _, _, _ in pipeline(
    "Hello, I am ready.",
    voice='af_heart',
    speed=1.15
):
    pass

print("Helen's voice is ready!")

audio = None
stream = None


def initialize_audio():
    global audio, stream

    print("Initializing audio output...")

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=24000,
        output=True
    )

    print("Audio output ready!")


def speak(text):

    start_time = time.perf_counter()
    first_chunk = True

    print("Helen is speaking...")

    generator = pipeline(
        text,
        voice='af_heart',
        speed=1.15
    )

    for _, _, chunk in generator:

        if first_chunk:
            print(
                "Time to first audio:",
                round(time.perf_counter() - start_time, 2),
                "seconds"
            )
            first_chunk = False

        stream.write(
            np.asarray(chunk, dtype=np.float32).tobytes()
        )

    print(
        "Total speech time:",
        round(time.perf_counter() - start_time, 2),
        "seconds"
    )


def shutdown():

    global audio, stream

    if stream is not None:
        stream.stop_stream()
        stream.close()

    if audio is not None:
        audio.terminate()

    print("Helen's audio system closed.")
