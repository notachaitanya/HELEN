import cv2 as cv
import numpy as np
from ultralytics import YOLO
import os

model = YOLO("yolo8m-face.pt")
images = []
faces = []
lables = []

DIR = r"D:\HELEN\VISION\trainedModel\images"

if not images:
    images=os.listdir(DIR)

for people in images:
    path = os.path.join(DIR,people)

    for person in people:
        personPath = os.path.join(path,person)
         
    