import cv2
import math
import numpy as np
from imutils.video.pivideostream import PiVideoStream
import imutils
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import threading
import motion_controller
import RPi.GPIO as GPIO


class Vision:
    """Vision Class"""
    def __init__(self, queue, queue_main):
        self.vs = PiVideoStream().start()
        
        self.queue = queue
        self.queue_main = queue_main      
        self.shapes = ['spade', 'club', 'diamond', 'heart']
        self.shape_contours = self.get_reference_shapes_contours()
        self.found_white_egg = False
        self.found_brown_egg = False
        self.event = threading.Event()
        self.data = None
        self.object_to_find = ""

        #timer for sending data
        self.send_data_worker = threading.Thread(target=self.send_data)
        self.send_data_worker.start()

        self.method = "brownegg"
        self.symbol_brown_egg = "spade"
        self.symbol_white_egg = "club"
        self.show_feed = False        

        #Variables for finding objects
        self.balloonRadius = 100
        self.eggRadius = 50
        self.shapeArea = 1000
        self.distance = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.OUT)
        self.pwm = GPIO.PWM(21, 100)
        self.pwm.start(5)
        
        sleep(.2)   
         

    def update(self):
        """Process one frame"""       
        frame = self.vs.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		
        if not self.queue.empty():
            command = self.queue.get()
            commands = command['egg']
            split = commands.split(",")
            if 'egg' in command:
                self.symbol_brown_egg = self.shapes[int(split[0])-1]
                print(self.symbol_brown_egg)
                self.symbol_white_egg = self.shapes[int(split[1])-1]
                print(self.symbol_white_egg)
                self.method = "brownegg"
            elif 'distance' in command:
                self.distance = commands
            else:
                print("We didnt get an egg command")

        if self.method == "cards":
            # Detect the shapes            
            if self.object_to_find == "spade":
                self.process_shape(hsv, frame.copy())
            elif self.object_to_find == "club":
                self.process_shape(hsv, frame.copy())
            elif self.object_to_find == "diamond":
                self.process_shape(hsv, frame.copy())
            elif self.object_to_find == "heart":
                self.process_shape(hsv, frame.copy())
                
        elif self.method == "redballoon":
            self.get_round_contour(hsv, frame.copy())
        elif self.method == "brownegg" or "whiteegg":
            self.get_round_contour(hsv, frame.copy())
        else:
            return ValueError("Couldn't parse the given method")

        cv2.waitKey(10)
    
    def fury_road(self):
        self.data = "0"
        sleep(8.56)
        self.data = "idle"
        sleep(30)
        self.data = "0"
    
    # New method
    def process_shape(self, hsv, frame):
        #find the proper contours
        red = self.color_filter(hsv, 'red')
        _, red_contours, _ = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        black = self.color_filter(hsv, 'black')
        _, black_contours, _ = cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        contour = self.shape_contours[self.object_to_find]
        found_contour = self.best_matching_shape((red_contours if self.object_to_find == 'heart' or 'diamond' else black_contours), contour)
        
        center = None
        ((x,y), radius) = cv2.minEnclosingCircle(contour)
        M=cv2.moments(contour)

        if self.show_feed:
            if self.object_to_find == "heart" or "diamond":
                cv2.drawContours(frame, found_contour, 0, (0,255,0), 3)
                self.show_image("shape", red_contours)
            if self.object_to_find == "spade" or "club":
                cv2.drawContours(frame, found_contour, 0, (0,255,0), 3)
                self.show_image("shape", black_contours)

        try:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        except:
            pass

        if found_contour is not None:
            print("Found %s moving towards it" % self.object_to_find)
            if radius > 75:
                #if self.distance < 250 and self.distance > 0:
                self.data = "height,110"
                print("High mode for dropping of the egg")
                sleep(2)
                print("dropping the egg")
                self.open()
                if self.method == "brownegg":
                    self.method = "whiteegg"
                if self.method == "whiteegg":
                    self.method = "brownegg"
            else:
                self.data = self.offset_center(frame, center)[0]
        else:
            self.data = "rotate_right"
        
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

    def close(self):
        print("closing beak")
        for i in range(6):
            duty = float(40- (i * 4)) / 10.0 + 2.5
            self.pwm.ChangeDutyCycle(duty)
            sleep(0.05)
    
    def open(self):
        print("opening beak")
        for i in range(6):
            duty = float(16+ (i * 4)) / 10.0 + 2.5
            self.pwm.ChangeDutyCycle(duty)
            sleep(0.05)    

    #New method only calculates stuff for the largest contour in the frame
    def get_round_contour(self, hsv, frame):
        mask = self.color_filter(hsv, self.method)
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        contour = self.get_largest_contour(contours)
        ((x,y), radius) = cv2.minEnclosingCircle(contour)
        M=cv2.moments(contour)

        try:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        except:
            pass

        if radius > 10:
            print("Found a contour with a radius larger than 10")
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)                
            color = (255,255,255)

            #Balloon module
            if(self.method == "redballoon"):
                if radius > self.balloonRadius:
                    self.data = "clap"
                else: 
                    self.data = self.offset_center(frame, center)[0]
            
            #Egg module
            elif (self.method == "brownegg" or "whiteegg"):

                #Debug info
                if self.method == "brownegg":
                    print("Currently looking for brown egg")
                elif self.method == "whiteegg":
                    print("Currently looking for white egg")

                if radius > self.eggRadius:
                    self.data = "height,85"
                    sleep(1)
                    self.close()

                    if self.method == "brownegg":
                        self.found_brown_egg = True
                        self.object_to_find = self.symbol_brown_egg
                        print("Found brown egg, now searching for %s" % self.symbol_brown_egg)          
                        self.method = "cards"

                    elif self.method == "whiteegg":
                        self.found_white_egg = True
                        self.object_to_find = self.symbol_brown_egg
                        print("Found white egg, now searching for %s " % self.symbol_white_egg)                           
                        self.method = "cards"
                else:
                    self.data = self.offset_center(frame, center)[0]
        
        # if we cant find a contour with a radius > 10 we should look around for something bigger
        elif self.method == "brownegg" or "whiteegg":
            self.data = "rotate_right"
        if self.show_feed:
            cv2.imshow('round shape', frame)

    def offset_center(self, frame, center):
        shape = frame.shape
        x_offset = float(center[0] - shape[1] / 2)
        x_offset = float((x_offset / 320) * 180)
        y_offset = shape[0] /2 - center[1]
        return (x_offset, y_offset)

    def best_matching_shape(self, contours, shape):
        """Returns the best matching shape, None if not found a match"""
        best_shape = None
        best_value = 999
        
        for contour in contours:
            # Skip if contour is too small
            if cv2.contourArea(contour) < self.shapeArea:
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
        """Filters the hsv values with the given color"""
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
            raise ValueError('Fool!!, wrong color')
        return result

    def send_data(self):
        while True:
            if self.data is None:
                continue

            #Send values
            elif "height" in self.data:
                self.queue_main.put({'motion_command' : self.data})
            else:
                self.queue_main.put({'objectcoords': self.data})


            print(str(self.data))
            self.event.wait(10)
    
    def release(self):
        self.vs.stop()
        cv2.destroyAllWindows()

# If executed instead of import show a little demo
if __name__ == '__main__':
    vision = Vision(True)
    vision.update()
    cv2.waitKey()
