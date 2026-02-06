from ultralytics import YOLO


def main(): 
# Load YOLOv8n model
    model = YOLO("yolov8n.pt")

    # Train on your dataset
    model.train(
        data="configs/alpr_data.yaml",  # dataset config
        epochs=25,              # number of epochs
        imgsz=640,              # image size
        batch=16,                # batch size 
        device=0,               # GPU 
        workers=4,              # number of data loader workers
        name="alpr_yolov8n",    # folder name to save weights & results
        exist_ok=True           # overwrite if folder exists
    )

if __name__ == "__main__":
    main()