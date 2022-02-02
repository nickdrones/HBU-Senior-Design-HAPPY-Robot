#PYTHON 3
from adafruit_servokit import ServoKit
import time
import array as arr

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
    motorArray = arr.array("frontLeft","rearLeft","frontRight","rearRight")
    for i in motorArray:
        if motorArray[i] == desiredMotor:
            kit.servo[i].angle=90
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

#################################################################################################################################################

print(" ___  ___  ________  ___  ___          ________  ___       ________  ________   ________           ________  ________       _______  ________    _______   _______               ")
print("|\  \|\  \|\   __  \|\  \|\  \        |\   ____\|\  \     |\   __  \|\   ____\ |\   ____\         |\   __  \|\  _____\     /  ___  \|\   __  \  /  ___  \ /  ___  \              ")
print("\ \  \\\  \ \  \|\ /\ \  \\\  \       \ \  \___|\ \  \    \ \  \|\  \ \  \___|_\ \  \___|_        \ \  \|\  \ \  \__/     /__/|_/  /\ \  \|\  \/__/|_/  //__/|_/  /|             ")
print(" \ \   __  \ \   __  \ \  \\\  \       \ \  \    \ \  \    \ \   __  \ \_____  \\ \_____  \        \ \  \\\  \ \   __\    |__|//  / /\ \  \\\  \__|//  / /__|//  / /             ")
print("  \ \  \ \  \ \  \|\  \ \  \\\  \       \ \  \____\ \  \____\ \  \ \  \|____|\  \\|____|\  \        \ \  \\\  \ \  \_|        /  /_/__\ \  \\\  \  /  /_/__  /  /_/__            ")
print("   \ \__\ \__\ \_______\ \_______\       \ \_______\ \_______\ \__\ \__\____\_\  \ ____\_\  \        \ \_______\ \__\        |\________\ \_______\|\________\\________\          ")
print("    \|__|\|__|\|_______|\|_______|        \|_______|\|_______|\|__|\|__|\_________\\_________\        \|_______|\|__|         \|_______|\|_______| \|_______|\|_______|          ")
print("                                                                       \|_________\|_________|                                                                                   ")
print("                                                                                                                                                                                 ")
print("                                                                                                                                                                                 ")
print("                       ________  _______   ___       ___  ___      ___ _______   ________      ___    ___      ________  ________  _________                                     ")
print("                      |\   ___ \|\  ___ \ |\  \     |\  \|\  \    /  /|\  ___ \ |\   __  \    |\  \  /  /|    |\   __  \|\   __  \|\___   ___\                                   ")
print("                      \ \  \_|\ \ \   __/|\ \  \    \ \  \ \  \  /  / | \   __/|\ \  \|\  \   \ \  \/  / /    \ \  \|\ /\ \  \|\  \|___ \  \_|                                   ")
print("                       \ \  \ \\ \ \  \_|/_\ \  \    \ \  \ \  \/  / / \ \  \_|/_\ \   _  _\   \ \    / /      \ \   __  \ \  \\\  \   \ \  \                                    ")
print("                        \ \  \_\\ \ \  \_|\ \ \  \____\ \  \ \    / /   \ \  \_|\ \ \  \\  \|   \/  /  /        \ \  \|\  \ \  \\\  \   \ \  \                                   ")
print("                         \ \_______\ \_______\ \_______\ \__\ \__/ /     \ \_______\ \__\\ _\ __/  / /           \ \_______\ \_______\   \ \__\                                  ")
print("                          \|_______|\|_______|\|_______|\|__|\|__|/       \|_______|\|__|\|__|\___/ /             \|_______|\|_______|    \|__|                                  ")
print("                                                                                             \|___|/                                                                             ")

print("Establishing Communication with PCA9685 over I2C")

kit=ServoKit(channels=16)

print("Connection Established")

# Servo 3: rear right
# Servo 2: front right
# Servo 1: rear left
# Servo 0: front left

# Drive Forward
kit.servo[3].angle=120
kit.servo[2].angle=60
kit.servo[1].angle=120
kit.servo[0].angle=60

time.sleep(1)

# Drive Backward
kit.servo[3].angle=60
kit.servo[2].angle=120
kit.servo[1].angle=60
kit.servo[0].angle=120

time.sleep(1)

# Stop
kit.servo[3].angle=90
kit.servo[2].angle=90
kit.servo[1].angle=90
kit.servo[0].angle=90

quit()