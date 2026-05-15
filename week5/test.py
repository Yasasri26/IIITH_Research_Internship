from ultralytics import YOLO

model = YOLO("runs/detect/person_bicycle_car_model/weights/best.pt")

results = model.predict(
    source="../week4/task2/dataset/images/test",
    save=True,
    conf=0.25
)

print("Testing completed successfully")