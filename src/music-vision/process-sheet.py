import numpy as np
import cv2

filename = "/Users/parkerhewitt/Code/Personal/Python/clefftop/images/many-staff.jpg"
img = cv2.imread(filename)
print("img dimensions: %s" % str(img.shape))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("thresh", thresh)

if not img.data:
    print("failed to read filenname: " + filename)
    exit()

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,7))
virtical_thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 1)
_,cnts,_ = cv2.findContours(virtical_thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, cnts, -1, (0,255,0), 3)
cv2.imshow("virt_thresh", virtical_thresh)
cv2.imshow("circled!" ,img)
cv2.waitKey(0)



