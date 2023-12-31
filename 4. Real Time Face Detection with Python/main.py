import cv2
faceCasCade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while True:
    nongare, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCasCade.detectMultiScale(img, 1.1, 4)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (225,0,0), 2)
        cv2.imshow("img", img)
        k = cv2.waitKey(30) & 0xFF
        if k == 27:
            break