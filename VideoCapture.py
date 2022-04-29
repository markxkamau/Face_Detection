import cv2

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    cv2.imshow("Video",img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.close()

cv2.destroyAllWindows()
