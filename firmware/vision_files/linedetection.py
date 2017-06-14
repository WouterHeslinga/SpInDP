import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera

WIDTH = 640
HEIGHT = 480
camera = cv2.VideoCapture(0)


def fury_road_progress(frame_hsv, progress):
    """Checks the current progress on following the Fury Road
    by ROI-ing a certain area, checking its color, and comparing it to earlier
    progress
    """
    if progress % 2 == 1:
        if average(frame_hsv)[0] < 11:
            progress += 1
    else:
        if average(frame_hsv)[2] < 50:
            progress += 1

    if progress == 1:
        return "Step 1: No circle seen yet", progress
    elif progress == 2:
        return "Step 2: Seen bottom of red circle", progress
    elif progress == 3:
        return "Step 3: Seen black line inside circle", progress
    elif progress == 4:
        return "Step 4: Seen top of red circle", progress
    elif progress == 5:
        return "Step 5: Seen black line. First rest, then I finish", progress


def average(frame):
    """Takes an image and returns an array containing average H, S and V"""
    return np.average(np.average(frame, axis=0), axis=0)


def capture(camera):
    with camera as stream:
        camera.capture(stream, format='bgr', use_video_port=True)
        # At this point the image is available as stream.array
        image = stream.array
    return


def selection(frame, width, height, x_offset=0, y_offset=0):
    """Takes a selection from the frame and turns it into its own image.
    The initial starting pixel is the center of the screen, and the rectangle
    will be made with the starting pixel as the center of the ROI
    """
    center_x = WIDTH / 2
    center_y = HEIGHT / 2

    return frame[center_y - (height / 2) + y_offset:
                 center_y + (height / 2) + y_offset,
                 center_x - (width / 2) + x_offset:
                 center_x + (width / 2) + x_offset]


progress = 1
message = ""

if __name__ == '__main__':
    while True:
        frame_input = camera.read()
        selection = cv2.cvtColor(selection(frame_input, 10, 10),
                                 cv2.COLOR_BGR2HSV)

        message, progress = fury_road_progress(selection, progress)

        print(message)
        cv2.imshow('frame', frame_input)
        cv2.imshow('selection', selection)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
