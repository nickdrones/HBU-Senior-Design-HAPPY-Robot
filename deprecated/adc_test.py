import board
from adafruit_ht16k33.bargraph import Bicolor24
import time


i2c = board.I2C()
bc24 = Bicolor24(i2c)

while 1==1:
    for x in range(23):
        bc24[x]  = bc24.LED_RED
        time.sleep(0.03)
        bc24[x] = bc24.LED_OFF
    for x in range(23):
        bc24[23-x]  = bc24.LED_RED
        time.sleep(0.03)
        bc24[23-x] = bc24.LED_OFF

#bc24[0] = bc24.LED_RED
#bc24[1] = bc24.LED_GREEN
#bc24[2] = bc24.LED_YELLOW
#bc24[3] = bc24.LED_OFF

#time.sleep(1)

#bc24.fill(bc24.LED_GREEN)