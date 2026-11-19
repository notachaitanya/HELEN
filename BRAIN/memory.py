buffer1Full = False
buffer2Full = False
buffer1 = []
buffer2 =[]
dataBuffer = []
activeBuffer = buffer1
def memory(query,answer):
    
    if len(activeBuffer) == 30:
        if activeBuffer is buffer1:
            activeBuffer = buffer2
            buffer1Full = True
        else:
            activeBuffer = buffer1
            buffer2Full = True

    if buffer1Full:
        dataBuffer = deepcopy(buffer1)
    if buffer2Full:
        dataBuffer = deepcopy(buffer2)

    activeBuffer.append({
        "user":query,
        "helen":answer
    })
    
