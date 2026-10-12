from BRAIN.prefrontalCortex import ollamaSend
from VISION.unTrainedModel import personsIdentifier
from SOUND import listen
from SOUND import speak
from INTERNET import internetSearch

query = listen.listen()
result = ollamaSend.send(query)
answer = result["message"]["content"]
speak.speak(answer)

internetSearch.internetSearch("what is latest driver standings in formula 1")



