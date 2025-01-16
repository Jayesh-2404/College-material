import qrcode
data = "https://www.example.com"
qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=10,  # Size of each box in the QR Code grid
    border=4,  # Thickness of the border
)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")


img.save("qrcode.png")

print("QR Code generated and saved as qrcode.png")
