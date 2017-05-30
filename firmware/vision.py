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
        hirachy, contours, _ = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour = get_largest_contour(contours)

        results[shape] = contour    
    return results

# If executed instaid of import show a little demo
if __name__ == '__main__':
    shapes = get_reference_shapes_contours()

    for key, val in shapes.items():
        print('%s: %s' % (key, cv2.contourArea(val)))
    cv2.waitKey(0)