Cricket Ball Tracking System
Project Overview
This project is focused on tracking a cricket ball in real-time during a match. I built a system that detects and tracks the ball using computer vision techniques. The main tools used for this project are the YOLOv8 object detection model and Optical Flow, which work together to detect and follow the ball’s movement across the video.

How I Did It
1. Detecting the Cricket Ball with YOLOv8
To start, I trained a YOLOv8 model on a custom dataset of cricket ball images. YOLOv8 is an efficient object detection model, designed to quickly find and identify objects in images. In this case, I used it to locate the cricket ball in each video frame.

For training, I used the Cricket Ball Dataset for YOLO, available on Kaggle. The dataset was split into training and validation sets. Here's the data.yaml file that I used to configure the dataset for training:
