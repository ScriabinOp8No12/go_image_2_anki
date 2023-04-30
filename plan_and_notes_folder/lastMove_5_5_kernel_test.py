import cv2
import numpy as np
import glob

def detect_circles(img):

    # Convert the image to grayscale, houghcircles method requires this
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to preprocess image better, it actually does make a difference
    # gray_blur = cv2.GaussianBlur(gray, (9, 9), 0)  # (9, 9) was working for all images, EXCEPT for image 1
    gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)   # (5, 5) works for all these images at least
    # try kernel sizes of (3, 3) or (5, 5)  --> very common

    # Parameters for Hough Circle Transform
    dp = 1          # default value
    minDist = 20    # default value
    param1 = 50     # default value
    param2 = 30     # default value
    minRadius = 10  # between 10 and 15 radius gets you the hollow inner circle
    maxRadius = 15

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    # If no circles detected, function immediately returns false
    if circles is not None:
        # Convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loops over each detected circle and extracts its center coordinate (x, y) and radius r.
        for (x, y, r) in circles:
            # draws circle with center: (x, y), radius: r, color: green (0, 255, 0), thickness: 3 pixels
            cv2.circle(img, (x, y), r, (0, 255, 0), 3)

    # Display the resulting image
    cv2.imshow("Detected circles", img)
    cv2.waitKey(0)

img = cv2.imread(r"C:\Users\nharw\Desktop\Extra folder of puzzles\Eric 19 2023-02-22.png")

detect_circles(img)

# path = r'C:\Users\nharw\Desktop\Extra folder of puzzles\*.png'
#
# for image in glob.glob(path):
#     img = cv2.imread(image)
#     detect_circles(img)
