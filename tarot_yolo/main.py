from ultralytics import YOLO
#from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

model = YOLO('models/tarot_yolov9.pt')

#results = model('https://raw.githubusercontent.com/ultralytics/yolov5/master/data/images/bus.jpg', show=True, save=True)

results = model.predict(source="0", show=True)