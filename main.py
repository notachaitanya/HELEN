from BRAIN.prefrontalCortex import ollamaSend
from VISION.unTrainedModel import personsIdentifier

result = ollamaSend.send("who am i")
print(result["message"]["content"])

number = personsIdentifier()

if number > 1:
    print(f"two more ppl in room ${number}")
