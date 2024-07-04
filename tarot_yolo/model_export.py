from ultralytics import YOLO

# Load a model
model = YOLO("tarot_yolo/models/tarot_yolov9.pt")

# Export the model
onnx_file = model.export(format="onnx", dynamic=True)