# 🧠 Week 02 – Python Environment & Object Detection

## 📌 Overview

Week 02 focuses on setting up a controlled Python environment and implementing object detection using a pretrained YOLO model from Ultralytics.

---

## ✅ Task 01: Virtual Environment Setup

### 🔍 Objective

To create an isolated Python environment for dependency management.

### ⚙️ Steps

```bash
python -m venv myenv
myenv\Scripts\activate
```

### 🧠 Learning

* Importance of dependency isolation
* Avoiding version conflicts
* Managing project-specific environments

---

## ✅ Task 02: Installing Ultralytics

### 🔍 Objective

To install and configure the Ultralytics package for object detection.

### ⚙️ Command

```bash
pip install -U ultralytics
```

### 🧠 Learning

* Package management using pip
* Installing ML frameworks locally
* Preparing environment for model execution

---

## ✅ Task 03: Object Detection using YOLO

### 🔍 Objective

To perform object detection using a pretrained YOLO model.

### ⚙️ Code

```python
from ultralytics import YOLO

# Load pretrained model
model = YOLO("yolov8n.pt")

# Run detection
results = model("image.jpg", show=True)
```

### 📸 Output

* Detected objects are displayed with bounding boxes
* Output image saved automatically

---

## 🧠 Learning Outcomes

* Understanding of object detection workflow
* Basics of pretrained deep learning models
* Real-time inference using YOLO

---

## 📁 Folder Structure

```
Week-02/
│
├── venv-setup/
├── ultralytics-installation/
├── yolo-output/
└── README.md
```

---

## 🚀 Summary

This week introduced foundational concepts in machine learning workflows, including environment setup and applying pretrained models for object detection tasks.
