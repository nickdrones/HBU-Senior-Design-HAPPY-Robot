import jetson.inference
import jetson.utils
from adafruit_servokit import ServoKit
import time
import signal



def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: {}) has been caught. Cleaning up...".format(signal))
    print("Stopping Motors")
    driveChassisLR(0, 0)
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)


import argparse
import sys

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

# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.",
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use")

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
        opt = parser.parse_known_args()[0]
except:
        print("")
        parser.print_help()
        sys.exit(0)


print("Establishing Communication with PCA9685 over I2C")

kit=ServoKit(channels=16)

print("Connection with PCA9685 Established")

time.sleep(2)

print("Establishing computer vision, this may take up to 30 seconds (~10 minutes for first time boot)")

# create video output object
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)

# load the object detection network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)

# create video sources
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)



#perform first img read
img = input.Capture()
# detect objects in the image (with overlay)
detections = net.Detect(img, overlay=opt.overlay)

print("")
print("Initialization Complete")
print("")
print("██████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗")
print("██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝")
print("██████╔╝█████╗  ███████║██║  ██║ ╚████╔╝ ")
print("██╔══██╗██╔══╝  ██╔══██║██║  ██║  ╚██╔╝  ")
print("██║  ██║███████╗██║  ██║██████╔╝   ██║   ")
print("╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝   ")
print("")

x_coords = 0
y_coords = 0

# process frames until the user exits
while True:
        # capture the next image
        img = input.Capture()

        # detect objects in the image (with overlay)
        detections = net.Detect(img, overlay=opt.overlay)

        # print the detections
        #print("detected {:d} objects in image".format(len(detections)))


        for detection in detections:
                if (net.GetClassDesc(detection.ClassID) == "person"):
                    #print(detection)
                    # format: left of screen = "   -- Center:  (101.094, 447.1)"
                    # format: right of screen = "   -- Center:  (1146.88, 393.514)"
                    detectionString = str(detection)
                    lines = detectionString.split("\n")
                    line_11 = lines[10]

                    # Split the line up between the parenthesis and comma and write to variables for X and Y pos
                    temp_found_arr = line_11.split('(')
                    temp_found = temp_found_arr[1]
                    temp_found_x_coords = temp_found.split(', ')
                    x_coords = temp_found_x_coords[0]
                    y_coords = temp_found_x_coords[1].split(')')[0]
                    
                    class_desc = net.GetClassDesc(detection.ClassID)
                    #print ("Detected person at " +  + x_coords + " " + y_coords)

                    x_coords = float(x_coords)
                    y_coords = float(y_coords)

                    if (x_coords < 540):
                        print("slight left")
                        driveChassisLR(50, 100)
                    elif (x_coords > 740):
                        print("slight right")
                        driveChassisLR(100, 50)
                    elif (x_coords >= 540 and 740 >= x_coords):
                        print("straight ahead")
                        driveChassisLR(100, 100)
                    if(net.GetClassDesc(detection.ClassID) != "person"):
                        driveChassisLR(0, 0)



        # exit on input/output EOS
        if not input.IsStreaming() or not output.IsStreaming():
                break
