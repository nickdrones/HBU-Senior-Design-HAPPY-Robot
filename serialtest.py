#!/usr/bin/python3
import time
import serial


serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
time.sleep(2)

# Send a simple header
print("Start of Program")

while True:
    try:
        
        ser_bytes = serial_port.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)

        # bytesToRead = serial_port.inWaiting()
        # data = serial_port.read(bytesToRead)
        # databits.append(data)
        # print(data)
        # databit += data
        # if we get a carriage return, add a line feed too
        # \r is a carriage return; \n is a line feed
        # This is to help the tty program on the other end 
        # Windows is \r\n for carriage return, line feed
        # Macintosh and Linux use \n
        # if data == "\r".encode():
        # if len(databits) > 100:
        # #For Windows boxen on the other end
        # #serial_port.write("\n".encode())
        # print("Complete message: ")
        # print(databits)
        # break


    except KeyboardInterrupt:
        print("Exiting Program")

    except Exception as exception_error:
        print("Error occurred. Exiting Program")
        print("Error: " + str(exception_error))

    finally:
        serial_port.close()
        pass
