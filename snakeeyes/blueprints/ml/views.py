import os
from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash
from werkzeug import secure_filename
# from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
# from keras.models import Sequential, load_model
import numpy as np
# import argparse
# import imutils
# import cv2
#import time
import uuid
import base64
# import tensorflow as tf
# global graph,model
# from flask_wtf import CsrfProtect

# Have to connect from from db folders
from snakeeyes.db.db_setup import init_db, db_session
# from snakeeyes.db.forms import VinylSearchForm
from snakeeyes.db.models import Album, Label
from snakeeyes.db.tables import Results

from colorthief import ColorThief
#for resizing
from PIL import Image

ml = Blueprint('ml', __name__, template_folder='templates')

@ml.route('/homepage')
def mlindex():
    T10 = '../static/images/img/1/TRENTO_OAK.jpg'
    return render_template('ml/index.html', imagesource='../static/images/assets/template2.jpg', T10=T10)
# graph = tf.get_default_graph()

# img_width, img_height = 150, 150
# model_path = './snakeeyes/static/models/model.h5'
# model_weights_path = './snakeeyes/static/models/weights.h5'
# model = load_model(model_path)
# model.load_weights(model_weights_path)

UPLOAD_FOLDER = 'snakeeyes/static/images/uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

# def predict(file):
#     x = load_img(file, target_size=(img_width,img_height))
#     x = img_to_array(x)
#     x = np.expand_dims(x, axis=0)
    
#     with graph.as_default():
#         array = model.predict(x)
        
#     result = array[0]
#     answer = np.argmax(result)
#     if answer == 0:
#         print("Label: Daisy")
#     elif answer == 1:
#         print("Label: Rose")
#     elif answer == 2:
#         print("Label: Sunflower")
#     return answer

