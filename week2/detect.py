from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Run object detection
results = model(
    source="input_images",
    save=True,
    conf=0.25
)

print("Detection completed successfully")