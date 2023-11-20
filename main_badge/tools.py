import qrcode
# Data to be encoded
import config


def build_png_qr_code(data='https://www.linkedin.com/in/nectostr/', filename='linked_in.png'):
    # Encoding data using make() function
    qr = qrcode.QRCode(border=1)
    qr.add_data(data)
    qr.make()
    img = qr.make_image()
    img = img.resize((config.IMAGE_SIZE, config.IMAGE_SIZE))
    img.save(filename, 'PNG')


if __name__ == "__main__":
    build_png_qr_code(data="https://nectostr.github.io/", filename="website.png")