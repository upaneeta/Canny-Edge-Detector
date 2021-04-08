import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    success,frame=cap.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur_frame=cv2.GaussianBlur(gray_frame,(3,3),0)
    canny_frame=cv2.Canny(blur_frame,45,100)
    cv2.imshow("Original",frame)
    cv2.imshow("Canny Edges",canny_frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
