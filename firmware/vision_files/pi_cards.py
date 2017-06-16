# import the necessary packages
from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
from collections import deque
import argparse
import imutils
import time
import cv2
import numpy as np
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--num-frames", type=int, default=10000, help="# of frames to loop over for FPS test")
ap.add_argument("-d", "--display", type=int, default=-1, help="Whether or not frames should be displayed")
args = vars(ap.parse_args())
 
lower_red = (0,159,114)
upper_red = (204,245,255)
pts = deque(maxlen=20)
# initialize the camera and stream
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(1920, 1080))
#stream = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)
#stream.close()
rawCapture.close()
camera.close()



def get_largest_contour(contours):
    """Returns the largest contour"""
    largest_size = 0
    largest_contour = None

    for contour in contours:
        size = cv2.contourArea(contour)
        if size > largest_size:
            largest_size = size
            largest_contour = contour
    
    return largest_contour

def best_matching_shape(contours, shape):
    """Returns the best matching shape, None if not found a match"""
    best_shape = None
    best_value = 999
    
    for contour in contours:
        # Skip if contour is too small
        if cv2.contourArea(contour) < 100:
            continue
        
        match_value = cv2.matchShapes(contour, shape, 1, 0.0)
        # Skip contour if there was a contour that has a better match
        if match_value > .1 or match_value > best_value:
            continue
        
        best_shape = contour
        best_value = match_value
    
    return best_shape

def get_reference_shapes_contours():
    """Returns a dictionary of the four symbol contours"""
    results = {}
    shapes = ['club', 'diamond', 'heart', 'spade']

    for shape in shapes:
        # Blur, grayscale and threshold for binary image
        frame = cv2.imread('assets/%s.jpg' % shape)
        frame = cv2.GaussianBlur(frame, (3,3), 0)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, frame = cv2.threshold(frame, 169, 255, cv2.THRESH_BINARY_INV)

        # Find the largest contour
        _, contours, hirachy = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour = get_largest_contour(contours)

        results[shape] = contour    
    return results


def color_filter(hsv, color):
    """Filters the hsv values with the given color, the options are 'red' and 'black'"""
    result = None
    if color == 'red':
        result = cv2.inRange(hsv, (0, 161, 80), (255, 255, 255))
        # HSV colors hue is in 360 deg, so we need values in the negative. Use a seccond range and bitwise those.
        # result = cv2.bitwise_or(result, cv2.inRange(hsv, (158, 137, 60), (182, 255, 255)))
    elif color == 'black':
        result = cv2.inRange(hsv, (0, 0, 0), (179, 255, 100))
    else:
        raise ValueError('Fool!!, only black and red!')
    return result



# created a *threaded *video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from `picamera` module...")
vs = PiVideoStream().start()
time.sleep(2.0)
fps = FPS().start()

shapes = get_reference_shapes_contours()

for key, val in shapes.items():
    print('%s: %s' % (key, cv2.contourArea(val)))

# loop over some frames...this time using the threaded stream
while fps._numFrames < args["num_frames"]:
    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels
    frame = vs.read()
    frame = cv2.flip(frame, -1)
    #frame = imutils.resize(frame, width=320)
 
    blur = cv2.GaussianBlur(frame, (7,7), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    red = color_filter(hsv, 'red')
    _, red_contours, _ = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    black = color_filter(hsv, 'black')
    _, black_contours, _ = cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow('red', red)
    cv2.imshow('black', black)

    heart = best_matching_shape(red_contours, shapes['heart'])
    if heart is not None:
        frame = cv2.drawContours(frame, [heart], 0, (190, 190, 90), 3)
        
    diamond = best_matching_shape(red_contours, shapes['diamond'])
    if diamond is not None:
        frame = cv2.drawContours(frame, [diamond], 0, (0, 255, 0), 3)

    spade = best_matching_shape(black_contours, shapes['spade'])
    if spade is not None:
        frame = cv2.drawContours(frame, [spade], 0, (180, 10, 0), 3)

    club = best_matching_shape(black_contours, shapes['club'])
    if club is not None:
        frame = cv2.drawContours(frame, [club], 0, (0, 10, 180), 3)
        
    cv2.imshow('Output', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
    # update the FPS counter
    fps.update()
 
# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
