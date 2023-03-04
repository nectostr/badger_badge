import qrcode
# Data to be encoded
import config
data = 'https://www.linkedin.com/in/nectostr/'

# Encoding data using make() function
qr = qrcode.QRCode(border=0)
qr.add_data(data)
qr.make()
img = qr.make_image()
img = img.resize((config.IMAGE_SIZE, config.IMAGE_SIZE))
img.save('badge-image.png', 'PNG')
