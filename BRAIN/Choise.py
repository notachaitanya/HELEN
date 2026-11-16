
from BRAIN.ollama import ollamaSend
from BRAIN.internet import Internet


def choise(question):

    prompt1 = f"""
    Classify the user's request into exactly one category:

    1 - INTERNET: Requires current or externally researched information.
    2 - MEMORY: Requires information from previous conversations or personal stored data.
    3 - GENERAL: Can be answered using existing knowledge.

    User request: {question}

    Return only 1 for INTERNET, 2 for MEMORY.
    If the question belongs to category 3, do not return the number. Directly provide the answer.
    """

    result = ollamaSend.send(prompt1, max_tokens=500).strip()

    # INTERNET
    if result == "1":

        data = Internet.search(question)

        InternetPrompt = f"""
        You are Helen's answer engine.

        User's question:
        {question}

        Information retrieved from the internet:
        {data}

        Instructions:
        1. Use relevant information from the retrieved sources.
        2. Combine information to create an accurate answer.
        3. Acknowledge contradictions between sources.
        4. Never invent unsupported facts.
        5. If information is insufficient, say so.
        6. Answer naturally and conversationally.

        Provide only the final answer.
        """

        answer = ollamaSend.send(InternetPrompt, max_tokens=500).strip()
        return answer

    # MEMORY
    elif result == "2":
        return "Memory system is not implemented yet."

    else:
        return result
