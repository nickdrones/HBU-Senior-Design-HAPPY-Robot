# COMPUTER VISION CODE
import cv2
import time
def setup():
    print("Initializing Camera...")
    global video 
    video = cv2.VideoCapture(0)
    print("Initializing Camera Complete")

def printArray():
    check, frame = video.read()
    print(check)
    print(frame)
    time.sleep(3)

def destroyTheRing():
    video.release()

if __name__ == '__main__':
	setup()