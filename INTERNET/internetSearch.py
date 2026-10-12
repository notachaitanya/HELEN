from ddgs import DDGS

def internetSearch(query):
    results = DDGS().text(query,max_results=10)
    
    if not results:
        return "No search results found."
    
    output = []
    
    for item in results:
        output.append(
            f"Title: {item['title']}\n"
            f"Summary: {item['body']}\n"
            f"URL: {item['href']}"
        )

    return "\n\n".join(output)


print(internetSearch("what is latest driver standings in f1"))