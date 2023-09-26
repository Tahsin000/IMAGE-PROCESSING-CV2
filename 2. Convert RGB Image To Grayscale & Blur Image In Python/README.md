## asic Image Processing with OpenCV: Resizing, Grayscale Conversion, and Gaussian Blur

1. Import OpenCV:

   ```python
   import cv2
   ```

   This line imports the OpenCV library, which is used for image processing and computer vision tasks.

2. Load an Image:

   ```python
   img = cv2.imread("img.jpg")
   ```

   This line loads an image from the file "img.jpg" into the `img` variable. The image is stored as a NumPy array, which allows you to perform various image processing operations.

3. Resize the Image:

   ```python
   resized_img = cv2.resize(img, (400, 600))
   ```

   Here, the `cv2.resize()` function is used to resize the loaded image to a new size of 400x600 pixels. The resized image is stored in the `resized_img` variable.

4. Convert the Image to Grayscale:

   ```python
   ImgGray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
   ```

   This line converts the resized image (`resized_img`) from a color image (BGR) to grayscale using `cv2.cvtColor()`. The resulting grayscale image is stored in the `ImgGray` variable.

5. Apply Gaussian Blur:

   ```python
   ImgBlur = cv2.GaussianBlur(ImgGray, (99, 99), 0)
   ```

   The `cv2.GaussianBlur()` function is applied to the grayscale image (`ImgGray`) to apply Gaussian smoothing. It blurs the image using a kernel size of (99, 99) and a standard deviation of 0. The resulting blurred image is stored in the `ImgBlur` variable.

6. Display Images:

   ```python
   cv2.imshow("Gray Img", ImgGray)
   cv2.imshow("Original Img", resized_img)
   cv2.imshow("Blur Img", ImgBlur)
   ```

   These lines use `cv2.imshow()` to display the three images: the grayscale image, the original resized image, and the blurred image. The window titles are specified as "Gray Img," "Original Img," and "Blur Img," respectively.

7. Wait for User Input and Close Windows:

   ```python
   cv2.waitKey(0)
   ```

   This line waits indefinitely for a key press (parameter 0) from the user. This allows you to view the displayed images until you decide to close them.

8. Cleanup:

   ```python
   cv2.destroyAllWindows()
   ```

   Finally, `cv2.destroyAllWindows()` is called to close all open image display windows when you're done viewing the images.

The code demonstrates basic image loading, resizing, conversion to grayscale, and Gaussian blur operations using OpenCV. It can be a starting point for more advanced image processing tasks.
