# 🏏 Cricket Ball Tracking System

This project tracks a **cricket ball in real-time** during a match using advanced computer vision techniques.  
It detects the ball using **YOLOv8** and then uses **Optical Flow** to track and predict its trajectory.

---

## 🚀 Approach

### **1. Object Detection with YOLOv8**
The first step involves training the **YOLOv8** model on a custom dataset of cricket ball images.  
YOLOv8 is known for its high speed and accuracy, making it perfect for real-time detection tasks.

- I trained YOLOv8 on the **Cricket Ball Dataset for YOLO** (available on **Kaggle**).  
- The dataset was split into **training** and **validation** sets.  
- YOLOv8 was configured to detect just **one class**: the cricket ball.

Here’s the `data.yaml` I used:

```yaml
train: /kaggle/input/cricket-ball-dataset-for-yolo/cricket_ball_data/train  # Path to training images
val: /kaggle/input/cricket-ball-dataset-for-yolo/cricket_ball_data/valid    # Path to validation images
nc: 1                                                                      # Number of classes (1 for cricket ball)
names:
  0: cricketBall                                                           # Name of class 0 is 'cricketBall'
```

This configuration file specifies:
- **train:** Path to training images.  
- **val:** Path to validation images.  
- **nc:** Number of classes (1, since we only detect the cricket ball).  
- **names:** The class name (`cricketBall`).

---

### **2. Tracking with Optical Flow**
Once YOLOv8 detects the cricket ball in each video frame, the next step is **tracking**.

- I implemented **Optical Flow**, a classic technique in computer vision, to track the motion of the ball between consecutive frames.  
- Optical Flow estimates how each pixel moves from one frame to the next, allowing accurate motion tracking.  
- This approach helps to **predict the trajectory** even when the ball is moving fast or changing direction.

---

### **3. Visualizing the Final Output**
The system visualizes the cricket ball’s trajectory on the video in **real-time**:
- YOLOv8 detects the ball in each frame.
- Optical Flow continuously tracks its movement.
- A **trajectory line** is drawn to show the ball’s path, speed, and direction over time.

---

### **4. Video Demo**
Here’s a demo of the system in action:

**Cricket Ball Tracking Video:**
- YOLOv8 detects the ball in each frame.  
- Optical Flow tracks the motion frame-by-frame.  
- The ball’s trajectory is visualized live on the video.

---

## 🎯 Conclusion
This project combines the power of **YOLOv8** and **Optical Flow** to track and analyze a cricket ball in real-time.  
It can predict the trajectory and visualize the movement, making it a **valuable tool for sports analytics**.  
With further enhancements, this can be used to analyze metrics like **speed, spin, and path prediction** during matches.

---

## 🛠️ Tech Stack
- **YOLOv8** for object detection  
- **Optical Flow** for motion tracking  
- **OpenCV** for video processing  
- **Python** as the primary programming language  

---
