from ultralytics import YOLO

model = YOLO("models/alpr_yolov8n_640.pt")

results = model.predict(
    source="datasets/Data/test/images",
    conf=0.4,
    imgsz=640,
    save=True,
    project="results",
    name="qualitative"
    )
