import cv2
from ultralytics import YOLO
import argparse
import os

def run_inference(model_path, image_path, save_dir="output"):
    # Load YOLOv8 model
    model = YOLO(model_path)
    
    # Ensure output directory exists
    os.makedirs(save_dir, exist_ok=True)

    # Run inference
    results = model(image_path)

    # Loop over results (usually 1 if single image)
    for i, result in enumerate(results):
        # Show image with boxes
        result.plot(show=True)  # fixed: use plot() instead of show()
        
        # Save annotated image
        output_path = os.path.join(save_dir, f"result_{i}.jpg")
        annotated_frame = result.plot()  # returns image with boxes drawn
        cv2.imwrite(output_path, annotated_frame)
        
        # Print detected boxes
        boxes = result.boxes
        if boxes is not None and len(boxes) > 0:
            print(f"Detected {len(boxes)} license plate(s):")
            for j, box in enumerate(boxes):
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                conf = box.conf[0].item()
                print(f" {j+1}. Box: [{x1:.1f}, {y1:.1f}, {x2:.1f}, {y2:.1f}], Confidence: {conf:.2f}")
        else:
            print("No license plates detected.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ALPR Inference Pipeline")
    parser.add_argument("--model", type=str, default="../models/alpr_yolov8n_640.pt", help="Path to YOLOv8 model weights")
    parser.add_argument("--image", type=str, required=True, help="Path to input image")
    parser.add_argument("--output", type=str, default="output", help="Directory to save output images")
    args = parser.parse_args()

    run_inference(args.model, args.image, args.output)
