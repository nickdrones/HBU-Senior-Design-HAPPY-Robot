import cv2
#from nanocamera.NanoCam import Camera
import nanocamera as nano
import numpy as np

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

if __name__ == '__main__':
    # Create the Camera instance
    camera = nano.Camera(flip=2, width=640, height=480, fps=30)
    print('CSI Camera ready? - ', camera.isReady())
    while camera.isReady():
        try:
            # read the camera image
            frame = camera.read()
            font = cv2.FONT_HERSHEY_SIMPLEX
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )

            boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

            for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
                cv2.rectangle(frame, (xA, yA), (xB, yB),(0, 255, 0), 2)
    
            cv2.putText(frame, 
                'TEXT ON VIDEO', 
                (50, 50), 
                font, 1, 
                (0, 255, 255), 
                2, 
                cv2.LINE_4)
            # display the frame
            cv2.imshow("Video Frame", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        except KeyboardInterrupt:
            break

    # close the camera instance
    camera.release()

    # remove camera object
    del camera