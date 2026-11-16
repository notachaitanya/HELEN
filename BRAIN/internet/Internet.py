from ddgs import DDGS
from rapidfuzz import fuzz
from flashrank import Ranker, RerankRequest


ranker = Ranker()
def search(question):
    allTitles = []
    duplicates = set()
    uniqueResults = []
    passages =[]
    finalResults=[]   # contains final results after removing duplicates and removing less ranked results
    results = DDGS().text(
        query=question,
        backend ="auto",
        max_results=10,
    )

    #rapid fuzz ------ removing duplicate or very similar results. 
    for result in results:
        allTitles.append(result["title"])
    
    for i in range(0,len(results)):
        for j in range(i+1,len(results)):
            score = fuzz.ratio(allTitles[i],allTitles[j])
            
            if score>90:
                duplicates.add(j)
            else:
                continue
            
    for i,result in enumerate(results):
        if i not in duplicates:
            uniqueResults.append(result)
            
    # flash ranking ----- ranking relavent results.
    for i,result in enumerate(uniqueResults):
        passages.append(
            {
            "id":i,
            "text":result["title"]+". "+result.get("body", "")
            }
        )
    
    request = RerankRequest(
        query=question,
        passages=passages
    )
    rankedResults = ranker.rerank(request)
    for result in rankedResults:
        if result["score"]<0.8:
            continue
        else:
            finalResults.append(result)
            
    
    

