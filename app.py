from flask import Flask,render_template,Response
from main import detect
import cv2 as cv

app = Flask(__name__)
camera=cv.VideoCapture(0)

def generate_frames():
    while True:
        retn,frame=camera.read()
        if not retn:
            break
        else:
            frame=detect(frame)
            ret,buffer =cv.imencode('.jpg',frame)
            frame=buffer.tobytes()
            
        yield(b'--frame\r\r'
                   b'Content-Type: image/jpeg\r\n\r\n'+frame +b'\r\n')
        
            

@app.route('/')
def index():
    return (render_template('index.html'))

@app.route('/video')
def video_function():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

    
    
if __name__=='__main__':
    app.run(debug=True)