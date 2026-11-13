from ddgs inport DDGS

def search(question):
    results = DDGS().text(
        query=question
        backend ="auto",
        max_results=10,
    )