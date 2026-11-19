from BRAIN.ollama import ollamaSend

buffer1 = []
buffer2 =[]
dataBuffer = []
activeBuffer = buffer1
def memory(query,answer):

    global activeBuffer
    
    if len(activeBuffer) >= 30:
        if activeBuffer is buffer1:
            activeBuffer = buffer2
            dataBuffer.append(buffer1.copy())
            buffer1.clear()
        else:
            activeBuffer = buffer1
            dataBuffer.append(buffer2.copy())
            buffer2.clear()

    activeBuffer.append({
        "user":query,
        "helen":answer
    })

    if (True):
            prompt = f'''
            You are Helen's memory analyser.
            Analyse the given conversations and extract information worth remembering about the user.
            Remember:
            - Personal details and preferences.
            - Projects, technologies and progress.
            - Goals and ambitions.
            - Important decisions and ongoing situations.
            Ignore:
            - Casual conversations.
            - Temporary questions.
            - Generic knowledge.
            - Repeated information.
            Rules:
            - Never invent information.
            - Combine related facts.
            - Assign importance from 0.0 to 1.0.
            - Return only valid JSON.
            Format:
            {
            "memories": [
                {
                "type": "project",
                "topic": "Helen",
                "content": "User is building a personal AI assistant.",
                "importance": 0.9
                }
            ]
            }

            If nothing is worth remembering, return {"memories": []}.

            the data is {dataBuffer}
            '''

            data = ollamaSend.send(prompt)
    
