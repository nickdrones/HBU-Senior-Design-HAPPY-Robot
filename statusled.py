import board
from adafruit_ht16k33.bargraph import Bicolor24
import time

class ledbar:
    def __init__(self):
        self.name = "HAL"
        self.tempVar=0
        self.i2c_led = board.I2C()
        self.bc24 = Bicolor24(self.i2c_led)
    def getTempVar(self):
        return self.tempVar
    def GreenFillTo(self,amount):
        for x in range(amount):
            self.bc24[x]  = self.bc24.LED_GREEN
    def RedFillTo(self,amount):
        for x in range(amount):
            self.bc24[x]  = self.bc24.LED_RED
    def YellowFillTo(self,amount):
        for x in range(amount):
            self.bc24[x]  = self.bc24.LED_YELLOW
    def YellowCreepTo(self,amount):
        for x in range(amount):
            self.bc24[x]  = self.bc24.LED_GREEN
            time.sleep(0.07)
    def allOff(self):
        self.bc24.fill(self.bc24.LED_OFF)
    def showSuccessfulDeviceInit(self):
        for x in range(2):
            self.YellowFillTo(24)
            time.sleep(0.3)
            self.allOff()
    def showSuccessfulRobotInit(self):
        self.allOff()
        time.sleep(1)
        for x in range(4):
            self.GreenFillTo(24)
            time.sleep(0.5)
            self.allOff()
    def KITT(self):
        while 1==1:
            for x in range(23):
                self.bc24[x]  = self.bc24.LED_RED
                time.sleep(0.03)
                self.bc24[x] = self.bc24.LED_OFF
            for x in range(23):
                self.bc24[23-x]  = self.bc24.LED_RED
                time.sleep(0.03)
                self.bc24[23-x] = self.bc24.LED_OFF
