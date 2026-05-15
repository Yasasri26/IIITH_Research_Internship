Week 5 – Object Detection using YOLO (Custom Model)

&#x20;Project Overview



This project implements a custom object detection system using a YOLO-based deep learning model. The system is trained to detect multiple object categories such as person, bicycle, and car, and is evaluated using standard performance metrics and visual outputs.



The workflow includes model training, evaluation, and inference on images and videos.



&#x20;Objectives

Train a YOLO-based object detection model on a custom dataset

Detect multiple object classes in images and videos

Evaluate model performance using standard metrics

Visualize detection results for analysis

&#x20;Classes Detected

Person 

Bicycle 

Car 

&#x20;Model Details

Architecture: YOLO (You Only Look Once)

Framework: PyTorch / Ultralytics YOLO

Input Size: 640 × 640 (typical configuration)

Training Type: Supervised learning on labeled dataset

Output: Bounding boxes with class predictions and confidence scores

&#x20;Evaluation Metrics



The model performance is evaluated using:



Precision – Measures correctness of predictions

Recall – Measures ability to detect all objects

F1 Score – Balance between precision and recall

Confusion Matrix – Class-wise prediction performance

Precision-Recall Curve (PR Curve) – Tradeoff between precision and recall

Precision Curve (P Curve) – Precision behavior across thresholds

&#x20;Results



The trained model is analyzed using visual outputs such as:



Training performance graphs

Confusion matrix for classification accuracy

Precision-Recall curve for detection quality

F1-score curve for model balance analysis



These results help understand model effectiveness and limitations.



&#x20;Inference Outputs



The trained model is tested on both images and videos.



Final detection video showcasing real-time object detection

Processed video with bounding box overlays

Sample images with detected objects and confidence scores

&#x20;How to Run

Train the Model

python train.py

Test the Model

python test.py

Run Inference



Processed outputs will be saved in the detection results directory after execution.



&#x20;Dependencies

Python 3.8+

PyTorch

OpenCV

NumPy

Matplotlib

Ultralytics YOLO (if applicable)



Install dependencies using:



pip install -r requirements.txt

&#x20;Key Learnings

Understanding object detection using YOLO architecture

Working with bounding box predictions

Evaluating model performance using multiple metrics

Performing inference on real-world images and videos

Structuring a complete computer vision pipeline



Conclusion



This project demonstrates a complete object detection pipeline using YOLO, from training to evaluation and inference. The model successfully detects multiple object categories and provides meaningful visual insights through performance metrics and output videos.

