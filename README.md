# Husky Automated Package and Parcel deliverY (HAPPY)

We are a team of four seniors in the HBU Class of 2022 from the College of Science and Engineering. Our team is comprised of two Electrical Engineering majors, one Computer Science major, and one Cyber Engineering major.


## About this project

\<TO BE FILLED IN WITH DETAILS LATER>
Also the design document will be uploaded to this repository once the full release is complete at the end of the semester.


## Code Details
Computer Vision code based off samples found here: [https://github.com/dusty-nv/jetson-inference/](https://github.com/dusty-nv/jetson-inference/)

I2C and PCA9685 code based off documentation here: [https://www.jetsonhacks.com/2019/07/22/jetson-nano-using-i2c/](https://www.jetsonhacks.com/2019/07/22/jetson-nano-using-i2c/)

Drive code is written in Python 3 and uses the adafruit_servokit library. Command to install the library is below:
> pip3 install adafruit-circuitpython-servokit

Serial communication utilizes pyserial which can be installed using the following command:
> sudo apt-get install python3-serial

MAIN.py is the main code, run in Python3 as sudo (failing to run as sudo will result in serial port access failing)

## Coming Soon

- GPS Sensor integration
- Navigation Algorithm
- And more!