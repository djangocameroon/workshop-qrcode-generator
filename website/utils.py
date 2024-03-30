import io
import uuid

import qrcode
from django.core.files import File
from PIL import Image


def generate_uuid() -> str:
    return uuid.uuid4().hex


def generate_qrcode(information: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(information)
    qr.make(fit=True)
    qrcode_img = qr.make_image(fill_color="black", back_color="white")
    
    width, height = qrcode_img.size
    canvas_dim = 500
    x = (canvas_dim - width) / 2
    y = (canvas_dim - height) / 2
    
    canvas = Image.new("RGB", (canvas_dim, canvas_dim), "white")
    canvas.paste(qrcode_img, (int(x), int(y)))
    
    buffer = io.BytesIO()
    canvas.save(buffer, format="PNG")
    canvas.close()
    
    return File(buffer)
