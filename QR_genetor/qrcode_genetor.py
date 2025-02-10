import qrcode

# Generate a simple QR code
img = qrcode.make("www.linkedin.com/in/pankaj-verma-b73930273")
img.save("LinkedIn.png")