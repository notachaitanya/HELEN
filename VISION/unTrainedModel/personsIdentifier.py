
import cv2 as cv
from ultralytics import YOLO

def personIdentifier():
    model = YOLO("yolo11n.pt")
    video = cv.VideoCapture(0)
    frame_count = 0

    while True:
        ret, frame = video.read()

        if not ret:
            break

        frame_count += 1

        if frame_count % 5 == 0:
            tracker = 0
            results = model(frame)

            for result in results:
                boxes = result.boxes

                for box in boxes:
                    class_id = int(box.cls[0])
                    name = model.names[class_id]

                    if name == "person":
                        tracker += 1

            print("People detected:", tracker)

        if cv.waitKey(1) & 0xFF == ord("d"):
            break

    video.release()
    cv.destroyAllWindows()
