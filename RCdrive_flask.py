import drive_system
import sensors
import time
import statusled
import signal
from threading import Thread
import random
import re
import sys
from flask import Flask, render_template, redirect, url_for, request, session, flash, Response
from turbo_flask import Turbo
import threading
import time
from functools import wraps
import hashlib
from socket import *
import pandas as pd
import math 
import cv2
import signal
import _thread


start_time = time.time()



############################################################
# Keyboard Interrupt Handler, allows for graceful shutdown #
############################################################
def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    #ALL CODE TO RUN WHILE STOPPING ROBOT GOES HERE
    exit(0)
signal.signal(signal.SIGINT, keyboardInterruptHandler)



print("         ██╗  ██╗██████╗ ██╗   ██╗    █  ██████╗ ██████╗ ")
print("         ██║  ██║██╔══██╗██║   ██║            ██╗╚════██╗")
print("         ███████║██████╔╝██║   ██║        █████╔╝ █████╔╝")
print("         ██╔══██║██╔══██╗██║   ██║      ██╔═══╝ ██╔═══╝ ")
print("         ██║  ██║██████╔╝╚██████╔╝      ███████╗███████╗")
print("         ╚═╝  ╚═╝╚═════╝  ╚═════╝       ╚══════╝╚══════╝")
print("")

print("             _______   _______ ______   _____ __ ________          ")
print("            / ____/ | / / ___// ____/  <  / // /<  /__  /          ")
print("           / __/ /  |/ /\__ \/ /       / / // /_/ / /_ <           ")
print("          / /___/ /|  /___/ / /___    / /__  __/ /___/ /           ")
print("         /_____/_/ |_//____/\____/   /_/  /_/ /_//____/            ")
print("   _____                            ____                           ")
print("  / ___/___  ____  (_)___  _____   / __ \___  _____(_)___ _____    ")
print("  \__ \/ _ \/ __ \/ / __ \/ ___/  / / / / _ \/ ___/ / __ `/ __ \   ")
print(" ___/ /  __/ / / / / /_/ / /     / /_/ /  __(__  ) / /_/ / / / /   ")
print("/____/\___/_/ /_/_/\____/_/     /_____/\___/____/_/\__, /_/ /_/    ")
print("    __  __        ___            ____          ___/____/     __  __")
print("   / / / /       /   |          / __ \        / __ \         \ \/ /")
print("  / /_/ /       / /| |         / /_/ /       / /_/ /          \  / ")
print(" / __  /  _    / ___ |   _    / ____/  _    / ____/  _        / /  ")
print("/_/ /_/  (_)  /_/  |_|  (_)  /_/      (_)  /_/      (_)      /_/   ")
print("")
print("")

time.sleep(2)
print("###############################################")
print("Initializing Robot")
print("###############################################")
print("")

time.sleep(1)

print("Establishing Communication with LED bar to display status")
try:
    HAL = statusled.ledbar()
except:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("ERROR!!!")
    print("LED Bar not connected, continuing...")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("Connection Established at default I2C address")
print("")

HAL.showSuccessfulDeviceInit()

time.sleep(1)

print("Establishing Communication with Analog to Digital Converter")
try:
    Tyndale = sensors.analog2digital()
except:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("ERROR!!!")
    print("ADC not connected, continuing...")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("Connection Established at default I2C address")

print("")

HAL.YellowCreepTo(5)

time.sleep(1)

print("Establishing Communication with PCA9685 over I2C")
try:
    Hermes = drive_system.Chassis()
except:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("ERROR!!!")
    print("PCA9685 not connected, continuing...")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("Connection with PCA9685 Established at default I2C address")
print("")

HAL.YellowCreepTo(10)

time.sleep(1)

print("Establishing Communication with GPS module over Serial")
print("Pausing for 5 seconds to allow sensor to connect to satellites")
try:
    Navi = sensors.GPS_sensor()
    time.sleep(5)
except:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("ERROR!!!")
    print("GPS Board not connected via serial, continuing...")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("Serial communication established at COM port /dev/ttyACM0")
print("")

HAL.YellowCreepTo(15)

time.sleep(1)

print("Initializing Camera")
video =  cv2.VideoCapture("nvarguscamerasrc ! nvvidconv ! video/x-raw, width=(int)1280, height=(int)720, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink", cv2.CAP_GSTREAMER)
print("Camera Loaded Successfully")
print("")


HAL.YellowCreepTo(20)

time.sleep(1)

print("Establishing Communication with magnetometer over I2C")
try:
    Mando = sensors.magnetometer()
    time.sleep(5)
except:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("ERROR!!!")
    print("Magnetometer not connected, continuing...")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("Connection with magnetometer Established at default I2C address")
print("")

HAL.YellowCreepTo(24)

time.sleep(1)

print("Initialization Complete")
print("")
print("██████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗")
print("██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝")
print("██████╔╝█████╗  ███████║██║  ██║ ╚████╔╝ ")
print("██╔══██╗██╔══╝  ██╔══██║██║  ██║  ╚██╔╝  ")
print("██║  ██║███████╗██║  ██║██████╔╝   ██║   ")
print("╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝   ")
print("")

###################################################################################################

HAL.showSuccessfulRobotInit()

time.sleep(2)

#HAL.KITT()

#while(1==1):
#    combocoords = Navi.getComboCoords()
#    print(combocoords)
#    time.sleep(2)
#    Sauron.processFrame()


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
    fieldnames = ['destinationCode', 'normalName','destcoords1','destcoords2']
    #coords to test
    coords2 = int(Navi.getLastLattitude())
    coords1 = int(Navi.getLastLongitude())
    coord1vals = []
    coord2vals = []
    lengths = []
    for x in A.values:
        coord1vals.append(int(x[int(fieldnames.index("destcoords1"))]))
        coord2vals.append(int(x[int(fieldnames.index("destcoords2"))]))
    for i in range(len(coord1vals)):
        lengths.append(math.sqrt(math.pow(((int(coord1vals[i]))-(coords1)),2) + math.pow(((int(coord2vals[i]))-(coords2)),2)))
    lengthsToSort = []
    for i in lengths:
        lengthsToSort.append(i)
    lengthsToSort.sort()
    #print(A.values[lengths.index(lengthsToSort[0])][int(fieldnames.index("normalName"))])
    headingtoreturn = Mando.getHeading()
    gpsToReturn = str(Navi.getLastLongitude()) + " , " + str(Navi.getLastLattitude())
    voltagetoreturn = Tyndale.getBatteryVoltage()
    jobStatusAvail = ["Idle", "On Job", "Error", "Waiting for Dropoff", "Waiting for Pickup", "Loading", "Unloading"]
    currentjobstatus = jobStatusAvail[0]
    start_time = time.time()
    timesincelastservercontact = int(int(time.time()-start_time)/60)
    nearestdestinationtome = A.values[lengths.index(lengthsToSort[0])][int(fieldnames.index("normalName"))]
    distancetonearestdestinationtome = int(lengthsToSort[0])
    return {'returnedHeading': headingtoreturn,'returnedGPS': gpsToReturn,'returnedVolt': voltagetoreturn, 'returnedstatus':currentjobstatus, 'lastcontacted':timesincelastservercontact,'returnednearestdestination':nearestdestinationtome,'distancetonearestdestination':distancetonearestdestinationtome}



def update_load():
    with app.app_context():
        while True:
            time.sleep(1)
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


#if __name__ == "__main__":
A = pd.read_csv('destinations.csv')
_thread.start_new_thread(HAL.KITT)
app.run(debug=False, port=8080, host="172.17.21.145")



#quit()