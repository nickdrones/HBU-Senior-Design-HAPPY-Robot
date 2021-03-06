#######################################################
## Run this code using following command:
##     flask run --host=172.17.21.145
#######################################################
import random
import re
import sys
from flask import Flask, render_template, redirect, url_for, request, session, flash, Response
from turbo_flask import Turbo
import threading
import time
from functools import wraps
import hashlib
import cv2
import signal

def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    #ALL CODE TO RUN WHILE STOPPING ROBOT GOES HERE
    exit(0)
signal.signal(signal.SIGINT, keyboardInterruptHandler)

video = cv2.VideoCapture(0)
#video =  cv2.VideoCapture("nvarguscamerasrc ! nvvidconv ! video/x-raw, width=(int)1280, height=(int)720, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink", cv2.CAP_GSTREAMER)

app = Flask(__name__)
turbo = Turbo(app)

authorizedUsers = ["nickb","briand","luisc","drakel"]
userPasswords = ["5f4dcc3b5aa765d61d8327deb882cf99","5f4dcc3b5aa765d61d8327deb882cf99","5f4dcc3b5aa765d61d8327deb882cf99","5f4dcc3b5aa765d61d8327deb882cf99"]
#all accounts use password "password"

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

app.secret_key = 'Iridocyclitis'

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/maptest')
def maptest():
    return render_template('maptest.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        indexofuser=-1
        for x in range(len(authorizedUsers)):
            if str(request.form['username']) == authorizedUsers[x]:
                indexofuser = x
        tempHashVal = hashlib.md5(request.form['password'].encode())
        hashedEnteredPassword = tempHashVal.hexdigest()
        if indexofuser < 0:
            error = 'Invalid Username. Please try again.'
        elif hashedEnteredPassword != userPasswords[x]:
            error = 'Invalid Password. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect("/")
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))

@app.route('/api/jobreceive', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print(json)
    else:
        return 'Content-Type not supported!'


@app.context_processor
def inject_data():
    headingtoreturn = int(random.random() * 360)
    gpsToReturn = str(int(random.random() * -100000000)) + " , " + str(int(random.random() * 100000000))
    voltagetoreturn = int(random.random() * 120)/10
    currentjobstatus = "Idle"
    timesincelastservercontact = 3
    nearestdestinationtome = "Atwood II"
    distancetonearestdestinationtome = 32
    return {'returnedHeading': headingtoreturn,'returnedGPS': gpsToReturn,'returnedVolt': voltagetoreturn, 'returnedstatus':currentjobstatus, 'lastcontacted':timesincelastservercontact,'returnednearestdestination':nearestdestinationtome,'distancetonearestdestination':distancetonearestdestinationtome}



def update_load():
    with app.app_context():
        while True:
            time.sleep(0.2)
            turbo.push(turbo.replace(render_template('magnet.html'), 'magnet'))
            turbo.push(turbo.replace(render_template('gps.html'), 'gps'))
            turbo.push(turbo.replace(render_template('voltagesensor.html'), 'voltage'))
            turbo.push(turbo.replace(render_template('onthejob.html'), 'onthejob'))
            turbo.push(turbo.replace(render_template('nearestdestination.html'), 'nearestdestination'))

def gen(video):
    while True:
        success, image = video.read()
        scale_percent = 30 # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
        frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.equalizeHist(frame_gray)

        ret, jpeg = cv2.imencode('.jpg', resized)

        frame = jpeg.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    #app.run(debug=True, port=8080)
    app.run(debug=False, port=8080, host="0.0.0.0")
    #app.run(debug=True, port=8080, host="172.17.21.145")