import os
from flask import Flask, render_template, request, redirect, url_for, Blueprint
from werkzeug import secure_filename
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
import numpy as np
import argparse
import imutils
import cv2
#import time
import uuid
import base64
import tensorflow as tf
global graph,model
# from flask_wtf import CsrfProtect

ml = Blueprint('ml', __name__, template_folder='templates')


graph = tf.get_default_graph()

img_width, img_height = 150, 150
model_path = './snakeeyes/static/models/model.h5'
model_weights_path = './snakeeyes/static/models/weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

UPLOAD_FOLDER = 'snakeeyes/static/images/uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

def predict(file):
    x = load_img(file, target_size=(img_width,img_height))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    
    with graph.as_default():
        array = model.predict(x)
        
    result = array[0]
    answer = np.argmax(result)
    if answer == 0:
        print("Label: Daisy")
    elif answer == 1:
        print("Label: Rose")
    elif answer == 2:
        print("Label: Sunflower")
    return answer

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@ml.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method=='GET':
        return render_template('ml/index.html', label='abc', imagesource='../static/images/assets/template2.jpg')

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
    elif request.method == 'POST':
        #import time
        #start_time = time.time()
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            result = predict(file_path)
            if result == 0:
                label = 'Daisy'
            elif result == 1:
                label = 'Rose'          
            elif result == 2:
                label = 'Sunflower'

            #Here is a test of custom blocks to pass
            if label == 'Sunflower':
                T10 = '../static/images/img/1/1.jpg'
                T11 = 'Floordepot'
                T12 = 'Trento Oak'
                T13 = 'EU2917'
                T14 = '6.50'
            elif label == 'Rose':
                T10 = '../static/images/img/10/CHAD_BLACKWOOD_EURO_X3.0_S4S_XTRA.jpg'
                T11 = 'Floordepot'
                T12 = 'Chad Blackwood'
                T13 = 'EU3375X'
                T14 = '8.50'
            elif label == 'Daisy':
                T10 = '../static/images/img/5/CHERRY_PRUNUS_EUROX_4.2_LOCKING.jpg'
                T11 = 'Floordepot'
                T12 = 'Cherry Prunus'
                T13 = 'EU4622'
                T14 = '14.50'
                
            print(result)
            print(file_path)
            filename = my_random_string(6) + filename
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            os.rename(file_path, os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #print("--- %s seconds ---" % str (time.time() - start_time))
            #print('./uploads/' + filename)
        return render_template('ml/index.html', label=label, imagesource='../static/images/uploads/' + filename, T10=T10, T11=T11, T12=T12, T13=T13, T14=T14)

##I have no idea what this file below does because it seems to work without it
from flask import send_from_directory

@app.route('/snakeeyes/static/images/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

from werkzeug import SharedDataMiddleware
app.add_url_rule('/snakeeyes/static/images/uploads/<filename>', 'uploaded_file',
                 build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/snakeeyes/static/images/uploads':  app.config['UPLOAD_FOLDER']
})

