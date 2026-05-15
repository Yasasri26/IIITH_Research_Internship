\# Week 4 - YOLO Dataset Preparation and Labeling



\## Objective



Understand YOLO dataset structure and create a custom labeled dataset for object detection training using Label Studio and YOLO format annotations.



\---



\# Task 1 - Study of YOLO Dataset Structure



\## Topics Studied



\* YOLO dataset folder structure

\* YAML configuration files

\* YOLO annotation format

\* Normalized bounding box coordinates

\* Metadata files used in YOLO datasets



\## YOLO Dataset Structure



```text

dataset/

├── images/

│   ├── train/

│   ├── val/

│   └── test/

│

├── labels/

│   ├── train/

│   ├── val/

│   └── test/

│

└── data.yaml

```



\---



\# Explanation of Dataset Folders



\## images/train



Contains images used for training the model.



\## images/val



Contains validation images used to evaluate the model during training.



\## images/test



Contains testing images used after training for final evaluation.



\## labels/train



Contains annotation text files corresponding to training images.



\## labels/val



Contains annotation text files corresponding to validation images.



\## labels/test



Contains annotation text files corresponding to testing images.



\---



\# YOLO Label File Format



Example annotation:



```text

0 0.512 0.433 0.201 0.178

```



\## Meaning of Values



| Value | Description            |

| ----- | ---------------------- |

| 0     | Class ID               |

| 0.512 | Center X coordinate    |

| 0.433 | Center Y coordinate    |

| 0.201 | Width of bounding box  |

| 0.178 | Height of bounding box |



All coordinates are normalized between 0 and 1.



\---



\# Task 2 - Dataset Creation and Labeling



\## Tasks Performed



\* Selected a traffic video dataset

\* Extracted frames using FFmpeg

\* Created train, validation, and test folders

\* Installed Label Studio

\* Annotated objects manually

\* Exported YOLO formatted labels

\* Created YAML configuration file



\---



\# Tools Used



\* Python

\* FFmpeg

\* Label Studio

\* YOLO / Ultralytics



\---



\# Classes Used



| Class ID | Object  |

| -------- | ------- |

| 0        | Person  |

| 1        | Bicycle |

| 2        | Car     |



\---



\# data.yaml Configuration



```yaml

path: dataset



train: images/train

val: images/val

test: images/test



names:

&#x20; 0: person

&#x20; 1: bicycle

&#x20; 2: car

```



\---



\# Annotation Process



The dataset images were annotated using Label Studio by drawing bounding boxes around:



\* persons

\* bicycles

\* cars



Each image generated a corresponding YOLO label text file.



\---



\# Outputs Generated



\* Extracted video frames

\* Annotated images

\* YOLO label files

\* YAML configuration file

\* Dataset report

\* Label Studio screenshots



\---



\# Folder Structure



```text

week4/

├── dataset/

│   ├── images/

│   ├── labels/

│   └── data.yaml

│

├── report/

├── screenshots/

└── README.md

```



\---



\# Observations



\* Proper dataset organization is essential for YOLO training.

\* Accurate labeling improves model performance.

\* YAML configuration files define dataset paths and class names.

\* Normalized coordinates help YOLO generalize across image sizes.



\---



\# Conclusion



A custom YOLO dataset was successfully created and annotated using Label Studio. The dataset was organized into YOLO-compatible format with training, validation, and testing sets. This dataset is now ready for custom YOLO model training in Week 5.



\---



\# References



1\. https://docs.ultralytics.com/

2\. https://labelstud.io/

3\. https://github.com/ultralytics/ultralytics

4\. https://www.ultralytics.com/

5\. https://docs.ultralytics.com/datasets/detect/



```

```



