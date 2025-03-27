from flask import Flask, render_template, Response, jsonify
from Model import generate_frames

app = Flask(__name__)

lane_1_count = 0
lane_2_count = 0
light_status = "Initializing..."

@app.route('/')
def home():
    """Render HTML dashboard"""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Stream processed video"""
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/traffic_data')
def traffic_data():
    """Return JSON data for frontend"""
    return jsonify({
        "lane_1_count": lane_1_count,
        "lane_2_count": lane_2_count,
        "signal_status": light_status
    })

if __name__ == '__main__':
    app.run(debug=True)
