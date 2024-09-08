from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt") 

# Train the model
results = model.train(data="C:/dev/yolov8_cats/cats.v1i.yolov8/data.yaml", epochs=100, imgsz=640)