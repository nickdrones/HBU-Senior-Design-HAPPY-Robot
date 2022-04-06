import serial
import time

print("UART Demonstration Program")
print("NVIDIA Jetson Nano Developer Kit")


serial_port = serial.Serial(
    port="/dev/ttyACM0",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
print("waiting 10 seconds")
time.sleep(10)
print("done waiting, sending commands")

try:
    # Send a message to the Arduino
    serial_port.write("B".encode())
    while True:
        if serial_port.inWaiting() > 0:
            data = serial_port.readline().decode()
            print(data)
            break
    print("if you see me, the break worked")

except:
    print("lmao error git rekt")