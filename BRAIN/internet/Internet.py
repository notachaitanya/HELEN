
from ddgs import DDGS
from ddgs.exceptions import DDGSException
from rapidfuzz import fuzz
from flashrank import Ranker, RerankRequest
import requests
import trafilatura


ranker = Ranker()


def search(question):

    allTitles = []
    duplicates = set()
    uniqueResults = []
    passages = []
    URLs = []
    data = []
    finalResults = []

    # 1. Search the internet
    try:
        results = DDGS().text(
            query=question,
            backend="Yahoo",
            max_results=10
        )

    except DDGSException as error:
        print("SEARCH FAILED:", error)
        return []

    if not results:
        print("SEARCH RETURNED NO RESULTS")
        return []

    # 2. Remove duplicate results
    for result in results:
        allTitles.append(result.get("title", ""))

    for i in range(len(allTitles)):
        for j in range(i + 1, len(allTitles)):

            score = fuzz.ratio(allTitles[i], allTitles[j])

            if score > 90:
                duplicates.add(j)

    for i, result in enumerate(results):
        if i not in duplicates:
            uniqueResults.append(result)

    # 3. Prepare passages for FlashRank
    for i, result in enumerate(uniqueResults):
        passages.append({
            "id": i,
            "text": result.get("title", "") + ". " +
                    result.get("body", "")
        })

    if not passages:
        return []

    # 4. Rank relevant results
    request = RerankRequest(
        query=question,
        passages=passages
    )

    rankedResults = ranker.rerank(request)

    for result in rankedResults:

        print("RANK SCORE:", result["score"])

        if result["score"] >= 0.8:
            finalResults.append(
                uniqueResults[result["id"]]
            )

    if not finalResults:
        print("FLASHRANK FILTERED ALL RESULTS")
        return []

    # 5. Extract webpage content
    for result in finalResults:
        url = result.get("href")

        if url:
            URLs.append(url)

    for url in URLs:

        try:
            response = requests.get(
                url,
                timeout=15,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            response.raise_for_status()

            html = response.text
            content = trafilatura.extract(html)

            if content:
                data.append(content)

        except requests.RequestException as error:
            print("PAGE FETCH FAILED:", url, error)
            continue

    print("FINAL EXTRACTED PAGES:", len(data))

    return data
