import ollama

def send(text):
    result = ollama.chat(
        model="gemma2:2b",
        messages=[
            {
                "role" : "nota",
                "content" : text
            }
        ]   
    )
    return result
