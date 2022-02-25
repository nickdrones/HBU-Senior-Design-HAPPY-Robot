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
        with contextlib.redirect_stdout(io.StringIO()) as f:
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
            # create video output object
            self.output = jetson.utils.videoOutput(self.opt.output_URI, argv=sys.argv+is_headless)
            # load the object detection network
            self.net = jetson.inference.detectNet(self.opt.network, sys.argv, self.opt.threshold)
            # create video sources
            self.input = jetson.utils.videoSource(self.opt.input_URI, argv=sys.argv)

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
        #perform first img read to finalize all initialization outputs
        img = self.input.Capture()
        # detect objects in the image (with overlay)
        detections = self.net.Detect(img, overlay=self.opt.overlay)
        # TO BE FINISHED



#Help: https://github.com/JetsonHacksNano/UARTDemo/blob/master/uart_example.py