
import ollama

def send(text, max_tokens=256):
    result = ollama.chat(
        model="gemma2:2b",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ],
        keep_alive=-1,
        options={
            "num_predict": max_tokens,
            "temperature": 0
        }
    )

    return result["message"]["content"].strip()
