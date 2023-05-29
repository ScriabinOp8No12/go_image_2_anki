import cv2
def detect_circles(img):

    # Convert the image to grayscale, houghcircles method requires this
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to preprocess image better, it actually does make a difference
    gray_blur = cv2.GaussianBlur(gray, (9, 9), 0)

    # Parameters for Hough Circle Transform
    dp = 1          # default value 1
    minDist = 1    # default value 20
    param1 = 50     # default value 50
    param2 = 30    # default value 30
    minRadius = 10  # between 10 and 15 radius gets you the hollow inner circle
    maxRadius = 15

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT, dp, minDist,
                               param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    return circles is not None
