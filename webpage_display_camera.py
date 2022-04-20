from flask import Flask, Response
import cv2

app = Flask(__name__)

#use on pc but NOT jetson
#video = cv2.VideoCapture(0)

#use on Jetson but NOT pc
import jetson.inference
import jetson.utils
import argparse
import sys
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
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)


@app.route('/')
def index():
    return "Default Message"


def gen():
    while True:
        #success, image = video.read()
        image = input.Capture()
        #frame_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #frame_gray = cv2.equalizeHist(frame_gray)

        #ret, jpeg = cv2.imencode('.jpg', image)

        frame = image.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2204, threaded=True)