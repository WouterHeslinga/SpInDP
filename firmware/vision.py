import cv2
import math
import numpy as np
from imutils.video.pivideostream import PiVideoStream
import imutils
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep


class Vision:
    """Vision Class"""
    def __init__(self, show_feed, queue):
        self.vs = PiVideoStream().start()
        sleep(.2)
        self.queue = queue
        self.show_feed = show_feed
        self.method = "balloon"
        #self.object_to_find = object_to_find
        self.status = False
        self.shapes = ['club', 'diamond', 'heart', 'spade']
        self.shape_contours = self.get_reference_shapes_contours()
        #self.symbolarray = symbolarray
        self.delivered_white_egg = False
        self.delivered_brown_egg = False

    def find_egg(self, hsv):
        eggs = ["white", "brown"]


        brown = self.color_filter(hsv, 'brownegg')
        _, brown_contours, _ = cv2.findContours(brown, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        white = self.color_filter(hsv, 'whiteegg')
        _, white_contours, _ = cv2.findContours(white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # search for eggs either white or brown
            # Calibrate gyro sensor 0 point
            # patrol around to search for an egg if we haven't seen one yet
            # if found white egg and found white egg == False
                # pick up white egg
                # find symbolarray[0]
                # move to bowl
                # if close to symbol search blue line
                # drop egg in bowl
                # when done continue with brown egg
            # elif found brown egg and found brown egg == False
                # pick up brown egg
                # find symbolarray[0]
                # move to bowl
                # if close to symbol search blue line
                # drop egg in bowl
                # when done continue with white egg
            # else patrol to find an egg

    def update(self):
        """Process one frame"""        
        frame = self.vs.read()
        # Blur the image and get the hsv values
        blur = cv2.GaussianBlur(frame, (7,7), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        if self.method == "cards":
            # Detect the shapes
            if self.object_to_find == "heart":
                self.process_shapes(hsv, frame.copy() if self.show_feed else None)
            elif self.object_to_find == "spade":
                self.process_shapes(hsv, frame.copy() if self.show_feed else None)
            elif self.object_to_find == "club":
                self.process_shapes(hsv, frame.copy() if self.show_feed else None)
            elif self.object_to_find == "diamond":
                self.process_shapes(hsv, frame.copy() if self.show_feed else None)
                
        elif self.method == "balloon":
            self.get_round_contour(hsv, frame.copy())
        elif self.method == "egg":
            # Detect egg
            self.test = "egg"
        else:
            raise ValueError("Wrong method")

        self.queue.put(self.status)
        cv2.waitKey(10)

    def process_shapes(self, hsv, render_frame=None):
        """Detects the four symbols"""
        # Find the contours
        red = self.color_filter(hsv, 'red')
        _, red_contours, _ = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        black = self.color_filter(hsv, 'black')
        _, black_contours, _ = cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # render threshold
        if render_frame is not None:
            cv2.imshow('black', black)
            cv2.imshow('red', red)

        # Match each individual shapes
        for shape in self.shapes:
            contour = self.shape_contours[shape]
            found_contour = self.best_matching_shape((red_contours if shape == 'heart' or shape == 'diamond' else black_contours), contour)
            self.status['symbols'][shape] = found_contour is not None

            # Draw contour if show_Feed is true
            if found_contour is not None and render_frame is not None:
                print("Found %s" % shape)
                
                color = None
                if shape == 'heart':
                    color = (0, 255, 0)
                if shape == 'diamond':
                    color = (50, 200, 60)
                if shape == 'spade':
                    color = (90, 90, 30)
                if shape == 'club':
                    color = (100, 20, 20)

                render_frame = cv2.drawContours(render_frame, [found_contour], 0, color, 3)
        
        if self.show_feed:
            cv2.imshow(shape, render_frame)
    
    def show_image(self, name, frame):
        if not self.show_feed:
            return
        cv2.imshow(name, frame)
    
    def get_largest_contour(self, contours):
        """Returns the largest contour"""
        largest_size = 0
        largest_contour = None

        for contour in contours:
            size = cv2.contourArea(contour)
            if size > largest_size:
                largest_size = size
                largest_contour = contour
        
        return largest_contour

    def get_round_contour(self, hsv, frame):
        mask = self.color_filter(hsv, 'balloon')
        _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for i in range(len(contours)):
            contour = contours[i]
            area = cv2.contourArea(contour)
            if area < 700:
                continue
            perimeter = cv2.arcLength(contour, True)
            factor = 4 * math.pi * area / perimeter ** 2
            if factor > .5:
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                M = cv2.moments(contour)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, ("Factor: %f" % factor), (cx, cy), font, .5, (0, 255, 0), 2)
            self.show_image('round shape', frame)

    def best_matching_shape(self, contours, shape):
        """Returns the best matching shape, None if not found a match"""
        best_shape = None
        best_value = 999
        
        for contour in contours:
            # Skip if contour is too small
            if cv2.contourArea(contour) < 1000:
                continue
            
            match_value = cv2.matchShapes(contour, shape, 1, 0.0)
            # Skip contour if there was a contour that has a better match
            if match_value > .05 or match_value > best_value:
                continue
            
            best_shape = contour
            best_value = match_value
        
        return best_shape

    def get_reference_shapes_contours(self):
        """Returns a dictionary of the four symbol contours"""
        results = {}

        for shape in self.shapes:
            # Blur, grayscale and threshold for binary image
            frame = cv2.imread('assets/%s.jpg' % shape)
            frame = cv2.GaussianBlur(frame, (3,3), 0)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, frame = cv2.threshold(frame, 169, 255, cv2.THRESH_BINARY_INV)

            # Find the largest contour
            _, contours, hirachy = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contour = self.get_largest_contour(contours)

            results[shape] = contour    
        return results

    def color_filter(self, hsv, color):
        """Filters the hsv values with the given color, the options are 'red' and 'black'"""
        result = None
        if color == 'red':
            result = cv2.inRange(hsv, (0, 180, 80), (255, 240, 255))
        elif color == 'whiteegg':
            result = cv2.inRange(hsv, (0, 0, 150), (255, 75, 255))
        elif color == 'brownegg':
            result = cv2.inRange(hsv, (5, 60, 25), (20, 255, 255))
        elif color == 'redballoon':
            result = cv2.inRange(hsv, (0, 159, 114), (204, 245, 255))
        elif color == 'blue':
            result = cv2.inRange(hsv, (94, 86, 45), (154, 220, 222))
        elif color == 'black':
            result = cv2.inRange(hsv, (0, 0, 0), (179, 255, 100))
        else:
            raise ValueError('Fool!!, only black and red!')
        return result
    
    def release(self):
        self.vs.stop()
        cv2.destroyAllWindows()

# If executed instead of import show a little demo
if __name__ == '__main__':
    vision = Vision(True)
    vision.update()
    cv2.waitKey()
