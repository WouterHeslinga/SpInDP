# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from collections import deque
from random import randint
import time
import cv2
import numpy as np


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (608, 512)
camera.framerate = 60
rawCapture = PiRGBArray(camera, size=(608, 512))

#define range of blue color in hsv
#red
lower_red = (0, 159, 114)
upper_red = (204, 245, 255)
pts = deque(maxlen=20)

# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    frame = frame.array
    #frame = cv2.flip(frame, -1)

    # show the frame to our screen
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1) & 0xFF
        
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
