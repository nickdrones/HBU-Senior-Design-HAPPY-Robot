# PYTHON 3
from adafruit_servokit import ServoKit
import time
import array as arr
kit = None
leftSpeed = None
rightSpeed = None

def setup():
    print("Establishing Communication with PCA9685 over I2C")
    kit = ServoKit(channels=16)
    print("Connection with PCA9685 Established")

def driveChassisStraight(percentPower):
    ####################################
    # This function allows us to use a power
    #  percentage value between 100% and -100%
    #  to control the speed and direction of
    #  the robot for driving fully straight. 
    ####################################
    frontAngle=90-percentPower*(9/10)
    rearAngle=90+percentPower*(9/10)
    kit.servo[3].angle=rearAngle
    kit.servo[2].angle=frontAngle
    kit.servo[1].angle=rearAngle
    kit.servo[0].angle=frontAngle
    return

def driveChassisLR(percentPowerLeft, percentPowerRight):
    ####################################
    # This function allows us to use a power
    #  percentage value between 100% and -100%
    #  to control the speed and direction of
    #  the robot for each side independently. 
    ####################################
    frontRightAngle=90-percentPowerRight*(9/10)
    rearRightAngle=90+percentPowerRight*(9/10)
    frontLeftAngle=90-percentPowerLeft*(9/10)
    rearLeftAngle=90+percentPowerLeft*(9/10)
    
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

def driveChassisStraight_Ramp(percentPower,rampSpeed):
    ####################################
    # This function allows us to use a power
    #  percentage value between 100% and -100%
    #  to control the speed and direction of
    #  the robot. Also, 0-100 can be input
    #  to control the speed at which the
    #  motors ramp up to full power.
    ####################################
    tempMotorPercent=0
    stepAmount=percentPower/rampSpeed
    while abs(tempMotorPercent) < abs(percentPower):
        frontRightAngle=90-tempMotorPercent*(9/10)
        rearRightAngle=90+tempMotorPercent*(9/10)
        frontLeftAngle=90-tempMotorPercent*(9/10)
        rearLeftAngle=90+tempMotorPercent*(9/10)
        kit.servo[3].angle=rearRightAngle
        kit.servo[2].angle=frontRightAngle
        kit.servo[1].angle=rearLeftAngle
        kit.servo[0].angle=frontLeftAngle
        time.sleep(0.01)
        tempMotorPercent+=stepAmount
    frontRightAngle=90-percentPower*(9/10)
    rearRightAngle=90+percentPower*(9/10)
    frontLeftAngle=90-percentPower*(9/10)
    rearLeftAngle=90+percentPower*(9/10)
    kit.servo[3].angle=rearRightAngle
    kit.servo[2].angle=frontRightAngle
    kit.servo[1].angle=rearLeftAngle
    kit.servo[0].angle=frontLeftAngle
    return

if __name__ == '__main__':
	setup()