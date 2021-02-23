import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)

while True:
    ret , frame=cap.read()
    if frame is None:
        break


    fgmask = fgbg.apply(frame)


    cv2.imshow("Live_Here",frame)
    cv2.imshow("FG MASK FRAME",fgmask)

    if (cv2.waitKey(30)==27):
        break


cap.release()
cv2.destroyAllWindows()
