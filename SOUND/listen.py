
import keyboard
import pyaudio
import wave
import whisper

model = whisper.load_model("base")

def listen():
    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=3200
    )

    frames = []

    try:
        keyboard.wait("s")

        print("Recording...")

        while keyboard.is_pressed("s"):
            data = stream.read(
                3200,
                exception_on_overflow=False
            )
            frames.append(data)

        print("Processing audio...")

        with wave.open("voice.wav", "wb") as file:
            file.setnchannels(1)
            file.setsampwidth(audio.get_sample_size(
                pyaudio.paInt16
            ))
            file.setframerate(16000)
            file.writeframes(b"".join(frames))

    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

    result = model.transcribe("voice.wav")
    return result["text"].strip()
