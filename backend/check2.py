import cv2
import mysql.connector
from pyzbar.pyzbar import decode
def scan_qr_code(image_path):
    image = cv2.imread(image_path)
    decoded_objects = decode(image)
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    else:
        return None




def search_database(id):
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

        cursor.execute('SELECT * FROM data WHERE id=%s',(id,))
        data = cursor.fetchall()
        print("Name : ",status[0],"\nId :", status[1], "\nContact : ",status[2])
    else:
        print("not found")


if __name__ == "__main__":
    qr_image_path = "16.png"  # Assuming the QR code image is in the same directory

    decoded_data = scan_qr_code(qr_image_path)
    search_database(decoded_data)

    if decoded_data is not None:
        print("Decoded successfully")
    else:
        print("QR code not detected or couldn't be decoded.")



