# Automatic License Plate Recognition (ALPR) – YOLOv8

This project implements a **high-accuracy, real-time license plate detection system** using **YOLOv8n**.  
The system is designed for practical applications such as **traffic monitoring, parking automation, and surveillance**, focusing on **robust detection, high precision, and fast inference**.

---

## Project Description

The goal of this project is to accurately detect vehicle license plates in diverse real-world scenarios, including varying lighting conditions, angles, and backgrounds with high precision 
while maintaining fast inference speed suitable for real-world systems such as traffic monitoring, parking automation, and surveillance.

The model is trained as a **single-class object detector (`license_plate`)** using a large-scale annotated dataset. 
The workflow includes **model training, evaluation, and real-time inference**

---

## Dataset

- **Dataset:** Automatic License Plate Recognition (ALPR)  
- **Source:** [Kaggle](https://www.kaggle.com/datasets/mgmitesh/automatic-license-plate-recognition-alpr-dataset)  
- **Size:**  
  - ~21,000 training images  
  - ~2,000 validation images  
- **Note:** Dataset is **not included** in this repository (see `Data/README.md`).

---

## Model & Training

- **Architecture:** YOLOv8n (Nano)  
- **Framework:** Ultralytics YOLOv8  
- **Task:** Single-class object detection  
- **Image size:** 640 × 640  
- **Batch size:** 16  
- **Optimizer:** AdamW (auto-selected)  
- **Training hardware:**  
  - Local: NVIDIA GTX 1050 Ti (4GB)  
  - Cloud: Tesla T4 (Google Colab)

---

## Results (Validation)

**Final model performance on validation set:**

| Metric         | Result |
|----------------|--------|
| Precision      | **98.3%** |
| Recall         | **95.2%** |
| F1-score       | **96.6%** |
| mAP@0.50       | **98.4%** |
| mAP@0.50:0.95  | **69.9%** |
| Inference speed| **~3.5 ms/image (Tesla T4)**  /  **~8.7 ms/image (GTX 1050 Ti)**|


**Highlights:**

- Extremely low false positives (high precision)  
- Strong detection coverage (high recall)  
- Accurate localization across IoU thresholds  
- Real-time inference on both high-end and consumer GPUs  

---

