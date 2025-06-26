import cv2
import numpy as np
from ultralytics import YOLO

# Initialize YOLO model
model = YOLO('/content/runs/detect/train2/weights/best.pt')

# Video paths
input_video = '/content/WhatsApp Video 2025-06-26 at 20.28.23_d69ee3e3.mp4'
output_video = '/content/final_output.mp4'

# Open video capture
cap = cv2.VideoCapture(input_video)
if not cap.isOpened():
    print("Error: Unable to open video.")
    exit()

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Optical flow parameters
lk_params = dict(winSize=(25, 25),
                maxLevel=2,
                criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Tracking variables
prev_gray = None
prev_ball_pos = None
prev_ball_radius = None
track_points = None

# Processing loop
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    current_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Run YOLO detection every frame
    results = model(frame, conf=0.6)
    
    # Reset tracking if we get a new detection
    if results[0].boxes is not None and len(results[0].boxes) > 0:
        boxes = results[0].boxes.xyxy.cpu().numpy()
        confidences = results[0].boxes.conf.cpu().numpy()
        labels = results[0].boxes.cls.cpu().numpy()
        
        # Find best ball detection
        best_idx = None
        for i, label in enumerate(labels):
            if label == 0:  # Class 0 is ball
                if best_idx is None or confidences[i] > confidences[best_idx]:
                    best_idx = i
        
        if best_idx is not None:
            x1, y1, x2, y2 = boxes[best_idx]
            center = ((x1 + x2)/2, (y1 + y2)/2)
            radius = (x2 - x1)/2
            
            # Update tracking points
            prev_ball_pos = center
            prev_ball_radius = radius
            track_points = np.array([[center]], dtype=np.float32)
            prev_gray = current_gray.copy()
            
            # Draw green detection box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f'Detected {confidences[best_idx]:.2f}', 
                        (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Use optical flow only when YOLO fails but we have previous position
    elif prev_ball_pos is not None and prev_gray is not None:
        # Calculate optical flow
        new_points, status, _ = cv2.calcOpticalFlowPyrLK(
            prev_gray, current_gray, track_points, None, **lk_params)
        
        # If tracking succeeded
        if status[0][0] == 1:
            new_pos = new_points[0][0]
            track_points = new_points
            
            # Draw green tracking box (same style as detection)
            x1 = int(new_pos[0] - prev_ball_radius)
            y1 = int(new_pos[1] - prev_ball_radius)
            x2 = int(new_pos[0] + prev_ball_radius)
            y2 = int(new_pos[1] + prev_ball_radius)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, 'Tracking', (x1, y1-10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Update for next frame
            prev_ball_pos = (new_pos[0], new_pos[1])
    
    # Update previous frame for optical flow
    prev_gray = current_gray.copy()
    
    # Write frame to output
    out.write(frame)

# Release resources
cap.release()
out.release()

print(f"Processing complete. Output saved to {output_video}")