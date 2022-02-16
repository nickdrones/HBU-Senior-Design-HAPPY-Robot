# GPS CODE SERIAL READ
import time
import serial
def setup():
    print("Initializing Serial Comms to GPS...")

    global serial_port 
    serial_port = serial.Serial(port="/dev/ttyTHS1",baudrate=115200,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,)
    
    print("Initializing GPS Complete")

if __name__ == '__main__':
	setup()

#Help: https://github.com/JetsonHacksNano/UARTDemo/blob/master/uart_example.py