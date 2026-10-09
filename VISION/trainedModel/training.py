import cv2 as cv
import numpy as np
from ultralytics import YOLO
import os

model = YOLO("yolov8m-face.pt")
faceRecognition = cv.face.LBPHFaceRecognizer_create()
images = []
faces = []
lables = []
characters = {}

DIR = r"D:\HELEN\VISION\trainedModel\images"

if not images:
    images=os.listdir(DIR)

for i,people in enumerate(images):
    path = os.path.join(DIR,people)

    for person in os.listdir(path):
        personPath = os.path.join(path,person)

        face = cv.imread(personPath)
        result = model(face)
        boxes = result[0].boxes

        if boxes is None or len(boxes) == 0:
            continue

        x1,y1,x2,y2 = result[0].boxes.xyxy[0].int().tolist()
        face = face[y1:y2,x1:x2]

        if face.size == 0:
            continue

        grey_face = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
        grey_face = cv.resize(grey_face,(200,200))
        lables.append(i)
        faces.append(grey_face)

    characters[people] = i

lables = np.array(lables)
faces = np.array(faces)

faceRecognition.train(faces,lables)
faceRecognition.save("faceRecognizer.yml")

        
    