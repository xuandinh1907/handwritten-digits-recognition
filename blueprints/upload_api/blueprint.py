from flask import Blueprint, render_template, request
import tensorflow as tf
import numpy as np 
import re
import base64



model = tf.keras.models.load_model('models/my_model.h5')

def parse_image(imgData):
    img_str = re.search(b"base64,(.*)", imgData).group(1)
    img_decode = base64.decodebytes(img_str)
    with open('output.png', "wb") as f:
        f.write(img_decode)
    return img_decode

upload_api = Blueprint('upload_api', __name__)

@upload_api.route('/upload/',methods=['POST'])
def upload():
    image = parse_image(request.get_data())
    image = tf.image.decode_jpeg(image, channels=1)
    image = tf.image.resize(image, [28, 28])
    # Change background to black and normalize data
    image = (255 - image)/255.0
    image = tf.reshape(image, (1, 28, 28))

    prediction = model.predict(image)
    prediction = np.argmax(prediction, axis=1)
    return str(prediction)