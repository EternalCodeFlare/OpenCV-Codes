import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Livestream",frame)
#   To exit the livestream press: esc key(this will also capture your photo and save it in the current working directory)
    if (cv2.waitKey(1)==27):
        cv2.imwrite('opencv1.png', frame)
        break
cap.release()
cv2.destroyAllWindows()
