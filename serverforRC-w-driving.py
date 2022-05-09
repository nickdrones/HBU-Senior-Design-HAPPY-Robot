#!/usr/bin/env python
from socket import *
from time import ctime          # Import necessary modules
from adafruit_servokit import ServoKit


def driveChassisLR(percentPowerLeft, percentPowerRight):
    ####################################
    # This function allows us to use a power
    #  percentage value between 100% and -100%
    #  to control the speed and direction of
    #  the robot for each side independently. 
    ####################################
    frontRightAngle=90-percentPowerRight*(9/10)
    rearRightAngle=90-percentPowerRight*(9/10)
    frontLeftAngle=90-percentPowerLeft*(9/10)
    rearLeftAngle=90-percentPowerLeft*(9/10)
    
    kit.servo[3].angle=rearRightAngle
    kit.servo[2].angle=frontRightAngle
    kit.servo[1].angle=rearLeftAngle
    kit.servo[0].angle=frontLeftAngle
    return

def stopMotor(desiredMotor):
    #####################################
    # This function stops a desired motor
    #   by feeding in the motor name
    #####################################
    if desiredMotor=="frontLeft":
        kit.servo[0].angle=90
    if desiredMotor=="rearLeft":
        kit.servo[1].angle=90
    if desiredMotor=="frontRight":
        kit.servo[2].angle=90
    if desiredMotor=="rearRight":
        kit.servo[3].angle=90
    return

def stopAllMotors():
    ##################################
    #  This function stops all motors
    ##################################
    stopMotor("frontLeft")
    stopMotor("rearLeft")
    stopMotor("frontRight")
    stopMotor("rearRight")
    return

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-', 'xy_home']

HOST = ''           # The variable of HOST is null, so the function bind( ) can be bound to all valid addresses.
PORT = 21567
BUFSIZ = 1024       # Size of the buffer
ADDR = (HOST, PORT)

print("Establishing Communication with PCA9685 over I2C")

kit=ServoKit(channels=16)

print("Connection with PCA9685 Established")


print("Initialization Complete")
print("")
print("██████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗")
print("██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝")
print("██████╔╝█████╗  ███████║██║  ██║ ╚████╔╝ ")
print("██╔══██╗██╔══╝  ██╔══██║██║  ██║  ╚██╔╝  ")
print("██║  ██║███████╗██║  ██║██████╔╝   ██║   ")
print("╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝   ")
print("")

tcpSerSock = socket(AF_INET, SOCK_STREAM)    # Create a socket.
tcpSerSock.bind(ADDR)    # Bind the IP address and port number of the server. 
tcpSerSock.listen(5)     # The parameter of listen() defines the number of connections permitted at one time. Once the 
			 # connections are full, others will be rejected. 

while True:
	stopAllMotors()
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
			print('motor moving forward') # receive command "forward", move forward
			driveChassisLR(100,100)
		elif data == ctrl_cmd[1]:
			print('recv backward cmd') # receive command "backward", move backward
			driveChassisLR(-100,-100)
		elif data == ctrl_cmd[2]:
			print('recv left cmd')   # receive command "left", move left
			driveChassisLR(-100,100)
		elif data == ctrl_cmd[3]:
			print('recv right cmd')    # receive command "right", move right
			driveChassisLR(100,-100)
		elif data == ctrl_cmd[4]:
			print('recv stop cmd')      # stop when receive stop command
			stopAllMotors() 
		else:
			print('Command Error! Cannot recognize command: ' + str(data))

tcpSerSock.close()
