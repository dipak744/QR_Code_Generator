from turtle import fillcolor
import qrcode
from PIL import Image
import qrcode.constants


qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4,)
qr.add_data("www.youtube.com/@dipak_sah")
qr.make(fit=True)
img=qr.make_image(fill_color="blue", back_color="white")
img.save("Dipak's_youtube.png")
