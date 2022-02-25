# Sensor Class
# Python 3
import time
import serial
import jetson.inference
import jetson.utils
from adafruit_servokit import ServoKit
import argparse
import sys
import io
import contextlib

class GPS_sensor:
    
    # instance attributes
    def __init__(self):
        self.serial_port = serial.Serial(port="/dev/ttyTHS1",baudrate=115200,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,)
        # Have to run code as sudo to access serial port, or  serial access to all accounts using this command: "sudo chmod 666 /dev/ttyTHS1"
        self.name = "Navi"
        self.lastLongitude = 0
        self.lastLatitude = 0
    
    def getLastLattitude(self):
        return self.lastLatitude

    def getLastLongitude(self):
        return self.lastLongitude

class magnetometer:
    def __init__(self):
        self.name = "Mando"
        self.tempVar=0
    def getTempVar(self):
        return self.tempVar

class primaryCamera:
    
    # instance attributes
    def __init__(self):
        with contextlib.redirect_stderr(io.StringIO()) as f:
            parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.",
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())
            parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
            parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
            parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
            parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
            parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use")
            is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]
            self.opt = parser.parse_known_args()[0]
            silent_output = ["--log-level=silent"]
            # create video output object
            self.output = jetson.utils.videoOutput(self.opt.output_URI, argv=sys.argv+is_headless+silent_output)
            # load the object detection network
            self.net = jetson.inference.detectNet(self.opt.network, sys.argv+silent_output, self.opt.threshold)
            # create video sources
            self.input = jetson.utils.videoSource(self.opt.input_URI, argv=sys.argv+silent_output)

            #perform first img read to finalize all initialization outputs
            img = self.input.Capture()
            # detect objects in the image (with overlay)
            detections = self.net.Detect(img, overlay=self.opt.overlay)

        self.name = "Sauron"
        self.person_heading = 0
        self.lastLatitude = 0
    
    def getLastLattitude(self):
        return self.lastLatitude
    
    def processFrame(self):
        while True:
                # capture the next image
                self.img = self.input.Capture()

                # detect objects in the image (with overlay)
                self.detections = self.net.Detect(self.img, overlay=self.opt.overlay)

                # print the detections
                #print("detected {:d} objects in image".format(len(detections)))


                for detection in self.detections:
                        if (self.net.GetClassDesc(detection.ClassID) == "person"):
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
                            
                            class_desc = self.net.GetClassDesc(detection.ClassID)
                            #print ("Detected person at " +  + x_coords + " " + y_coords)

                            x_coords = float(x_coords)
                            y_coords = float(y_coords)

                            if (x_coords < 540):
                                print("slight left")
                            elif (x_coords > 740):
                                print("slight right")
                            elif (x_coords >= 540 and 740 >= x_coords):
                                print("straight ahead")
                self.person_spotted = False
                for detection in self.detections:
                        if (self.net.GetClassDesc(detection.ClassID) == "person"):
                                person_spotted = True
                if(person_spotted==False):
                    print("nobody")




#Help: https://github.com/JetsonHacksNano/UARTDemo/blob/master/uart_example.py