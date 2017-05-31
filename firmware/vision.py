import cv2
import numpy as np

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

# If executed instaid of import show a little demo
if __name__ == '__main__':
    shapes = get_reference_shapes_contours()

    for key, val in shapes.items():
        print('%s: %s' % (key, cv2.contourArea(val)))
    
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        
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

    cap.release()
    cv2.destroyAllWindows()