from ultralytics import YOLO

model = YOLO("models/alpr_yolov8n_640.pt")

def main():
    model.val(
        data="configs/alpr_data.yaml",
        imgsz=640,
        batch=16
    )

if __name__ == "__main__":
    main()