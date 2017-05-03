from flask import Flask, Response, render_template
import cv2

cam = cv2.VideoCapture(0)
app = Flask(__name__)

def stream():
    while True:
        ret, frame = cam.read()
        dingen = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, jpg = cv2.imencode('.jpg', dingen)
        jpg_bytes = jpg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
