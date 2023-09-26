## Generating QR Code for Text

### Description
To generate a QR code for text, you can use the following code. It will create a QR code containing the text "Hello HHJN! ami hotash bolchi" and save it as "QR code1.png."

```python
QR = qrcode.make("Hello HHJN! ami hotash bolchi")
QR.save("QR code1.png")
```


### Usage
1. Install the `qrcode` library if you haven't already:
   ```
   pip install qrcode[pil]
   ```

2. Run the provided code to generate a QR code for your desired text.

## Generating QR Code for a URL

### Description
To generate a QR code for a URL, you can use the following code. It creates a QR code for the URL "https://www.github.com/tahsin000" with custom settings and saves it as "QR code2.png."

```python
qrForGit = qrcode.QRCode(
    version=1,
    box_size=10,
    border=10
)
link = "https://www.github.com/tahsin000"
qrForGit.add_data(link)
qrForGit.make(fit=True)

img = qrForGit.make_image(fill="black", back_color="white")
img.save("QR code2.png")
```

### Usage
1. Install the `qrcode` library if you haven't already:
   ```
   pip install qrcode[pil]
   ```

2. Run the provided code to generate a QR code for your desired URL.
