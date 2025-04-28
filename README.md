# FINAL-PLP-PROJECT
🚦 AI Traffic Monitoring System
This project is a real-time traffic monitoring system that uses AI models and computer vision to detect vehicles in different lanes, update vehicle counts, and recommend actions based on traffic density. It also provides a live traffic video feed and a dashboard that updates automatically every second.
________________________________________
📋 Project Overview
This project uses:
•	A Flask server to stream live video and serve traffic data.
•	YOLO-based object detection (or your preferred model) to detect vehicles.
•	JavaScript (Fetch API) to dynamically update the web dashboard every few seconds.
•	HTML/CSS frontend for live traffic visualization and recommendations.
________________________________________
🛠️ Features
•	📹 Live video stream from the traffic camera.
•	🚗 Real-time vehicle count per lane (Lane 1 and Lane 2).
•	🟢🔴 Traffic signal simulation (Green/Red status for lanes).
•	📈 Traffic recommendations to optimize lane usage.

________________________________________
📋 Project Structure
/Final-PLP-Project
│── /static
│   ├── css/styles.css
│   ├── js/script.js
│── /templates
│   ├── index.html
│── /videos
│   ├── output_video.mp4
│── model.py   # Your Flask app (previously app.py)
└── README.md          # This file
________________________________________
🚀 How It Works
•	A camera feed (real or simulated) is analyzed using an AI model to detect vehicles.
•	The number of vehicles in each lane is counted.
•	Every second, the frontend dashboard polls the backend at /traffic_data and updates the car counts.
•	The traffic signal status (e.g., Green, Red, Yellow) is updated based on traffic conditions.
•	A recommendation is generated based on live traffic analysis.
•	The live video feed is streamed via Flask using /video_feed.
________________________________________
🛠️ Installation and Setup
1.	Clone the repository:
2.	git clone https://github.com/your-username/ai-traffic-monitoring.git
3.	cd ai-traffic-monitoring
4.	Set up a virtual environment (optional but recommended):
5.	python -m venv venv
6.	source venv/bin/activate  # For Linux/Mac
7.	venv\Scripts\activate     # For Windows
8.	Install the required dependencies:
9.	pip install -r requirements.txt
10.	Run the Flask server:
11.	python app.py
12.	Access the dashboard: Open your browser and go to:
http://127.0.0.1:5000/
________________________________________
⚙️ Requirements
Make sure you have the following Python packages installed:
•	Flask
•	OpenCV (opencv-python)
•	TensorFlow or PyTorch (depending on your model)
•	NumPy
You can install them manually or create a requirements.txt file like:
Flask
opencv-python
numpy
tensorflow   # or torch
________________________________________
📈 Results
•	Detected and counted vehicles in Lane 1 and Lane 2.
•	Real-time dashboard updates.
•	Live camera feed embedded in the dashboard.
•	Fully functioning and aesthetic dashboard
•	Traffic signals that change based on traffic data.
•	Recommendations update based on real-time traffic status.
________________________________________
🧠 My Approach
•	Flask was used for the backend server to serve the video and traffic data.
•	JavaScript (Fetch API + setInterval) was used to request /traffic_data every second.
•	OpenCV handled video capture and frame processing.
•	The AI model detected and classified objects (vehicles) in each video frame.
•	Lane segmentation was done manually by defining ROIs (regions of interest).
•	A simple thresholding strategy was used to decide signal status based on car count.
________________________________________
⚙️ Notes
•	Model.py should contain your object detection model and a generate_frames() function that:
o	Captures video.
o	Detects vehicles.
o	Sends frames for live streaming.
•	The traffic_data API endpoint sends updated car counts and signal status every few seconds.
•	Customize how you assign lanes, e.g., based on image regions (left for Lane 1, right for Lane 2).

Thanks for checking it out! 🚦🚗🛣️
________________________________________
________________________________________

