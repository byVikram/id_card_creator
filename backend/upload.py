import os

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def up(id):
    prefix = str(id)
    pic_name = prefix + "pic" + ".png"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
    print("saving file this message is from upload.py file")

id="3"
up(id)