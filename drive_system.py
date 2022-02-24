# PYTHON 3
from adafruit_servokit import ServoKit
import time

class Chassis:
    
    # instance attributes
    def __init__(self):
        self.kit = ServoKit(channels=16)
        self.name = "Hermes"
        self.leftSpeed = 0
        self.rightSpeed = 0
    
    def getLeftSpeed(self):
        return self.leftSpeed

    def getRightSpeed(self):
        return self.rightSpeed

    def sing(self, song):
        return " {} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

    def driveChassisStraight(self, percentPower):
        ####################################
        # This function allows us to use a power
        #  percentage value between 100% and -100%
        #  to control the speed and direction of
        #  the robot for driving fully straight. 
        ####################################
        frontAngle=90-percentPower*(9/10)
        rearAngle=90+percentPower*(9/10)
        self.kit.servo[3].angle=rearAngle
        self.kit.servo[2].angle=frontAngle
        self.kit.servo[1].angle=rearAngle
        self.kit.servo[0].angle=frontAngle
        return

    def driveChassisLR(self, percentPowerLeft, percentPowerRight):
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
    
        self.kit.servo[3].angle=rearRightAngle
        self.kit.servo[2].angle=frontRightAngle
        self.kit.servo[1].angle=rearLeftAngle
        self.kit.servo[0].angle=frontLeftAngle
        return

    def stopMotor(self,desiredMotor):
        #####################################
        # This function stops a desired motor
        #   by feeding in the motor name
        #####################################
        if desiredMotor=="frontLeft":
            self.kit.servo[0].angle=90
        if desiredMotor=="rearLeft":
            self.kit.servo[1].angle=90
        if desiredMotor=="frontRight":
            self.kit.servo[2].angle=90
        if desiredMotor=="rearRight":
            self.kit.servo[3].angle=90
        return

    def stopAllMotors(self):
        ##################################
        #  This function stops all motors
        ##################################
        self.stopMotor("frontLeft")
        self.stopMotor("rearLeft")
        self.stopMotor("frontRight")
        self.stopMotor("rearRight")
        return

    def driveChassisStraight_Ramp(self,percentPower,rampSpeed):
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
            self.kit.servo[3].angle=rearRightAngle
            self.kit.servo[2].angle=frontRightAngle
            self.kit.servo[1].angle=rearLeftAngle
            self.kit.servo[0].angle=frontLeftAngle
            time.sleep(0.01)
            tempMotorPercent+=stepAmount
        frontRightAngle=90-percentPower*(9/10)
        rearRightAngle=90+percentPower*(9/10)
        frontLeftAngle=90-percentPower*(9/10)
        rearLeftAngle=90+percentPower*(9/10)
        self.kit.servo[3].angle=rearRightAngle
        self.kit.servo[2].angle=frontRightAngle
        self.kit.servo[1].angle=rearLeftAngle
        self.kit.servo[0].angle=frontLeftAngle
        return