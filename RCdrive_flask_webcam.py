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
import cv2
from socket import *



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
video = cv2.VideoCapture(0)
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

@app.context_processor
def inject_data():
    headingtoreturn = Mando.getHeading()
    gpsToReturn = str(Navi.getLastLongitude()) + " , " + str(Navi.getLastLattitude())
    voltagetoreturn = Tyndale.getBatteryVoltage()
    jobStatusAvail = ["Idle", "On Job", "Error", "Waiting for Dropoff", "Waiting for Pickup", "Loading", "Unloading"]
    currentjobstatus = jobStatusAvail[0]
    timesincelastservercontact = 3
    possibleDestinations = ["Atwood II", "Atwood I", "MDA", "Sports Media Office","Sports Marketing","Glasscock/Maybee","Science Office", "COSE Office", "Library", "Nursing Office","Hodo","Hinton"]
    nearestdestinationtome = possibleDestinations[0]
    distancetonearestdestinationtome = 999
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
        frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        frame_gray = cv2.equalizeHist(frame_gray)

        ret, jpeg = cv2.imencode('.jpg', image)

        frame = jpeg.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=False, port=8080, host="172.17.21.145")

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-', 'xy_home']

HOST = ''           # The variable of HOST is null, so the function bind( ) can be bound to all valid addresses.
PORT = 21567
BUFSIZ = 1024       # Size of the buffer
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)    # Create a socket.
tcpSerSock.bind(ADDR)    # Bind the IP address and port number of the server. 
tcpSerSock.listen(5)     # The parameter of listen() defines the number of connections permitted at one time. Once the 
			 # connections are full, others will be rejected. 

while True:
	Hermes.stopAllMotors()
	print('Waiting for connection...')
	# Waiting for connection. Once receiving a connection, the function accept() returns a separate 
	# client socket for the subsequent communication. By default, the function accept() is a blocking 
	# one, which means it is suspended before the connection comes.
	tcpCliSock, addr = tcpSerSock.accept() 
	print('...connected from :', addr)     # Print the IP address of the client connected with the server.

	while True:
		data = ''
		data = tcpCliSock.recv(BUFSIZ).decode()    # Receive data sent from the client. 
		if not data:
			break
		if data == ctrl_cmd[0]:
			print('motor moving forward')
			Hermes.driveChassisLR(100,100)
		elif data == ctrl_cmd[1]:
			print('recv backward cmd')
			Hermes.driveChassisLR(-100,-100)
		elif data == ctrl_cmd[2]:
			print('recv left cmd')
			Hermes.driveChassisLR(-100,100)
		elif data == ctrl_cmd[3]:
			print('recv right cmd')
			Hermes.driveChassisLR(100,-100)
		elif data == ctrl_cmd[4]:
			print('recv stop cmd')
			Hermes.stopAllMotors()
		else:
			print('Command Error! Cannot recognize command: ' + str(data))



#quit()