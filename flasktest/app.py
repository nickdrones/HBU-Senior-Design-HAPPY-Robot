#######################################################
## Run this code using following command:
##     flask run --host=172.17.21.145
#######################################################
import random
import re
import sys
from flask import Flask, render_template, redirect, url_for, request, session, flash
from turbo_flask import Turbo
import threading
import time
from functools import wraps

app = Flask(__name__)
turbo = Turbo(app)


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
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
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

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    #app.run(debug=True, port=8080, host="172.17.21.145")