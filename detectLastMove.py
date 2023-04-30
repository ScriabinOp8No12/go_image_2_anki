import cv2

def detect_circles(img):

    # Convert the image to grayscale, houghcircles method requires this
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to preprocess image better, it actually does make a difference
    gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Parameters for Hough Circle Transform
    dp = 1          # default value
    minDist = 20    # default value
    param1 = 50     # default value
    param2 = 30     # default value
    minRadius = 10  # between 10 and 15 radius gets you the hollow inner circle
    maxRadius = 15

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT, dp, minDist,
                               param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    if circles is None:
        # print("False")
        return False
    else:
        # print("True")
        return True


# remember to read the image first (for other modules when I export it)
# img = cv2.imread(r"C:\Users\nharw\Desktop\Extra folder of puzzles\Eric 11 2023-02-22.png")
# detect_circles(img)


