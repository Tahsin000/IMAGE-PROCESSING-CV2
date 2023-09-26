# Real-time Face Detection using OpenCV

**Description:**

This Python code demonstrates real-time face detection using OpenCV. It captures video from your webcam, processes each frame to detect faces, and draws rectangles around detected faces. You can exit the application by pressing the 'Esc' key (key code 27).

**Code Explanation:**

1. Import OpenCV:
   ```python
   import cv2
   ```

   This line imports the OpenCV library, which is used for computer vision and image processing tasks.

2. Load the Face Cascade Classifier:
   ```python
   faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
   ```

   This line loads a pre-trained Haar Cascade classifier for face detection. The XML file `"haarcascade_frontalface_default.xml"` contains the trained model for detecting frontal faces.

3. Video Capture Initialization (Using Webcam):
   ```python
   cap = cv2.VideoCapture(0)
   ```

   This line initializes video capture from the default webcam (index 0). You can adjust the index or provide a video file path to capture video from other sources.

4. Video Capture Loop:
   ```python
   while True:
   ```

   This creates an infinite loop that continuously captures and processes video frames.

5. Capture a Frame:
   ```python
   ret, img = cap.read()
   ```

   `cap.read()` reads a frame from the video source. The frame is stored in the `img` variable, and `ret` indicates whether the frame was successfully read.

6. Convert the Frame to Grayscale:
   ```python
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   ```

   The frame is converted to grayscale using `cv2.cvtColor()`, which simplifies face detection.

7. Detect Faces:
   ```python
   faces = faceCascade.detectMultiScale(img, 1.1, 4)
   ```

   `faceCascade.detectMultiScale()` detects faces in the grayscale frame. It returns a list of rectangles (x, y, width, height) that represent the detected faces.

8. Draw Rectangles around Detected Faces:
   ```python
   for (x, y, w, h) in faces:
       cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
   ```

   For each detected face, a blue rectangle is drawn around it using `cv2.rectangle()`.

9. Display the Video:
   ```python
   cv2.imshow("img", img)
   ```

   `cv2.imshow()` displays the current frame with detected faces in a window titled "img."

10. Exit on 'Esc' Key Press:
    ```python
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
    ```

    This part of the code waits for a key press using `cv2.waitKey()`. If the key pressed is the 'Esc' key (key code 27), the loop breaks, and the program exits.

11. Cleanup:
    ```python
    cap.release()
    cv2.destroyAllWindows()
    ```

    After exiting the loop, `cap.release()` releases the video capture object, and `cv2.destroyAllWindows()` closes all open windows.

**Note:**
- Ensure you have OpenCV installed.
- You can replace `"haarcascade_frontalface_default.xml"` with the path to your own Haar Cascade classifier XML file if needed.
- Make sure you have the necessary permissions to access your webcam.

This code can be a starting point for real-time face detection applications using OpenCV.