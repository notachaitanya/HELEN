from ultralytics import YOLO
import cv2 as cv

vid = cv.VideoCapture(0)
model = YOLO("yolo11n.pt")
while(True):
    ifTrue,frame = vid.read()
    results = model(frame)
    annotated_frame = results[0].plot()

    cv.imshow("YOLO Object Detection", annotated_frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break
    
cv.destroyAllWindows()
vid.release()