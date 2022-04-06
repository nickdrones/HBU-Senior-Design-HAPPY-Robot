import serial
import time

print("UART Demonstration Program")
print("NVIDIA Jetson Nano Developer Kit")


serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
time.sleep(1)

try:
    # Send a message to the Arduino
    while True:
        if serial_port.inWaiting() > 0:
            data = serial_port.readline().decode()
            print(data)
except:
    print("lmao error git rekt")