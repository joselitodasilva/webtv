from flask import Flask, render_template, Response	
from camera import Camera
from time import sleep


app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
        	b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def gen2(camera):
	for n in range(0,250):
		sleep(0.041)
		print "CU" + str(n)
		frame = camera.get_all_frames(n)
		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') 

def stream(camera):
	for frame in camera.get_all_frames:
		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#ROUTES
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
	return Response(gen2(Camera()),
			mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0')