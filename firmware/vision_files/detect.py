# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import math

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        img = frame.array

        # show the frame

        img = cv2.GaussianBlur(img, (13,13), 0)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
        cv2.imshow('thresh', thresh)
        image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

        for i in range(len(contours)):
            contour = contours[i]
            area = cv2.contourArea(contour)
            if area < 500:
                continue
            perimeter = cv2.arcLength(contour, True)
            factor = 4 * math.pi * area / perimeter ** 2
            if factor > .3:
                cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)
                M = cv2.moments(contour)
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, ("Factor: %f" % factor),(cx,cy), font, .5, (0,255,0),2)

	rawCapture.truncate(0)
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
