import cv2
def detect_circles(img):

    # Convert the image to grayscale, houghcircles method requires this
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to preprocess image better, larger values = more smoothing, they are usually
    # Odd numbers, it allows the kernel to be centered on the pixel being processed.
    # For example, a (3, 3) kernel has a center pixel and one pixel on each side of it in both the horizontal and vertical directions.
    gray_blur = cv2.GaussianBlur(gray, (7, 7), 0) # (7,7) perfectly detected from 83 puzzles, that had 30 hollow circles, and 53 non-hollow circles

    # Parameters for Hough Circle Transform
    dp = 1          # default value 1
    minDist = 1    # default value 20
    param1 = 50     # default value 50
    param2 = 30    # default value 30
    minRadius = 10  # min radius 10
    maxRadius = 15  # max radius 15

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT, dp, minDist,
                               param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    return circles is not None
