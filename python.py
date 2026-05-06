import qrcode
from IPython.display import display
qr = qrcode.QRCode(
    version=1,
    box_size=5,
    border=4,
)
qr.add_data('https://chatgpt.com')
qr.make(fit=True)

img = qr.make_image(fill_color="orange", back_color="white")
type(img)
img.save("MANU.png")
display(img)
