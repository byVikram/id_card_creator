import qrcode

def generate_qr(id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(id)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    prefix = str(id)
    prefix = prefix + ".png"
    parent_path="D:\\qrreg\\backend\\qrphotos\\"
    original_path = parent_path + prefix
    qr_img.save(original_path)


