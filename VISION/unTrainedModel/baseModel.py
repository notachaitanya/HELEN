import cv2 as cv
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

video = cv.VideoCapture(0)

while True:
    # variables
    confidence = 0
    Class = ""
    found = False


    ifTrue , frame = video.read()
    result = model(frame)

    boxes = result[0].boxes

    for box in boxes:
        Class = model.names[int(box.cls[0])]
        confidence = float(box.conf[0])

        if Class == "person" and confidence>0.5:
            print("hell yeah")
            found = True
            break

    if found:
        break

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()