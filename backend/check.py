
import mysql.connector
from pyzbar.pyzbar import decode
from PIL import Image



def scan_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    else:
        return None

def split_qr_data(qr_data):
    components = qr_data.split('\n')
    name,id, contact = "", "", ""
    for component in components:
        parts = component.split(': ')
        if len(parts) == 2:
            key, value = parts
            if key == "name":
                name = value
            elif key == "id":
                id = value
            elif key == "contact":
                contact = value


    print(name)
    search_database(name,id,contact)
    return name, id, contact


def search_database(name,id,contact):
    db = mysql.connector.connect(
        host='localhost',
        user='vikram',  # Replace with your MySQL username
        password='vikram',  # Replace with your MySQL password
        database='qrcode',  # Replace with the name of the MySQL database you created
    )

    cursor = db.cursor()
    cursor.execute('SELECT * FROM data WHERE id=%s',(id,))
    status = cursor.fetchone()

    if status:
        print("user found")
    else:
        print("not found")




if __name__ == "__main__":
    qr_image_path = "multi_line_data_qr.png"  # Assuming the QR code image is in the same directory

    decoded_data = scan_qr_code(qr_image_path)
    split_qr_data(decoded_data)
    if decoded_data is not None:  # Check if decoding was successful
        print( decoded_data)

    else:
        print("QR code not detected or couldn't be decoded.")