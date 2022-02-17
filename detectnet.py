import jetson.inference
import jetson.utils

import argparse
import sys

# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.",
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

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


# load the object detection network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)

# create video sources
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)


# process frames until the user exits
while True:
        # capture the next image
        img = input.Capture()

        # detect objects in the image (with overlay)
        detections = net.Detect(img, overlay=opt.overlay)

        # print the detections
        print("detected {:d} objects in image".format(len(detections)))


        for detection in detections:
                if (net.GetClassDesc(detection.ClassID) == "person"):
                    #print(detection)
                    detectionString = str(detection)
                    lines = detectionString.split("\n")
                    line_11 = lines[10]
                    class_desc = net.GetClassDesc(detection.ClassID)
                    print ("Detected " + class_desc + line_11)



        # exit on input/output EOS
        if not input.IsStreaming() or not output.IsStreaming():
                break
