# Dataset

This project uses the **Automatic License Plate Recognition (ALPR) Dataset**
provided on Kaggle.

🔗 **Dataset link:**  
https://www.kaggle.com/datasets/mgmitesh/automatic-license-plate-recognition-alpr-dataset

---

## Dataset Description

The dataset contains vehicle images with annotated **license plate bounding boxes**
and is suitable for object detection tasks.

It is organized in **YOLO format** and split into:
- Training set
- Validation set
- Test set

Each image has a corresponding `.txt` label file containing:
<class_id> <x_center> <y_center> <width> <height>

(all values are normalized).

---

## Dataset Structure

After downloading and extracting the dataset, the local structure should be:

```
Data/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
└── test/          
    ├── images/
    └── labels/
```
## Notes
- The dataset is not included in this repository to keep it lightweight.
- Please download the dataset manually from Kaggle using the link above.
- Ensure the folder structure matches the expected format before training.

## License & Credits
All dataset rights and credits belong to the original author on Kaggle.
