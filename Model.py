import cv2
import torch
import numpy as np
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")  # Uses YOLOv8 for object detection

# Define lanes (customize these based on your video)
lane1_region = (100, 300, 400, 500)  # (x1, y1, x2, y2)
lane2_region = (450, 300, 750, 500)

# Function to process video frames
def generate_frames():
    cap = cv2.VideoCapture("videos/output video.mp4")  # Video file

    if not cap.isOpened():
        print("Error opening video file")
        return

    global lane_1_count, lane_2_count, light_status

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO inference
        results = model(frame)
        lane_1_count = 0
        lane_2_count = 0

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box coordinates
                conf = box.conf[0].item()  # Confidence score
                cls = int(box.cls[0].item())  # Class ID

                if cls == 2 and conf > 0.6:  # Class 2 is "car"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    # Check lane position
                    if lane1_region[0] < x1 < lane1_region[2] and lane1_region[1] < y1 < lane1_region[3]:
                        lane_1_count += 1
                    elif lane2_region[0] < x1 < lane2_region[2] and lane2_region[1] < y1 < lane2_region[3]:
                        lane_2_count += 1

        # Traffic light logic
        if lane_1_count > lane_2_count:
            light_status = "Lane 1: Green | Lane 2: Red"
            signal_color = (0, 255, 0)
        else:
            light_status = "Lane 1: Red | Lane 2: Green"
            signal_color = (0, 0, 255)

        # Display information
        cv2.putText(frame, f"Lane 1 Cars: {lane_1_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, f"Lane 2 Cars: {lane_2_count}", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, f"Signal: {light_status}", (50, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, signal_color, 2)

        # Encode frame as JPEG for streaming
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    cap.release()
