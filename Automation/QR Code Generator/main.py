# QR Code Generator...

import qrcode
import os

def qr_code(filename, data, dest="./qrcodes/"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=5,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="blue", back_color="white")

    if not os.path.exists(dest):
        os.makedirs(dest)   

    img.save(dest + filename + ".png")

if __name__ == "__main__":
    filename = "My Name"
    data = "Muhammad Abdullah Abrar"
    qr_code(filename, data)