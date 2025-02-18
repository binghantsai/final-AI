from ultralytics import YOLO

img = './OIP.jpg'
# Load a pre-trained YOLOv10n model
model = YOLO("train_1/runs/detect/train/weights/best.pt")

# Perform object detection on an image
results = model(img)

# Display the results
results[0].show()