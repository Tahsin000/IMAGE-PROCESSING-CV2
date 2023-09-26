import cv2
from pyzbar.pyzbar import decode

capture = cv2.VideoCapture(0);
recived_data = None
while True:
    success, frame = capture.read()

    decode_data = decode(frame)

    try:
        data = decode_data[0][0]
        if data != recived_data:
            print(data)
            recived_data = data
    except:
        pass
    cv2.imshow("QR code Scanner app", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
