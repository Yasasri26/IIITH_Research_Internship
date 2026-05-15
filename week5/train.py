from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="../week4/task2/dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    name="person_bicycle_car_model"
)