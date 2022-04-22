import drive_system
import sensors
import time
import statusled
import signal
from threading import Thread


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

print("Initializing Nvidia Inference Libraries (This may take up to 30 seconds normally, or 15 minutes on a first boot)")
Sauron = sensors.primaryCamera()
print("Inference Models successfully loaded to RAM")
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

HAL.KITT()

#while(1==1):
#    combocoords = Navi.getComboCoords()
#    print(combocoords)
#    time.sleep(2)
#    Sauron.processFrame()


quit()