def my_random_string(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# dominant colour function
def find_nearest_vector(array, value):
  idx = np.array([np.linalg.norm(x+y+z) for (x,y,z) in array-value]).argmin()
  return array[idx]
    
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@ml.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method=='GET':
        # results = []
        # search_string = 'asd'

        # qry = db_session.query(Album, Label).filter(
        #     Label.id==Album.label_id).filter(
        #         Label.name.contains(search_string))
        # results = [item[0] for item in qry.all()]

        # table = Results(results)

        # T10 = '../static/images/img/1/TRENTO_OAK.jpg'
        # T20 = '../static/images/img/1/TRENTO_OAK.jpg'
        # T30 = '../static/images/img/1/TRENTO_OAK.jpg'
        # T40 = '../static/images/img/1/TRENTO_OAK.jpg'
        # T50 = '../static/images/img/1/TRENTO_OAK.jpg'
        # T60 = '../static/images/img/1/TRENTO_OAK.jpg'
        return render_template('ml/index.html', label='', imagesource='../static/images/assets/template2.jpg')

    elif request.method == 'POST':
        T10 = '../static/images/img/1/TRENTO_OAK.jpg'
        

    #     #import time
    #     #start_time = time.time()
        file = request.files['file']

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            filename = my_random_string(6) + filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # In case size exceed 1500, reduce it.
            MAX_SIZE = 1500
            image = Image.open(file_path)
            original_size = max(image.size[0], image.size[1])
            if original_size >= MAX_SIZE:
                resized_file = open(file_path)
                basewidth = MAX_SIZE
                wpercent = (basewidth/float(image.size[0]))
                hsize = int((float(image.size[1])*float(wpercent)))
                image = image.resize((basewidth,hsize), Image.ANTIALIAS)
                image.save(file_path) 

            # Crop image to focus on flooring area only
            try:
                Image.open(file_path).convert('RGB').save(file_path)
                img = Image.open(file_path) 
                width, height = img.size 
                  
                area = (width/4, height/2.5, width/1.2, height/1) #(left, top, right, bottom) tweak 'top' to adjust how much to crop down. Currently cropping at 70%.
                img = img.crop(area) 
                  
                #Saved in the same relative location 
                img.save(file_path)
            except:
                Image.open(file_path).convert('RGB').save(file_path)
                img = Image.open(file_path) 
                width, height = img.size 
                  
                area = (width/4, height/2.5, width/1.2, height/1) #(left, top, right, bottom) tweak 'top' to adjust how much to crop down. Currently cropping at 70%.
                img = img.crop(area) 
                  
                #Saved in the same relative location 
                img.save(file_path)
            #get dominant colour
            color_thief = ColorThief(file_path)
            dominant_color = color_thief.get_color(quality=1)
            DC = ('rgb'+ str(dominant_color)) #get dominant colour for template page
            # a = [(172, 156, 114), (121, 71, 30), (181, 170, 148), (170, 156, 127), (50, 34, 25), (109, 63, 40), (129, 89, 57), (153, 148, 120), (144, 137, 112), (149, 135, 108), (134, 119, 90), (142, 117, 91), (139, 118, 87), (143, 118, 81), (143, 119, 85), (134, 108, 72), (136, 108, 67), (153, 125, 82), (74, 53, 36), (123, 107, 85), (135, 84, 46), (130, 101, 65), (66, 51, 37), (141, 93, 54), (93, 65, 43), (156, 103, 55), (134, 101, 61), (30, 27, 22), (169, 132, 88), (178, 125, 76), (92, 78, 65), (72, 52, 39), (169, 143, 110), (166, 144, 106), (129, 90, 55), (37, 31, 25), (141, 98, 53), (112, 97, 73), (106, 54, 30), (102, 96, 81), (139, 101, 68), (149, 102, 61), (153, 111, 76), (103, 73, 45), (123, 72, 47), (110, 89, 67), (113, 99, 76), (143, 97, 56), (205, 178, 136), (91, 62, 41),(183, 186, 192)] # this is wood colour rbg code
            a = [(172, 156, 114), (181, 170, 148), (170, 156, 127), (153, 148, 120), (144, 137, 112), (149, 135, 108), (134, 119, 90), (142, 117, 91), (139, 118, 87), (143, 118, 81), (143, 119, 85), (134, 108, 72), (136, 108, 67), (153, 125, 82), (74, 53, 36), (123, 107, 85), (135, 84, 46), (130, 101, 65), (66, 51, 37), (141, 93, 54), (93, 65, 43), (156, 103, 55), (134, 101, 61), (30, 27, 22), (169, 132, 88), (178, 125, 76), (92, 78, 65), (72, 52, 39), (169, 143, 110), (37, 31, 25), (141, 98, 53), (112, 97, 73), (106, 54, 30), (102, 96, 81), (139, 101, 68), (149, 102, 61), (153, 111, 76), (103, 73, 45), (123, 72, 47), (110, 89, 67), (113, 99, 76), (143, 97, 56), (205, 178, 136), (91, 62, 41), (183, 186, 192),(190, 188, 186)] # this is wood colour rbg code
            A = np.array(a)# turn array'a' into numpy
            wood = ['Oak Falcata', 'Prato Oak', 'France Maple', 'Balsa Wood', 'Tulepo Wood', 'Spruce Omorika', 'Eastern Hemlock', 'Black Wood', 'Box Elder', 'Hazel Plum', 'Plum Dosato', 'Sessile Oak', 'Thai Teak', 'Oak Espana', 'Albizia Wood', 'Amarello Wood', 'Amazique Wood', 'Ambrosia Cedar', 'Anzio Chestnut', 'Bali Teak', 'Berlinia Wood', 'Canary Wood', 'Catalpa Wood', 'Chad Blackwood', 'Cherry Wood', 'Cherry Prunus', 'Chestnut Africa', 'Black Palm', 'Fano Oak', 'Hormigo Wood', 'Jabillo Glory', 'Laurel Oak', 'Macacauba Wood', 'Mountain Ash', 'Movingui Wood', 'Oak Corilona', 'Pavia Cherry', 'Rhodesian Teak', 'Romania Alder', 'Scafiti Walnut', 'Southern Magnolia', 'Teak Madura', 'Trento Oak', 'Walnut Mimosa', 'Oxidized Wood', 'Pale Oak'] # this is wood type in accordance to code
            pricelist = [14.5, 16.5, 8.0, 6.5, 15.5, 14.5, 13.5, 6.0, 15.5, 8.0, 8.0, 13.5, 8.0, 14.5, 15.5, 6.5, 6.5, 8.0, 6.5, 8.0, 6.5, 15.5, 6.5, 8.0, 6.0, 14.5, 14.5, 8.0, 6.5, 15.5, 13.5, 13.5, 15.5, 8.0, 6.5, 8.0, 6.5, 13.5, 8.0, 6.5, 13.5, 8.0, 6.5, 14.5, 6.0, 6.0]
            codelist = ['EU4196', 'EU2910', 'EU3327X', 'EU2008', 'EU5424', 'EU4114', 'EU4907M', 'EU2291', 'EU5442', 'EU3371X', 'EU3202', 'EU4681M', 'EU3384X', 'EU4361', 'EU5629', 'EU2007', 'EU2011', 'EU3026', 'EU2396', 'EU3386X', 'EU2001', 'EU5077', 'EU2006', 'EU3375X', 'EU2341', 'EU4622', 'EU4443', 'EU3006', 'EU2915', 'EU5433', 'EU4232M', 'EU4683M', 'EU5541', 'EU3025', 'EU2010', 'EU3092', 'EU2394', 'EU4031M', 'EU3334X', 'EU2399', 'EU4104M', 'EU3084M', 'EU2917', 'EU4153', '16285', '']
            thicknesslist = [4.0, 2.0, 3.0, 2.0, 5.0, 4.0, 4.0, 2.0, 5.0, 3.0, 3.0, 4.0, 3.0, 4.0, 5.0, 2.0, 2.0, 3.0, 2.0, 3.0, 2.0, 5.0, 2.0, 3.0, 2.0, 4.0, 4.0, 3.0, 2.0, 5.0, 4.0, 4.0, 5.0, 3.0, 2.0, 3.0, 2.0, 4.0, 3.0, 2.0, 4.0, 3.0, 2.0, 4.0, 3.0,2]
            speclist = [2.0, 3.0, 6.0, 3.0, 4.0, 2.0, 8.0, 3.0, 4.0, 1.0, 9.0, 8.0, 6.0, 2.0, 4.0, 3.0, 3.0, 9.0, 3.0, 6.0, 3.0, 4.0, 3.0, 6.0, 3.0, 2.0, 2.0, 9.0, 3.0, 4.0, 8.0, 8.0, 4.0, 9.0, 3.0, 1.0, 3.0, 8.0, 6.0, 3.0, 8.0, 10.0, 3.0, 2.0, 9.0, 0]
            # wood = ['Oak Falcata', 'Burmese Teak', 'Prato Oak', 'France Maple', 'Black Acacia', 'Burma Paduak', 'Afomosia Wood', 'Balsa Wood', 'Tulepo Wood', 'Spruce Omorika', 'Eastern Hemlock', 'Black Wood', 'Box Elder', 'Hazel Plum', 'Plum Dosato', 'Sessile Oak', 'Thai Teak', 'Oak Espana', 'Albizia Wood', 'Amarello Wood', 'Amazique Wood', 'Ambrosia Cedar', 'Anzio Chestnut', 'Bali Teak', 'Berlinia Wood', 'Canary Wood', 'Catalpa Wood', 'Chad Blackwood', 'Cherry Wood', 'Cherry Prunus', 'Chestnut Africa', 'Black Palm', 'Fano Oak', 'Fineline Spring', 'Fineline Summer', 'Hormigo Wood', 'Jabillo Glory', 'Laurel Oak', 'Macacauba Wood', 'Mountain Ash', 'Movingui Wood', 'Oak Corilona', 'Pavia Cherry', 'Rhodesian Teak', 'Romania Alder', 'Scafiti Walnut', 'Southern Magnolia', 'Teak Madura', 'Trento Oak', 'Walnut Mimosa', 'Oxidized Wood'] # this is wood type in accordance to code
            # pricelist = [14.5, 14.0, 6.5, 8.0, 18.0, 18.0, 17.0, 6.5, 15.5, 14.5, 13.5, 6.0, 15.5, 8.0, 8.0, 13.5, 8.0, 14.5, 15.5, 6.5, 6.5, 8.0, 6.5, 8.0, 6.5, 15.5, 6.5, 8.0, 6.0, 14.5, 14.5, 8.0, 6.5, 6.5, 6.5, 15.5, 13.5, 13.5, 15.5, 8.0, 6.5, 8.0, 6.5, 13.5, 8.0, 6.5, 13.5, 8.0, 6.5, 14.5, 2.6]
            # codelist = ['EU4196', '2G-S2711RC', 'EU2910', 'EU3327X', '4G-H7053S', '4G-H7054S', '4G-H7726X', 'EU2008', 'EU5424', 'EU4114', 'EU4907M', 'EU2291', 'EU5442', 'EU3371X', 'EU3202', 'EU4681M', 'EU3384X', 'EU4361', 'EU5629', 'EU2007', 'EU2011', 'EU3026', 'EU2396', 'EU3386X', 'EU2001', 'EU5077', 'EU2006', 'EU3375X', 'EU2341', 'EU4622', 'EU4443', 'EU3006', 'EU2915', 'EU2621', 'EU2623', 'EU5433', 'EU4232M', 'EU4683M', 'EU5541', 'EU3025', 'EU2010', 'EU3092', 'EU2394', 'EU4031M', 'EU3334X', 'EU2399', 'EU4104M', 'EU3084M', 'EU2917', 'EU4153', '16285']
            # thicknesslist = [4.0, 2.0, 2.0, 3.0, 4.0, 4.0, 4.0, 2.0, 5.0, 4.0, 4.0, 2.0, 5.0, 3.0, 3.0, 4.0, 3.0, 4.0, 5.0, 2.0, 2.0, 3.0, 2.0, 3.0, 2.0, 5.0, 2.0, 3.0, 2.0, 4.0, 4.0, 3.0, 2.0, 2.0, 2.0, 5.0, 4.0, 4.0, 5.0, 3.0, 2.0, 3.0, 2.0, 4.0, 3.0, 2.0, 4.0, 3.0, 2.0, 4.0, 3.0]
            # speclist = [2.0, 5.0, 3.0, 6.0, 7.0, 7.0, 7.0, 3.0, 4.0, 2.0, 8.0, 3.0, 4.0, 1.0, 9.0, 8.0, 6.0, 2.0, 4.0, 3.0, 3.0, 9.0, 3.0, 6.0, 3.0, 4.0, 3.0, 6.0, 3.0, 2.0, 2.0, 9.0, 3.0, 3.0, 3.0, 4.0, 8.0, 8.0, 4.0, 9.0, 3.0, 1.0, 3.0, 8.0, 6.0, 3.0, 8.0, 10.0, 3.0, 2.0, 9.0]
            pt = dominant_color #this is the target image. Example (63, 52, 44)

            #print(str('The target image rbg is ')+str(pt))
            nearestvector = find_nearest_vector(A,pt)

            #print(A)

            nvlist = list(nearestvector) #convert to vector
            tnvlist = tuple(nvlist)
            #print(str('The closest rbg of the image is ')+str(tnvlist))
            #print(tnvlist)
            x1 = a.index(tnvlist) #get index from array of a
            #print(x)
            getwood = wood[x1]
            getprice = pricelist[x1]
            getcode = codelist[x1]
            getthickness = thicknesslist[x1]
            getspec = speclist[x1]
            #print('which is ' +str(getwood))
            #print('////////////////////////')

            #get second nearest colour wood
            del a[x1]
            del wood[x1]
            del pricelist[x1]
            del codelist[x1]
            del thicknesslist[x1]
            del speclist[x1]
            A = np.array(a)

            pttwo = np.array(pt)
            newpttwo = pttwo * 0.85 #adjust the no to raise/decrease the variables. Current optimal value is 0.85.
            newpttwoa = list(newpttwo)
            pttwo = tuple(newpttwoa)

            #print(str('The 2nd target image rbg is ')+str(pttwo))
            nearestvector = find_nearest_vector(A,pttwo)

            #print(A)

            nvlist = list(nearestvector)
            tnvlist = tuple(nvlist)
            #print(str('The 2nd closest rbg of the image is ')+str(tnvlist))
            #print(tnvlist)
            x2 = a.index(tnvlist)
            # if x2 == x1:
            #     a.remove(tnvlist)
            #     wood.remove(getwood)
            #     pricelist.remove(getprice)
            #     codelist.remove(getcode)
            #     thicknesslist.remove(getthickness)
            #     speclist.remove(getspec)
            #x2 = x2-1

            # if x1 == x2:
            #     a.remove(tnvlist)
            #     wood.remove(getwood)
            #     pricelist.remove(getprice)
            #     codelist.remove(getcode)
            #     thicknesslist.remove(getthickness)
            #     speclist.remove(getspec)
            
            #print(x)
            getwood2 = wood[x2]
            getprice2 = pricelist[x2]
            getcode2 = codelist[x2]
            getthickness2 = thicknesslist[x2]
            getspec2 = speclist[x2]
            #print('which is ' +str(getwood))

            #get third nearest colour wood
            del a[x2]
            del wood[x2]
            del pricelist[x2]
            del codelist[x2]
            del thicknesslist[x2]
            del speclist[x2]
            A = np.array(a)

            ptthree = np.array(pt)
            newptthree = ptthree * 1.15 #adjust the no as variable to how senstive. Current optimal value is 1.15.
            newptthreea = list(newptthree)
            ptthree = tuple(newptthreea)

            #print(str('The 3rd target image rbg is ')+str(ptthree))
            nearestvector = find_nearest_vector(A,ptthree)

            #print(A)

            nvlist = list(nearestvector)
            tnvlist = tuple(nvlist)
            #print(str('The 3rd closest rbg of the image is ')+str(tnvlist))
            #print(tnvlist)
            x3 = a.index(tnvlist)

            #print(x)
            getwood3 = wood[x3]
            getprice3 = pricelist[x3]
            getcode3 = codelist[x3]
            getthickness3 = thicknesslist[x3]
            getspec3 = [x3]

            # convert all to lowercase
            getwoodl = getwood.lower()
            getwoodl2 = getwood2.lower()
            getwoodl3 = getwood3.lower()
            # remove spacebar
            getwoodlink = getwoodl.replace(' ', '')
            getwoodlink2 = getwoodl2.replace(' ', '')
            getwoodlink3 = getwoodl3.replace(' ', '')

            #brands = "http://192.168.99.100:8000/ambrosiacedar"
            #print('which is ' +str(getwood))

            #////end of getting dominant colour////

    #         result = predict(file_path)
    #         if result == 0:
    #             label = 'Light Wood'
    #         elif result == 1:
    #             label = 'Brown Oaks'          
    #         elif result == 2:
    #             label = 'Black Chadwood'

            #display database from here
            # search = label
        # results = []
        # search_string = 'asd'

        # qry = db_session.query(Album, Label).filter(
        #     Label.id==Album.label_id).filter(
        #         Label.name.contains(search_string))
        # results = [item[0] for item in qry.all()]

        # table = Results(results)
        # table.border = False


    #         #Here is a test of custom blocks to pass
    #         if label == 'Light Wood':
    #             T10 = '../static/images/img/1/1.jpg'
    #             T11 = 'Floordepot'
    #             T12 = 'Trento Oak'
    #             T13 = 'EU2917'
    #             T14 = '6.50'
    #         elif label == 'Brown Oaks':
    #             T10 = '../static/images/img/10/CHAD_BLACKWOOD_EURO_X3.0_S4S_XTRA.jpg'
    #             T11 = 'Floordepot'
    #             T12 = 'Chad Blackwood'
    #             T13 = 'EU3375X'
    #             T14 = '8.50'
    #         elif label == 'Black Chadwood':
    #             T10 = '../static/images/img/5/CHERRY_PRUNUS_EUROX_4.2_LOCKING.jpg'
    #             T11 = 'Floordepot'
    #             T12 = 'Cherry Prunus'
    #             T13 = 'EU4622'
    #             T14 = '14.50'
                
    #         print(result)
    #         print(file_path)
            #filename = my_random_string(6) + filename
            #full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    #         os.rename(file_path, os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #print("--- %s seconds ---" % str (time.time() - start_time))
            #print('./uploads/' + filename)

        return render_template('ml/template.html',
         imagesource='../static/images/uploads/' + filename, 
         getwoodpic1='../static/images/img/all/' + getwood + '.jpg', 
          getwoodlink='http://192.168.99.100:8000/' + getwoodlink,
           T10=T10, DC=DC, getwood=getwood, getprice=getprice, getcode=getcode,
            getthickness=getthickness,getspec=getspec,
             getwoodpic2='../static/images/img/all/' + getwood2 + '.jpg',
             getwoodlink2='http://192.168.99.100:8000/' + getwoodlink2,
              getwood2=getwood2, getprice2=getprice2, getcode2=getcode2,
               getthickness2=getthickness2,getspec2=getspec2,
                getwoodpic3='../static/images/img/all/' + getwood3 + '.jpg',
                getwoodlink3='http://192.168.99.100:8000/' + getwoodlink3,
                 getwood3=getwood3, getprice3=getprice3, getcode3=getcode3,
                  getthickness3=getthickness3, getspec3=getspec3)
        #return render_template('ml/template.html', imagesource='../static/images/uploads/' + filename, T10=T10, DC=DC, getwood=getwood, getprice=getprice, getcode=getcode, getthickness=getthickness,getspec=getspec, getwood2=getwood2, getprice2=getprice2, getcode2=getcode2, getthickness2=getthickness2,getspec2=getspec2, getwood3=getwood3, getprice3=getprice3, getcode3=getcode3, getthickness3=getthickness3, getspec3=getspec3)
        # return render_template('ml/index.html', imagesource='../static/images/assets/template2.jpg')
        # return render_template('ml/index.html', label=label, imagesource='../static/images/uploads/' + filename, T10=T10, T11=T11, T12=T12, T13=T13, T14=T14)

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

# No caching at all for API endpoints. To prevent cache of duplicating images
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response