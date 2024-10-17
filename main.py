from PyQt5.QtCore import showbase
from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO11n model on the 'bus.jpg' image
results = model("./AQNCPkYWm6OLGBCJqCL2Zdr_OAnxz2REeYeP5DTjEGMLStQjzlIsJpaVKFUxBhvtw4sxL62We9vvnrIVW0Tb--m4.mp4", save=True, show=True)