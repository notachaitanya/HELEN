
# import pyaudio
# import wave
# import whisper
# import numpy as np
# import time

# model = whisper.load_model("base")

# SILENCE_DURATION = 1.2
# SILENCE_THRESHOLD = 500
# CHUNK = 3200


# def listen():
#     audio = pyaudio.PyAudio()

#     stream = audio.open(
#         format=pyaudio.paInt16,
#         channels=1,
#         rate=16000,
#         input=True,
#         frames_per_buffer=CHUNK
#     )

#     frames = []
#     silence_start = None

#     print("Recording...")

#     try:
#         while True:
#             data = stream.read(
#                 CHUNK,
#                 exception_on_overflow=False
#             )

#             frames.append(data)

#             audio_array = np.frombuffer(
#                 data,
#                 dtype=np.int16
#             )

#             volume = np.sqrt(
#                 np.mean(audio_array.astype(np.float32) ** 2)
#             )

#             if volume < SILENCE_THRESHOLD:

#                 if silence_start is None:
#                     silence_start = time.time()

#                 elif time.time() - silence_start >= SILENCE_DURATION:
#                     break

#             else:
#                 silence_start = None

#         print("Processing audio...")

#         with wave.open("voice.wav", "wb") as file:
#             file.setnchannels(1)
#             file.setsampwidth(
#                 audio.get_sample_size(pyaudio.paInt16)
#             )
#             file.setframerate(16000)
#             file.writeframes(b"".join(frames))

#     finally:
#         if stream.is_active():
#             stream.stop_stream()

#         stream.close()
#         audio.terminate()

#     result = model.transcribe(
#         "voice.wav",
#         language="en",
#         fp16=False
#     )

#     return result["text"].strip()


import pyaudio
import numpy as np
import time

SILENCE_DURATION = 0.8
SILENCE_THRESHOLD = 500
CHUNK = 3200


def listen():

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=CHUNK
    )

    speech_started = False
    silence_start = None

    print("Helen is listening...")

    try:
        while True:

            data = stream.read(
                CHUNK,
                exception_on_overflow=False
            )

            audio_array = np.frombuffer(
                data,
                dtype=np.int16
            )

            volume = np.sqrt(
                np.mean(audio_array.astype(np.float32) ** 2)
            )

            if volume >= SILENCE_THRESHOLD:

                speech_started = True
                silence_start = None

            elif speech_started:

                if silence_start is None:
                    silence_start = time.time()

                elif time.time() - silence_start >= SILENCE_DURATION:

                    print("Speech finished.")
                    return True

    finally:

        if stream.is_active():
            stream.stop_stream()

        stream.close()
        audio.terminate()

