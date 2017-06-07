import cv2
import numpy as np

class Vision:
    """Vision Class"""
    def __init__(self, show_feed, queue):
        self.queue = queue
        self.cap = cv2.VideoCapture(0)
        self.show_feed = show_feed
        self.status = {
            'symbols': {
                'heart': False,
                'spade': False,
                'club': False,
                'diamond': False
            }
        }
        self.shapes = ['club', 'diamond', 'heart', 'spade']
        self.shape_contours = self.get_reference_shapes_contours()

    def update(self):
        """Process one frame"""
        _, frame = self.cap.read()

        # Blur the image and get the hsv values
        blur = cv2.GaussianBlur(frame, (7,7), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        # Detect the shapes
        self.process_shapes(hsv, frame.copy() if self.show_feed else None)

        self.queue.put(self.status)
        cv2.waitKey(10)

    def process_shapes(self, hsv, render_frame=None):
        """Detects the four symbols"""
        # Find the contours
        red = self.color_filter(hsv, 'red')
        _, red_contours, _ = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        black = self.color_filter(hsv, 'black')
        _, black_contours, _ = cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Match each individual shapes
        for shape in self.shapes:
            contour = self.shape_contours[shape]
            found_contour = self.best_matching_shape((red_contours if shape == 'heart' or shape == 'diamond' else black_contours), contour)
            self.status['symbols'][shape] = found_contour is not None

            # Draw contour if show_Feed is true
            if found_contour is not None and render_frame is not None:
                print("Found %s" % shape)
                render_frame = cv2.drawContours(render_frame, [found_contour], 0, (0, 255, 0), 3)
        
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
    
    def best_matching_shape(self, contours, shape):
        """Returns the best matching shape, None if not found a match"""
        best_shape = None
        best_value = 999
        
        for contour in contours:
            # Skip if contour is too small
            if cv2.contourArea(contour) < 100:
                continue
            
            match_value = cv2.matchShapes(contour, shape, 1, 0.0)
            # Skip contour if there was a contour that has a better match
            if match_value > .02 or match_value > best_value:
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
            result = cv2.inRange(hsv, (0, 161, 80), (255, 255, 255))
            # HSV colors hue is in 360 deg, so we need values in the negative. Use a seccond range and bitwise those.
            # result = cv2.bitwise_or(result, cv2.inRange(hsv, (158, 137, 60), (182, 255, 255)))
        elif color == 'black':
            result = cv2.inRange(hsv, (0, 0, 0), (179, 255, 100))
        else:
            raise ValueError('Fool!!, only black and red!')
        return result

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

# If executed instaid of import show a little demo
if __name__ == '__main__':
    vision = Vision(True)
    vision.update()
    cv2.waitKey()