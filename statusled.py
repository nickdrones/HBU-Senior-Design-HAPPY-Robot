import board
from adafruit_ht16k33.bargraph import Bicolor24
import time

class ledbar:
    def __init__(self):
        self.name = "HAL"
        self.i2c_led = board.I2C()
        self.bc24 = Bicolor24(self.i2c_led)


    def GreenFillTo(self,amount):  #fill LED Bar with green from 0 to designated number
        for x in range(amount):
            self.bc24[x]  = self.bc24.LED_GREEN

    def RedFillTo(self,amount): #fill LED Bar with red from 0 to designated number
        for x in range(amount):
            self.bc24[x]  = self.bc24.LED_RED

    def YellowFillTo(self,amount): #fill LED Bar with yellow from 0 to designated number
        for x in range(amount):
            self.bc24[x]  = self.bc24.LED_YELLOW

    def YellowCreepTo(self,amount):   #slowly fill LED Bar with yellow from 0 to designated number
        for x in range(amount):
            self.bc24[x]  = self.bc24.LED_YELLOW
            time.sleep(0.07)

    def allOff(self):      #turn off all LEDs on bar
        self.bc24.fill(self.bc24.LED_OFF)

    def showSuccessfulDeviceInit(self):  #flash yellow to indicate LED bar initialization complete
        for x in range(2):
            self.bc24.fill(self.bc24.LED_YELLOW)
            time.sleep(0.3)
            self.allOff()
            time.sleep(0.3)

    def showSuccessfulRobotInit(self):   #flash green to indicate full robot init
        self.allOff()
        time.sleep(1)
        for x in range(4):
            self.bc24.fill(self.bc24.LED_GREEN)
            time.sleep(0.5)
            self.allOff()
            time.sleep(0.5)

    def KITT(self):    #bounce single red LED back and forth on bar like KITT from the tv show Knight Ryder
        while 1==1:
            for x in range(23):
                self.bc24[x]  = self.bc24.LED_RED
                time.sleep(0.03)
                self.bc24[x] = self.bc24.LED_OFF
            for x in range(23):
                self.bc24[23-x]  = self.bc24.LED_RED
                time.sleep(0.03)
                self.bc24[23-x] = self.bc24.LED_OFF
