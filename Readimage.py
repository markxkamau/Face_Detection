import cv2

img = cv2.imread("./Images/Kakashi.jpg", 0)
img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)


cv2.imwrite("New_img.jpg", img)

cv2.imshow("Hokage_Kakashi", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
