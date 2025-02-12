from ultralytics import YOLO

# Load YOLOv10n model
model = YOLO("/Trained with RGB Images _ Finaly/olov10n.pt")

# Train the model
model.train(data="/Trained with RGB Images _ Final/data.yaml", epochs=100, imgsz=640, patiences = 3, batch_size = 32)