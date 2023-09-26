# QR Code Scanner

## Description
This Python script captures video frames from a camera feed and decodes QR codes present in the frames. When a QR code with new data is detected, it prints the data to the console. This script uses OpenCV for video capture and the `pyzbar` library for QR code decoding.

## Usage

1. **Installation**
   - Make sure you have Python installed on your system.
   - Install the required libraries using pip:
     ```
     pip install opencv-python-headless pyzbar
     ```

2. **Running the Script**
   - Clone this repository or download the script.
   - Open your terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using the following command:
     ```
     python qr_code_scanner.py
     ```

3. **Scanning QR Codes**
   - Point your camera at a QR code.
   - The script will continuously scan the camera feed for QR codes.
   - When a QR code with new data is detected, it will be printed to the console.
   - To exit the script, press the 'q' key.

## Dependencies
- Python 3.x
- OpenCV
- `pyzbar` library

