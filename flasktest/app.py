#######################################################
## Run this code using following command:
##     flask run --host=172.17.21.145
#######################################################
import random
import re
import sys
from flask import Flask, render_template
from turbo_flask import Turbo
import threading
import time

app = Flask(__name__)
turbo = Turbo(app)


@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

@app.route('/')
def index():
    return render_template('index.html')


@app.context_processor
def inject_heading():
    headingtoreturn = int(random.random() * 100) / 100
    gpsToReturn = str(int(random.random() * 10000)) + "," + str(int(random.random() * 10000))
    return {'returnedHeading': headingtoreturn,'returnedGPS': gpsToReturn}


def update_load():
    with app.app_context():
        while True:
            time.sleep(0.2)
            turbo.push(turbo.replace(render_template('magnet.html'), 'magnet'))
            turbo.push(turbo.replace(render_template('gps.html'), 'gps'))