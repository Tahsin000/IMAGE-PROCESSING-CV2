import cv2
img = cv2.imread("img.jpg")
resized_img = cv2.resize(img, (400, 600))

ImgGray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
ImgBlur = cv2.GaussianBlur(ImgGray, (99, 99), 0)

cv2.imshow("Gray Img", ImgGray)
cv2.imshow("Original Img", resized_img)
cv2.imshow("Blur Img", ImgBlur)
cv2.waitKey(0)