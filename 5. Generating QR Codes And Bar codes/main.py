import qrcode
QR = qrcode.make("Hello HHJN! ami hotash bolchi")
QR.save("QR code1.png")

qrForGit = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 10
)
link = "https://www.github.com/tahsin000"
qrForGit.add_data(link)
qrForGit.make(fit = True)

img = qrForGit.make_image(fill="black", back_color="white")
img.save("QR code2.png");