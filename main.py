from BRAIN.prefrontalCortex import ollamaSend
from VISION.unTrainedModel import personsIdentifier
from SOUND import listen
from SOUND import speak

query = listen.listen()
result = ollamaSend.send(query)
answer = result["message"]["content"]
speak.speak(answer)



