from ultralytics import YOLO

# Load segmentation model
model = YOLO("yolov8n-seg.pt")

# Run segmentation
results = model(
    source="../input_images",
    save=True,
    conf=0.25
)

print("Segmentation completed successfully")