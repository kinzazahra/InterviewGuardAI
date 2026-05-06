from flask import Flask, render_template, Response, jsonify, request
import cv2
import mediapipe as mp
import time

app = Flask(__name__)

camera = cv2.VideoCapture(0)

mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection()

suspicion_score = 100
events = []

tab_switch_count = 0

def generate_frames():
    global suspicion_score

    while True:
        success, frame = camera.read()

        if not success:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb)

        face_count = 0

        if results.detections:
            face_count = len(results.detections)

            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box

                h, w, c = frame.shape

                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                bw = int(bbox.width * w)
                bh = int(bbox.height * h)

                cv2.rectangle(frame, (x, y), (x+bw, y+bh), (0,255,0), 2)

        # No Face
        if face_count == 0:
            cv2.putText(frame, "NO FACE DETECTED", (20,40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

            suspicion_score -= 1
            events.append("No face detected")

        # Multiple Faces
        if face_count > 1:
            cv2.putText(frame, "MULTIPLE FACES DETECTED", (20,80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

            suspicion_score -= 2
            events.append("Multiple faces detected")

        suspicion_score = max(suspicion_score, 0)

        cv2.putText(frame, f"Trust Score: {suspicion_score}",
                    (20,120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255,0,0),
                    3)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/tab_switch', methods=['POST'])
def tab_switch():
    global suspicion_score, tab_switch_count

    tab_switch_count += 1
    suspicion_score -= 5

    events.append("Tab switched")

    return jsonify({
        "message": "Tab switch detected"
    })


@app.route('/report')
def report():

    if suspicion_score >= 80:
        status = "Normal"
    elif suspicion_score >= 50:
        status = "Suspicious"
    else:
        status = "High Risk"

    return render_template(
        'report.html',
        score=suspicion_score,
        status=status,
        events=events,
        tab_switches=tab_switch_count
    )


if __name__ == "__main__":
    app.run(debug=True)