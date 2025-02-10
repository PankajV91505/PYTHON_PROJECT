import qrcode
from PIL import Image

# Generate a simple QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data("www.linkedin.com/in/pankaj-verma-b73930273")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="purple")
img.save("LinkedIn_profile.png")