# Husky Automated Package and Parcel deliverY (HAPPY)

We are a team of four seniors in the HBU Class of 2022 from the College of Science and Engineering. Our team is comprised of two Electrical Engineering majors, one Computer Science major, and one Cyber Engineering major.


## About this project

\<TO BE FILLED IN WITH DETAILS LATER>
Also the design document will be uploaded to this repository once the full release is complete at the end of the semester.


## Code Details
Computer Vision code based off samples found here: [https://github.com/dusty-nv/jetson-inference/](https://github.com/dusty-nv/jetson-inference/)

I2C and PCA9685 code based off documentation here: [https://www.jetsonhacks.com/2019/07/22/jetson-nano-using-i2c/](https://www.jetsonhacks.com/2019/07/22/jetson-nano-using-i2c/)

Magnetometer code working based off documentation here: [https://tutorials-raspberrypi.com/build-your-own-raspberry-pi-compass-hmc5883l/](https://tutorials-raspberrypi.com/build-your-own-raspberry-pi-compass-hmc5883l/)

Full documentation on Wayback Machine: [http://web.archive.org/web/20160503183933/http://think-bowl.com/raspberry-pi/i2c-python-library-3-axis-digital-compass-hmc5883l-with-the-raspberry-pi](http://web.archive.org/web/20160503183933/http://think-bowl.com/raspberry-pi/i2c-python-library-3-axis-digital-compass-hmc5883l-with-the-raspberry-pi)

Drive code is written in Python 3 and uses the adafruit_servokit library. Command to install the library is below:
> pip3 install adafruit-circuitpython-servokit

Serial communication utilizes pyserial which can be installed using the following command:
> sudo apt-get install python3-serial

MAIN.py is the main code, run in Python3. BEFORE RUNNING, confirm persmissions for serial are set to all by running the following command:
> sudo chmod 666 /dev/ttyTHS1
You cannot simply run the code as root because the i2ctools Python library is not recognized if the script is run as root

I2C devices connected can be listed by address by running the following command:
> i2cdetect -y -r 1

Web UI is python utilizing the Anvil framework which can be installed by running the following command:
> pip3 install anvil-app-server

We are creating the navigation algorithm by storing a list of waypoints and essentially using them as virtual "beacons" that the robot will drive between. The map of paths on campus with waypoints (W##) and destinations (D##) labeled.
![The Map](https://raw.githubusercontent.com/nickdrones/HBU-Senior-Design-HAPPY-Robot/main/images/waypointsmap.jpg)

## Coming Soon

- Navigation Algorithm
- Voltage sensor with ADC
- Web UI for sensor monitoring
- Different Accounts for security
- And more!