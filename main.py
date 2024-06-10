import cv2 as cv
import numpy as np

def getContours(img):
    contours, hiearchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if area>500:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            print(peri)
            approx  = cv.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv.boundingRect(approx)
            
            if objCor ==3:objectType = 'triangle'
            elif objCor == 4:
                aspratio = w/float(h)
                if aspratio>0.95 and aspratio<1.05:
                    objectType = "square"
                else: objectType = "rectangle"
            elif objCor>4: objectType = "circle"
            else:objectType = "None"
            cv.rectangle(imgContour, (x, y), (x+w, y+h), (0,255,0), 2)

            cv.putText(imgContour, objectType,
                       (x+(w//2)-10, y+(h//2)-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)            

img  = cv.imread('shapes2.jpeg')
imgContour = img.copy()
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)

imgCanny = cv.Canny(imgBlur, 50, 50)

getContours(imgCanny)
cv.imshow('sdvfddsf', imgContour)


cv.waitKey(0)
