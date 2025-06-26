# 🏏 Cricket Ball Tracking System

This project tracks a **cricket ball** in real-time during a match using computer vision techniques. The system first detects the ball using **YOLOv8** and then tracks its movement using **Optical Flow** to predict its trajectory.

## Approach

### 1. **Object Detection with YOLOv8**

The first step involved training the **YOLOv8** model on a custom dataset of cricket ball images. The model was trained to detect the cricket ball in each video frame. Here's the **dataset path** used for training:

```yaml
train: /kaggle/input/cricket-ball-dataset-for-yolo/cricket_ball_data/train  # Path to training images
val: /kaggle/input/cricket-ball-dataset-for-yolo/cricket_ball_data/valid     # Path to validation images
nc: 1                                 # Number of classes (1 for cricket ball)
names:
  0: cricketBall                     # Name of class 0 is 'cricketBall'
2. Tracking with Optical Flow
Once the cricket ball is detected in each frame, Optical Flow is used to track the ball’s movement between frames. Optical Flow works by analyzing the motion of pixels in consecutive frames, estimating how each part of the image has moved. This allows the system to predict the ball's path, even if it moves quickly or changes direction.

3. Final Output
The system then visualizes the ball’s trajectory on the video, showing how the ball moves over time.

4. Video Demo
Here’s the demo video where you can see the system in action:

Cricket Ball Tracking Video

In this video:

YOLOv8 detects the cricket ball in each frame.

Optical Flow tracks its motion and predicts its path.

The ball's trajectory is visualized in real-time.

