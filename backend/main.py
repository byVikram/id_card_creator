from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from badge import print_badge
from generator import generate_qr
import os


db = mysql.connector.connect(
    host='localhost',
    user='vikram',  # Replace with your MySQL username
    password='vikram',  # Replace with your MySQL password
    database='qrcode',  # Replace with the name of the MySQL database you created
)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

UPLOAD_FOLDER = 'profilephotos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/api/register', methods=['POST'])
def reg():

    name = request.form.get('fname')
    id = request.form.get('id')
    contact = request.form.get('contact')
    file=request.files['file']

    if file.filename == '':
        print("error in file")
    else:
        print("no error in file")

    if not name or not id or not contact:
        return jsonify({'message': 'Invalid data'}), 400

    cursor = db.cursor()
    cursor.execute('SELECT * FROM users WHERE id = %s ', (id,))
    status = cursor.fetchone()
    if status:
        return jsonify({'message': 'User already exist  '}), 200
    else:
        try:
            print("entered database")
            cursor.execute('INSERT INTO users (fname, id, contact) VALUES (%s, %s, %s)',
                           (name, id, contact))
            db.commit()
            #qr code start
            generate_qr(id)
            # Create a card template


            # profile image start
            prefix = str(id)
            pic_name=prefix+"pic"+".png"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
            print("saving file")
            # profile image end
            print_badge(name,id,contact)
            return jsonify({'fileUrl': "file uploaded"})

        except Exception as e:
            db.rollback()
            return jsonify({'fileUrl':"error"}), 500

if __name__ == '__main__':
    app.run(debug=True)