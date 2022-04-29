import cv2
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)

# faces = cv2.CascadeClassifier(cv2.cv2.haarcascades+'frontal_face_cascade.xml')
# body = cv2.CascadeClassifier(cv2.cv2.haarcascade+'haarcascade_fullbody.xml')
face = FaceDetector()
while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    new_img, idd = face.findFaces(img)

    if idd:
        cv2.imwrite("Mark.jpg",new_img)
        cv2.imshow("Live View",img)
    else:
        print("no face found")

    if cv2.waitKey(1) == ord('q'):
        break

cap.close()

cv2.destroyAllWindows()
