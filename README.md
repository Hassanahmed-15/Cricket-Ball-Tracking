# 🏏 Cricket Ball Tracking System

This project tracks a **cricket ball** in real-time during a match using computer vision techniques. The system first detects the ball using **YOLOv8** and then tracks its movement using **Optical Flow** to predict its trajectory.

## Approach

### 1. **Object Detection with YOLOv8**

The first step involved training the **YOLOv8** model on a custom dataset of cricket ball images. YOLOv8 is a powerful and efficient object detection model, which makes it ideal for real-time applications like this one.

For training, I used the **Cricket Ball Dataset for YOLO**, available on **Kaggle**. The dataset was split into **training** and **validation** sets, and I used YOLOv8 to train the model to recognize the cricket ball. Here's the **`data.yaml`** file that I used to configure the dataset paths:

```yaml
train: /kaggle/input/cricket-ball-dataset-for-yolo/cricket_ball_data/train  # Path to training images
val: /kaggle/input/cricket-ball-dataset-for-yolo/cricket_ball_data/valid     # Path to validation images
nc: 1                                 # Number of classes (1 for cricket ball)
names:
  0: cricketBall                     # Name of class 0 is 'cricketBall'
The above configuration file specifies:

train: The location of the training images.

val: The location of the validation images.

nc: Number of classes (1, as we're detecting only the cricket ball).

names: The name of the class (in this case, cricketBall).

2. Tracking with Optical Flow
Once the cricket ball is detected in each frame by YOLOv8, the next step is to track its movement across frames. For this, I used Optical Flow.

Optical Flow is a technique in computer vision that tracks the motion of objects by analyzing the movement of pixels between consecutive frames. It works by estimating how each pixel has moved from one frame to the next. This allows the system to predict the ball's path even when it moves quickly or changes direction.

The ball’s movement is tracked frame-by-frame, and the Optical Flow technique helps predict its trajectory over time.

3. Final Output
The system then visualizes the ball’s trajectory on the video, showing how the ball moves over time. This visualization provides a clear representation of the ball's movement path throughout the match, offering valuable insights into its speed and direction.

4. Video Demo
Here’s the demo video where you can see the system in action:

Cricket Ball Tracking Video

In this video:

YOLOv8 detects the cricket ball in each frame.

Optical Flow tracks its motion and predicts its path.

The ball's trajectory is visualized in real-time.

Conclusion
This project demonstrates how YOLOv8 and Optical Flow can be combined to track a cricket ball in real-time, predicting its trajectory and visualizing its movement during the match. The system has potential applications in sports analytics, helping to analyze the ball's path, speed, and movement during a game
