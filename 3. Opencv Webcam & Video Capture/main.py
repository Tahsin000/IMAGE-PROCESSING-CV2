import cv2
# cap = cv2.VideoCapture("video.mp4") # if you can play video in your local pc
cap = cv2.VideoCapture(0) # if you can play video in your webcam
while True:
    nongarHub, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
