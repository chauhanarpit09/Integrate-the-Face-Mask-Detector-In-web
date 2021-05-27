from flask import *
import cv2
import time
from predict import *
import dlib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

d = predict()

app = Flask(__name__)
app.config['SECRET_KEY'] = '959121b6ce54245c32bb1c09fae3cf16'
label = ""
@app.route("/")
@app.route("/home")
def home():
	return render_template('index.html',label = label)

def gen():
	cap = cv2.VideoCapture(0)
	while(cap.isOpened()):
		ret , img = cap.read()
		if ret == True:
			(l,p) = d.predict(img)
			img = d.draw(l,p,img)
			frame = cv2.imencode('.jpg',img)[1].tobytes()
			yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n'+ frame + b'\r\n')
			time.sleep(0.1)
		else:
			break
	
@app.route('/video_feedback')
def video_feed():
	return Response( gen() ,
					mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
	app.run(debug = True)