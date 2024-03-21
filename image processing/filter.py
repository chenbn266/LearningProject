import cv2
print(cv2.__version__)

img = cv2.imread("../dataset/miku.jpg")
cv2.imshow("miku",img)
cv2.waitKey(0)
cv2.destroyAllWindows()