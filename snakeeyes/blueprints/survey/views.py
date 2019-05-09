from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField

survey = Blueprint('survey', __name__, template_folder='templates')

recommend = [('Residential', 'Living Room', 'Large', 'Bright', 'Bright', 'High'), ('Residential', 'Living Room', 'Large', 'Bright', 'Bright', 'Low'), ('Residential', 'Living Room', 'Large', 'Bright', 'Dark', 'High'), ('Residential', 'Living Room', 'Large', 'Bright', 'Dark', 'Low'), ('Residential', 'Living Room', 'Large', 'Dark', 'Bright', 'High'), ('Residential', 'Living Room', 'Large', 'Dark', 'Bright', 'Low'), ('Residential', 'Living Room', 'Large', 'Dark', 'Dark', 'High'), ('Residential', 'Living Room', 'Large', 'Dark', 'Dark', 'Low'), ('Residential', 'Living Room', 'Small', 'Bright', 'Bright', 'High'), ('Residential', 'Living Room', 'Small', 'Bright', 'Bright', 'Low'), ('Residential', 'Living Room', 'Small', 'Bright', 'Dark', 'High'), ('Residential', 'Living Room', 'Small', 'Bright', 'Dark', 'Low'), ('Residential', 'Living Room', 'Small', 'Dark', 'Bright', 'High'), ('Residential', 'Living Room', 'Small', 'Dark', 'Bright', 'Low'), ('Residential', 'Living Room', 'Small', 'Dark', 'Dark', 'High'), ('Residential', 'Living Room', 'Small', 'Dark', 'Dark', 'Low'),('Residential', 'Open Space', 'Large', 'Bright', 'Bright', 'High'), ('Residential', 'Open Space', 'Large', 'Bright', 'Bright', 'Low'), ('Residential', 'Open Space', 'Large', 'Bright', 'Dark', 'High'), ('Residential', 'Open Space', 'Large', 'Bright', 'Dark', 'Low'), ('Residential', 'Open Space', 'Large', 'Dark', 'Bright', 'High'), ('Residential', 'Open Space', 'Large', 'Dark', 'Bright', 'Low'), ('Residential', 'Open Space', 'Large', 'Dark', 'Dark', 'High'), ('Residential', 'Open Space', 'Large', 'Dark', 'Dark', 'Low'), ('Residential', 'Open Space', 'Small', 'Bright', 'Bright', 'High'), ('Residential', 'Open Space', 'Small', 'Bright', 'Bright', 'Low'), ('Residential', 'Open Space', 'Small', 'Bright', 'Dark', 'High'), ('Residential', 'Open Space', 'Small', 'Bright', 'Dark', 'Low'), ('Residential', 'Open Space', 'Small', 'Dark', 'Bright', 'High'), ('Residential', 'Open Space', 'Small', 'Dark', 'Bright', 'Low'), ('Residential', 'Open Space', 'Small', 'Dark', 'Dark', 'High'), ('Residential', 'Open Space', 'Small', 'Dark', 'Dark', 'Low'),('Residential', 'Bathroom', 'Large', 'Bright', 'Bright', 'High'), ('Residential', 'Bathroom', 'Large', 'Bright', 'Bright', 'Low'), ('Residential', 'Bathroom', 'Large', 'Bright', 'Dark', 'High'), ('Residential', 'Bathroom', 'Large', 'Bright', 'Dark', 'Low'), ('Residential', 'Bathroom', 'Large', 'Dark', 'Bright', 'High'), ('Residential', 'Bathroom', 'Large', 'Dark', 'Bright', 'Low'), ('Residential', 'Bathroom', 'Large', 'Dark', 'Dark', 'High'), ('Residential', 'Bathroom', 'Large', 'Dark', 'Dark', 'Low'), ('Residential', 'Bathroom', 'Small', 'Bright', 'Bright', 'High'), ('Residential', 'Bathroom', 'Small', 'Bright', 'Bright', 'Low'), ('Residential', 'Bathroom', 'Small', 'Bright', 'Dark', 'High'), ('Residential', 'Bathroom', 'Small', 'Bright', 'Dark', 'Low'), ('Residential', 'Bathroom', 'Small', 'Dark', 'Bright', 'High'), ('Residential', 'Bathroom', 'Small', 'Dark', 'Bright', 'Low'), ('Residential', 'Bathroom', 'Small', 'Dark', 'Dark', 'High'), ('Residential', 'Bathroom', 'Small', 'Dark', 'Dark', 'Low'),('Residential', 'Kitchen', 'Large', 'Bright', 'Bright', 'High'), ('Residential', 'Kitchen', 'Large', 'Bright', 'Bright', 'Low'), ('Residential', 'Kitchen', 'Large', 'Bright', 'Dark', 'High'), ('Residential', 'Kitchen', 'Large', 'Bright', 'Dark', 'Low'), ('Residential', 'Kitchen', 'Large', 'Dark', 'Bright', 'High'), ('Residential', 'Kitchen', 'Large', 'Dark', 'Bright', 'Low'), ('Residential', 'Kitchen', 'Large', 'Dark', 'Dark', 'High'), ('Residential', 'Kitchen', 'Large', 'Dark', 'Dark', 'Low'), ('Residential', 'Kitchen', 'Small', 'Bright', 'Bright', 'High'), ('Residential', 'Kitchen', 'Small', 'Bright', 'Bright', 'Low'), ('Residential', 'Kitchen', 'Small', 'Bright', 'Dark', 'High'), ('Residential', 'Kitchen', 'Small', 'Bright', 'Dark', 'Low'), ('Residential', 'Kitchen', 'Small', 'Dark', 'Bright', 'High'), ('Residential', 'Kitchen', 'Small', 'Dark', 'Bright', 'Low'), ('Residential', 'Kitchen', 'Small', 'Dark', 'Dark', 'High'), ('Residential', 'Kitchen', 'Small', 'Dark', 'Dark', 'Low'),('Commercial', 'Living Room', 'Large', 'Bright', 'Bright', 'High'), ('Commercial', 'Living Room', 'Large', 'Bright', 'Bright', 'Low'), ('Commercial', 'Living Room', 'Large', 'Bright', 'Dark', 'High'), ('Commercial', 'Living Room', 'Large', 'Bright', 'Dark', 'Low'), ('Commercial', 'Living Room', 'Large', 'Dark', 'Bright', 'High'), ('Commercial', 'Living Room', 'Large', 'Dark', 'Bright', 'Low'), ('Commercial', 'Living Room', 'Large', 'Dark', 'Dark', 'High'), ('Commercial', 'Living Room', 'Large', 'Dark', 'Dark', 'Low'), ('Commercial', 'Living Room', 'Small', 'Bright', 'Bright', 'High'), ('Commercial', 'Living Room', 'Small', 'Bright', 'Bright', 'Low'), ('Commercial', 'Living Room', 'Small', 'Bright', 'Dark', 'High'), ('Commercial', 'Living Room', 'Small', 'Bright', 'Dark', 'Low'), ('Commercial', 'Living Room', 'Small', 'Dark', 'Bright', 'High'), ('Commercial', 'Living Room', 'Small', 'Dark', 'Bright', 'Low'), ('Commercial', 'Living Room', 'Small', 'Dark', 'Dark', 'High'), ('Commercial', 'Living Room', 'Small', 'Dark', 'Dark', 'Low'),('Commercial', 'Open Space', 'Large', 'Bright', 'Bright', 'High'), ('Commercial', 'Open Space', 'Large', 'Bright', 'Bright', 'Low'), ('Commercial', 'Open Space', 'Large', 'Bright', 'Dark', 'High'), ('Commercial', 'Open Space', 'Large', 'Bright', 'Dark', 'Low'), ('Commercial', 'Open Space', 'Large', 'Dark', 'Bright', 'High'), ('Commercial', 'Open Space', 'Large', 'Dark', 'Bright', 'Low'), ('Commercial', 'Open Space', 'Large', 'Dark', 'Dark', 'High'), ('Commercial', 'Open Space', 'Large', 'Dark', 'Dark', 'Low'), ('Commercial', 'Open Space', 'Small', 'Bright', 'Bright', 'High'), ('Commercial', 'Open Space', 'Small', 'Bright', 'Bright', 'Low'), ('Commercial', 'Open Space', 'Small', 'Bright', 'Dark', 'High'), ('Commercial', 'Open Space', 'Small', 'Bright', 'Dark', 'Low'), ('Commercial', 'Open Space', 'Small', 'Dark', 'Bright', 'High'), ('Commercial', 'Open Space', 'Small', 'Dark', 'Bright', 'Low'), ('Commercial', 'Open Space', 'Small', 'Dark', 'Dark', 'High'), ('Commercial', 'Open Space', 'Small', 'Dark', 'Dark', 'Low'),('Commercial', 'Bathroom', 'Large', 'Bright', 'Bright', 'High'), ('Commercial', 'Bathroom', 'Large', 'Bright', 'Bright', 'Low'), ('Commercial', 'Bathroom', 'Large', 'Bright', 'Dark', 'High'), ('Commercial', 'Bathroom', 'Large', 'Bright', 'Dark', 'Low'), ('Commercial', 'Bathroom', 'Large', 'Dark', 'Bright', 'High'), ('Commercial', 'Bathroom', 'Large', 'Dark', 'Bright', 'Low'), ('Commercial', 'Bathroom', 'Large', 'Dark', 'Dark', 'High'), ('Commercial', 'Bathroom', 'Large', 'Dark', 'Dark', 'Low'), ('Commercial', 'Bathroom', 'Small', 'Bright', 'Bright', 'High'), ('Commercial', 'Bathroom', 'Small', 'Bright', 'Bright', 'Low'), ('Commercial', 'Bathroom', 'Small', 'Bright', 'Dark', 'High'), ('Commercial', 'Bathroom', 'Small', 'Bright', 'Dark', 'Low'), ('Commercial', 'Bathroom', 'Small', 'Dark', 'Bright', 'High'), ('Commercial', 'Bathroom', 'Small', 'Dark', 'Bright', 'Low'), ('Commercial', 'Bathroom', 'Small', 'Dark', 'Dark', 'High'), ('Commercial', 'Bathroom', 'Small', 'Dark', 'Dark', 'Low'),('Commercial', 'Kitchen', 'Large', 'Bright', 'Bright', 'High'), ('Commercial', 'Kitchen', 'Large', 'Bright', 'Bright', 'Low'), ('Commercial', 'Kitchen', 'Large', 'Bright', 'Dark', 'High'), ('Commercial', 'Kitchen', 'Large', 'Bright', 'Dark', 'Low'), ('Commercial', 'Kitchen', 'Large', 'Dark', 'Bright', 'High'), ('Commercial', 'Kitchen', 'Large', 'Dark', 'Bright', 'Low'), ('Commercial', 'Kitchen', 'Large', 'Dark', 'Dark', 'High'), ('Commercial', 'Kitchen', 'Large', 'Dark', 'Dark', 'Low'), ('Commercial', 'Kitchen', 'Small', 'Bright', 'Bright', 'High'), ('Commercial', 'Kitchen', 'Small', 'Bright', 'Bright', 'Low'), ('Commercial', 'Kitchen', 'Small', 'Bright', 'Dark', 'High'), ('Commercial', 'Kitchen', 'Small', 'Bright', 'Dark', 'Low'), ('Commercial', 'Kitchen', 'Small', 'Dark', 'Bright', 'High'), ('Commercial', 'Kitchen', 'Small', 'Dark', 'Bright', 'Low'), ('Commercial', 'Kitchen', 'Small', 'Dark', 'Dark', 'High'), ('Commercial', 'Kitchen', 'Small', 'Dark', 'Dark', 'Low')]
series = [('Elder Brilliance', 'Earth Valley'),('Light Adolescence', 'Dark Chocolate'),('Cherry Passion', 'Supreme Wood'),('Timeless Wisdom', 'Dark Chocolate'),('Solid Wood'),('Light Adolescence'),('Solid Wood'),('Light Adolescence'),('Elder Brilliance'),('Light Adolescence'),('Red Inspire'),('Earth Valley'),('Elder Brilliance'),('Light Adolescence'),('Gentlemens Leather'),('Elder Brilliance'),('Elder Brilliance'),('Supreme Wood'),('Cherry Passion'),('Timeless Wisdom'),('Solid Wood'),('Light Adolescence'),('Solid Wood'),('Light Adolescence'),('Elder Brilliance'),('Light Adolescence'),('Red Inspire'),('Earth Valley'),('Elder Brilliance'),('Light Adolescence'),('Gentlemens Leather'),('Elder Brilliance'),('Timeless Wisdom', 'Dark Chocolate'),('Earth Valley', 'Timeless Wisdom'),('Timeless Wisdom', 'Dark Chocolate'),('Earth Valley', 'Timeless Wisdom'),('Earth Valley', 'Timeless Wisdom'),('Elder Brilliance'),('Earth Valley', 'Timeless Wisdom'),('Elder Brilliance'),('Timeless Wisdom', 'Dark Chocolate'),('Earth Valley', 'Timeless Wisdom'),('Timeless Wisdom', 'Dark Chocolate'),('Earth Valley', 'Timeless Wisdom'),('Earth Valley', 'Timeless Wisdom'),('Elder Brilliance'),('Earth Valley', 'Timeless Wisdom'),('Elder Brilliance'),('Gentlemens Leather','Earth Valley'),('Elder Brilliance','Solid Wood'),('Elder Brilliance','Solid Wood'),('Light Adolescence'),('Earth Valley','Dark Chocolate'),('Elder Brilliance'),('Solid Wood','Gentlemens Leather'),('Light Adolescence','Elder Brilliance'),('Gentlemens Leather','Earth Valley'),('Light Adolescence','Solid Wood'),('Elder Brilliance','Solid Wood'),('Light Adolescence'),('Earth Valley','Dark Chocolate'),('Elder Brilliance'),('Solid Wood','Gentlemens Leather'),('Light Adolescence','Elder Brilliance'),('Elder Brilliance','Red Inspire'),('Supreme Wood','Dark Chocolate'),('Cherry Passion','Supreme Wood'),('Timeless Wisdom','Dark Chocolate'),('Solid Wood'),('Light Adolescence'),('Solid Wood'),('Light Adolescence'),('Elder Brilliance'),('Light Adolescence'),('Red Inspire'),('Earth Valley'),('Elder Brilliance'),('Light Adolescence'),('Gentlemens Leather'),('Elder Brilliance'),('Elder Brilliance','Red Inspire'),('Supreme Wood','Dark Chocolate'),('Cherry Passion','Supreme Wood'),('Timeless Wisdom','Dark Chocolate'),('Solid Wood'),('Light Adolescence'),('Solid Wood'),('Light Adolescence'),('Elder Brilliance'),('Light Adolescence'),('Red Inspire'),('Earth Valley'),('Elder Brilliance'),('Light Adolescence'),('Gentlemens Leather'),('Elder Brilliance'),('Elder Brilliance','Red Inspire'),('Supreme Wood','Dark Chocolate'),('Cherry Passion','Supreme Wood'),('Timeless Wisdom','Dark Chocolate'),('Solid Wood'),('Light Adolescence'),('Solid Wood'),('Light Adolescence'),('Elder Brilliance'),('Light Adolescence'),('Red Inspire'),('Earth Valley'),('Elder Brilliance'),('Light Adolescence'),('Gentlemens Leather'),('Elder Brilliance'),('Gentlemens Leather','Earth Valley'),('Elder Brilliance','Solid Wood'),('Elder Brilliance','Solid Wood'),('Light Adolescence'),('Earth Valley','Dark Chocolate'),('Elder Brilliance'),('Solid Wood','Gentlemens Leather'),('Light Adolescence','Elder Brilliance'),('Gentlemens Leather','Earth Valley'),('Light Adolescence','Solid Wood'),('Elder Brilliance','Solid Wood'),('Light Adolescence'),('Earth Valley','Dark Chocolate'),('Elder Brilliance'),('Solid Wood','Gentlemens Leather'),('Light Adolescence','Elder Brilliance')]
#series = [('EB', 'EV'),('SW', 'DC'),('CP', 'SW'),('TW', 'DC'),('SO'),('LA'),('SO'),('LA'),('EB'),('LA'),('RI'),('EV'),('EB'),('LA'),('GL'),('EB'),('EB'),('SW'),('CP'),('TW'),('SO'),('LA'),('SO'),('LA'),('EB'),('LA'),('RI'),('EV'),('EB'),('LA'),('GL'),('EB'),('TW', 'DC'),('EV', 'TW'),('TW', 'DC'),('EV', 'TW'),('EV', 'TW'),('EB'),('EV', 'TW'),('EB'),('TW', 'DC'),('EV', 'TW'),('TW', 'DC'),('EV', 'TW'),('EV', 'TW'),('EB'),('EV', 'TW'),('EB'),('GL','EV'),('EB','SO'),('EB','SO'),('LA'),('EV','DC'),('EB'),('SO','GL'),('LA','EB'),('GL','EV'),('LA','SO'),('EB','SO'),('LA'),('EV','DC'),('EB'),('SO','GL'),('LA','EB'),('EB','RI'),('SW','DC'),('CP','SW'),('TW','DC'),('SO'),('LA'),('SO'),('LA'),('EB'),('LA'),('RI'),('EV'),('EB'),('LA'),('GL'),('EB'),('EB','RI'),('SW','DC'),('CP','SW'),('TW','DC'),('SO'),('LA'),('SO'),('LA'),('EB'),('LA'),('RI'),('EV'),('EB'),('LA'),('GL'),('EB'),('EB','RI'),('SW','DC'),('CP','SW'),('TW','DC'),('SO'),('LA'),('SO'),('LA'),('EB'),('LA'),('RI'),('EV'),('EB'),('LA'),('GL'),('EB'),('GL','EV'),('EB','SO'),('EB','SO'),('LA'),('EV','DC'),('EB'),('SO','GL'),('LA','EB'),('GL','EV'),('LA','SO'),('EB','SO'),('LA'),('EV','DC'),('EB'),('SO','GL'),('LA','EB')]
LightAdolescence = ['Prato Oak','France Maple','Trento Oak','Oxidized Wood','paleoak','','','']
ElderBrilliance = ['Balsa Wood', 'Tulepo Wood', 'Spruce Omorika', 'Eastern Hemlock','Oak Falcata','','','']
SolidWood = ['BlackWood','Boxelder Wood','Hazel Plum','Plum Dosato','Sessile Oak','Thai Teak','Oak Espana','Fano Oak']
GentlemensLeather = ['Ambrosia Cedar','Catalpa Wood','Cherry Wood','Fineline Spring','Movingui Wood','','','']
CherryPassion = ['Canary Wood','Cherry Prunus','Jabillo Glory','Oak Corilona','','','',''] #omitted Pavia Cherry and Teak Madura
#CherryPassion = ['Canary Wood','Cherry Prunus','Jabillo Glory','Oak Corilona','Pavia Cherry','Teak Madura','',''] #full set of Cherry Passion
EarthValley = ['Amarello Wood','Laurel Oak','Mountain Ash','Scafiti Walnut','Southern Magnolia','','','']
RedInspire = ['Afomosia Wood','Amazique Wood','Bali Teak','Fineline Summer','Romania Alder','Macacauba Wood','','']
SupremeWood = ['','','Berlinia Wood','Rhodesian Teak','Walnut Mimosa','','','']
#SupremeWood = ['Burmese Teak','Burma Paduak','Berlinia Wood','Macacauba Wood','Rhodesian Teak','Walnut Mimosa','','']
TimelessWisdom = ['Albizia Wood','Anzio Chestnut','Black Palm','Chestnut Africa','','','','']
DarkChocolate = ['Black Acacia','Chad Blackwood','Hormigo Wood','','','','','']

getseriespic1= []

    
class QuizForm(FlaskForm):

    # questions and options
    Q1 = RadioField(
        '1. What will be the type of your property?', 
        choices=[('Residential','Residential'),('Commercial','Commercial')],
                 default='Residential'
        )

    Q2 = RadioField(
        '2. Where is the flooring?', 
        choices=[('Living Room','Living Room'),('Open Space','Open Space'),('Bathroom','Bathroom'),('Kitchen','Kitchen')],
                 default='Living Room'
        )

    Q3 = RadioField(
        '3. How big will your floor area be?', 
        choices=[('Large','Large'),('Small','Small')],
                 default='Large'
        )
    Q4 = RadioField(
        '4. What will your wall colour be?', 
        choices=[('Bright','Bright'),('Dark','Dark')],
                 default='Bright'
        )
    Q5 = RadioField(
        '5. What will your furniture colour be?', 
        choices=[('Bright','Bright'),('Dark','Dark')],
                 default='Bright'
        )
    Q6 = RadioField(
        '6. How will the traffic on your floor be?', 
        choices=[('High','High'),('Low','Low')],
                 default='High'
        )
    
    # submit button
    submit = SubmitField("Submit answers")


# indexing page with questions
@survey.route('/survey', methods=['GET','POST'])
def surveys():
    global LightAdolescence
    global ElderBrilliance
    global SolidOak
    global GentlemensLeather
    global CherryPassion
    global EarthValley
    global RedInspire
    global SupremeWood
    global TimelessWisdom   
    global DarkChocolate
    sv = []
    form = QuizForm()
    #if request.method == 'POST':

    # if the user submits answers
    if form.validate_on_submit():

        survey1 = form.Q1.data
        survey2 = form.Q2.data
        survey3 = form.Q3.data
        survey4 = form.Q4.data
        survey5 = form.Q5.data
        survey6 = form.Q6.data

        sv.append(survey1)
        sv.append(survey2)
        sv.append(survey3)
        sv.append(survey4)
        sv.append(survey5)
        sv.append(survey6)

        tsv = tuple(sv)

        recommendindex = recommend.index((tsv))
        getseries = series[recommendindex]
        if len(getseries)==2:
            getseries1 = getseries[0]
            getseries2 = getseries[1]
        else:
            getseries1 = getseries
            getseries2 = ''

        if getseries1 == 'Light Adolescence':
            #global getseriespic1
            getseriespic1 = LightAdolescence[0]
            getseriespic2 = LightAdolescence[1]
            getseriespic3 = LightAdolescence[2]
            getseriespic4 = LightAdolescence[3]
            getseriespic5 = LightAdolescence[4]
            getseriespic6 = LightAdolescence[5]
            getseriespic7 = LightAdolescence[6]
            getseriespic8 = LightAdolescence[7]
        elif getseries1 == 'Elder Brilliance':
            getseriespic1 = ElderBrilliance[0]
            getseriespic2 = ElderBrilliance[1]
            getseriespic3 = ElderBrilliance[2]
            getseriespic4 = ElderBrilliance[3]
            getseriespic5 = ElderBrilliance[4]
            getseriespic6 = ElderBrilliance[5]
            getseriespic7 = ElderBrilliance[6]
            getseriespic8 = ElderBrilliance[7]
        elif getseries1 == 'Solid Wood':
            getseriespic1 = SolidWood[0]
            getseriespic2 = SolidWood[1]
            getseriespic3 = SolidWood[2]
            getseriespic4 = SolidWood[3]
            getseriespic5 = SolidWood[4]
            getseriespic6 = SolidWood[5]
            getseriespic7 = SolidWood[6]
            getseriespic8 = SolidWood[7]
        elif getseries1 == 'Gentlemens Leather':
            getseriespic1 = GentlemensLeather[0]
            getseriespic2 = GentlemensLeather[1]
            getseriespic3 = GentlemensLeather[2]
            getseriespic4 = GentlemensLeather[3]
            getseriespic5 = GentlemensLeather[4]
            getseriespic6 = GentlemensLeather[5]
            getseriespic7 = GentlemensLeather[6]
            getseriespic8 = GentlemensLeather[7]
        elif getseries1 == 'Cherry Passion':
            getseriespic1 = CherryPassion[0]
            getseriespic2 = CherryPassion[1]
            getseriespic3 = CherryPassion[2]
            getseriespic4 = CherryPassion[3]
            getseriespic5 = CherryPassion[4]
            getseriespic6 = CherryPassion[5]
            getseriespic7 = CherryPassion[6]
            getseriespic8 = CherryPassion[7]
        elif getseries1 == 'Earth Valley':
            getseriespic1 = EarthValley[0]
            getseriespic2 = EarthValley[1]
            getseriespic3 = EarthValley[2]
            getseriespic4 = EarthValley[3]
            getseriespic5 = EarthValley[4]
            getseriespic6 = EarthValley[5]
            getseriespic7 = EarthValley[6]
            getseriespic8 = EarthValley[7]
        elif getseries1 == 'Red Inspire':
            getseriespic1 = RedInspire[0]
            getseriespic2 = RedInspire[1]
            getseriespic3 = RedInspire[2]
            getseriespic4 = RedInspire[3]
            getseriespic5 = RedInspire[4]
            getseriespic6 = RedInspire[5]
            getseriespic7 = RedInspire[6]
            getseriespic8 = RedInspire[7]
        elif getseries1 == 'Supreme Wood':
            getseriespic1 = SupremeWood[0]
            getseriespic2 = SupremeWood[1]
            getseriespic3 = SupremeWood[2]
            getseriespic4 = SupremeWood[3]
            getseriespic5 = SupremeWood[4]
            getseriespic6 = SupremeWood[5]
            getseriespic7 = SupremeWood[6]
            getseriespic8 = SupremeWood[7]
        elif getseries1 == 'Timeless Wisdom':
            getseriespic1 = TimelessWisdom[0]
            getseriespic2 = TimelessWisdom[1]
            getseriespic3 = TimelessWisdom[2]
            getseriespic4 = TimelessWisdom[3]
            getseriespic5 = TimelessWisdom[4]
            getseriespic6 = TimelessWisdom[5]
            getseriespic7 = TimelessWisdom[6]
            getseriespic8 = TimelessWisdom[7]
        elif getseries1 == 'Dark Chocolate':
            getseriespic1 = DarkChocolate[0]
            getseriespic2 = DarkChocolate[1]
            getseriespic3 = DarkChocolate[2]
            getseriespic4 = DarkChocolate[3]
            getseriespic5 = DarkChocolate[4]
            getseriespic6 = DarkChocolate[5]
            getseriespic7 = DarkChocolate[6]
            getseriespic8 = DarkChocolate[7]

        # get name
        if getseries1 == 'Light Adolescence':
            woodname1 = LightAdolescence[0]
            woodname2 = LightAdolescence[1]
            woodname3 = LightAdolescence[2]
            woodname4 = LightAdolescence[3]
            woodname5 = LightAdolescence[4]
            woodname6 = LightAdolescence[5]
            woodname7 = LightAdolescence[6]
            woodname8 = LightAdolescence[7]
        elif getseries1 == 'Elder Brilliance':
            woodname1 = ElderBrilliance[0]
            woodname2 = ElderBrilliance[1]
            woodname3 = ElderBrilliance[2]
            woodname4 = ElderBrilliance[3]
            woodname5 = ElderBrilliance[4]
            woodname6 = ElderBrilliance[5]
            woodname7 = ElderBrilliance[6]
            woodname8 = ElderBrilliance[7]
        elif getseries1 == 'Solid Wood':
            woodname1 = SolidWood[0]
            woodname2 = SolidWood[1]
            woodname3 = SolidWood[2]
            woodname4 = SolidWood[3]
            woodname5 = SolidWood[4]
            woodname6 = SolidWood[5]
            woodname7 = SolidWood[6]
            woodname8 = SolidWood[7]
        elif getseries1 == 'Gentlemens Leather':
            woodname1 = GentlemensLeather[0]
            woodname2 = GentlemensLeather[1]
            woodname3 = GentlemensLeather[2]
            woodname4 = GentlemensLeather[3]
            woodname5 = GentlemensLeather[4]
            woodname6 = GentlemensLeather[5]
            woodname7 = GentlemensLeather[6]
            woodname8 = GentlemensLeather[7]
        elif getseries1 == 'Cherry Passion':
            woodname1 = CherryPassion[0]
            woodname2 = CherryPassion[1]
            woodname3 = CherryPassion[2]
            woodname4 = CherryPassion[3]
            woodname5 = CherryPassion[4]
            woodname6 = CherryPassion[5]
            woodname7 = CherryPassion[6]
            woodname8 = CherryPassion[7]
        elif getseries1 == 'Earth Valley':
            woodname1 = EarthValley[0]
            woodname2 = EarthValley[1]
            woodname3 = EarthValley[2]
            woodname4 = EarthValley[3]
            woodname5 = EarthValley[4]
            woodname6 = EarthValley[5]
            woodname7 = EarthValley[6]
            woodname8 = EarthValley[7]
        elif getseries1 == 'Red Inspire':
            woodname1 = RedInspire[0]
            woodname2 = RedInspire[1]
            woodname3 = RedInspire[2]
            woodname4 = RedInspire[3]
            woodname5 = RedInspire[4]
            woodname6 = RedInspire[5]
            woodname7 = RedInspire[6]
            woodname8 = RedInspire[7]
        elif getseries1 == 'Supreme Wood':
            woodname1 = SupremeWood[0]
            woodname2 = SupremeWood[1]
            woodname3 = SupremeWood[2]
            woodname4 = SupremeWood[3]
            woodname5 = SupremeWood[4]
            woodname6 = SupremeWood[5]
            woodname7 = SupremeWood[6]
            woodname8 = SupremeWood[7]
        elif getseries1 == 'Timeless Wisdom':
            woodname1 = TimelessWisdom[0]
            woodname2 = TimelessWisdom[1]
            woodname3 = TimelessWisdom[2]
            woodname4 = TimelessWisdom[3]
            woodname5 = TimelessWisdom[4]
            woodname6 = TimelessWisdom[5]
            woodname7 = TimelessWisdom[6]
            woodname8 = TimelessWisdom[7]
        elif getseries1 == 'Dark Chocolate':
            woodname1 = DarkChocolate[0]
            woodname2 = DarkChocolate[1]
            woodname3 = DarkChocolate[2]
            woodname4 = DarkChocolate[3]
            woodname5 = DarkChocolate[4]
            woodname6 = DarkChocolate[5]
            woodname7 = DarkChocolate[6]
            woodname8 = DarkChocolate[7]
            # next series get woodname

        if getseries2 == '':
            getseries2pic1 = ''
            getseries2pic2 = ''
            getseries2pic3 = ''
            getseries2pic4 = ''
            getseries2pic5 = ''
            getseries2pic6 = ''
            getseries2pic7 = ''
            getseries2pic8 = ''
        elif getseries2 == 'Light Adolescence':
            getseries2pic1 = LightAdolescence[0]
            getseries2pic2 = LightAdolescence[1]
            getseries2pic3 = LightAdolescence[2]
            getseries2pic4 = LightAdolescence[3]
            getseries2pic5 = LightAdolescence[4]
            getseries2pic6 = LightAdolescence[5]
            getseries2pic7 = LightAdolescence[6]
            getseries2pic8 = LightAdolescence[7]
        elif getseries2 == 'Elder Brilliance':
            getseries2pic1 = ElderBrilliance[0]
            getseries2pic2 = ElderBrilliance[1]
            getseries2pic3 = ElderBrilliance[2]
            getseries2pic4 = ElderBrilliance[3]
            getseries2pic5 = ElderBrilliance[4]
            getseries2pic6 = ElderBrilliance[5]
            getseries2pic7 = ElderBrilliance[6]
            getseries2pic8 = ElderBrilliance[7]
        elif getseries2 == 'Solid Wood':
            getseries2pic1 = SolidWood[0]
            getseries2pic2 = SolidWood[1]
            getseries2pic3 = SolidWood[2]
            getseries2pic4 = SolidWood[3]
            getseries2pic5 = SolidWood[4]
            getseries2pic6 = SolidWood[5]
            getseries2pic7 = SolidWood[6]
            getseries2pic8 = SolidWood[7]
        elif getseries2 == 'Gentlemens Leather':
            getseries2pic1 = GentlemensLeather[0]
            getseries2pic2 = GentlemensLeather[1]
            getseries2pic3 = GentlemensLeather[2]
            getseries2pic4 = GentlemensLeather[3]
            getseries2pic5 = GentlemensLeather[4]
            getseries2pic6 = GentlemensLeather[5]
            getseries2pic7 = GentlemensLeather[6]
            getseries2pic8 = GentlemensLeather[7]
        elif getseries2 == 'Cherry Passion':
            getseries2pic1 = CherryPassion[0]
            getseries2pic2 = CherryPassion[1]
            getseries2pic3 = CherryPassion[2]
            getseries2pic4 = CherryPassion[3]
            getseries2pic5 = CherryPassion[4]
            getseries2pic6 = CherryPassion[5]
            getseries2pic7 = CherryPassion[6]
            getseries2pic8 = CherryPassion[7]
        elif getseries2 == 'Earth Valley':
            getseries2pic1 = EarthValley[0]
            getseries2pic2 = EarthValley[1]
            getseries2pic3 = EarthValley[2]
            getseries2pic4 = EarthValley[3]
            getseries2pic5 = EarthValley[4]
            getseries2pic6 = EarthValley[5]
            getseries2pic7 = EarthValley[6]
            getseries2pic8 = EarthValley[7]
        elif getseries2 == 'Red Inspire':
            getseries2pic1 = RedInspire[0]
            getseries2pic2 = RedInspire[1]
            getseries2pic3 = RedInspire[2]
            getseries2pic4 = RedInspire[3]
            getseries2pic5 = RedInspire[4]
            getseries2pic6 = RedInspire[5]
            getseries2pic7 = RedInspire[6]
            getseries2pic8 = RedInspire[7]
        elif getseries2 == 'Supreme Wood':
            getseries2pic1 = SupremeWood[0]
            getseries2pic2 = SupremeWood[1]
            getseries2pic3 = SupremeWood[2]
            getseries2pic4 = SupremeWood[3]
            getseries2pic5 = SupremeWood[4]
            getseries2pic6 = SupremeWood[5]
            getseries2pic7 = SupremeWood[6]
            getseries2pic8 = SupremeWood[7]
        elif getseries2 == 'Timeless Wisdom':
            getseries2pic1 = TimelessWisdom[0]
            getseries2pic2 = TimelessWisdom[1]
            getseries2pic3 = TimelessWisdom[2]
            getseries2pic4 = TimelessWisdom[3]
            getseries2pic5 = TimelessWisdom[4]
            getseries2pic6 = TimelessWisdom[5]
            getseries2pic7 = TimelessWisdom[6]
            getseries2pic8 = TimelessWisdom[7]
        elif getseries2 == 'Dark Chocolate':
            getseries2pic1 = DarkChocolate[0]
            getseries2pic2 = DarkChocolate[1]
            getseries2pic3 = DarkChocolate[2]
            getseries2pic4 = DarkChocolate[3]
            getseries2pic5 = DarkChocolate[4]
            getseries2pic6 = DarkChocolate[5]
            getseries2pic7 = DarkChocolate[6]
            getseries2pic8 = DarkChocolate[7]
        # Get woodname
        if getseries2 == '':
            woodname21 = ''
            woodname22 = ''
            woodname23 = ''
            woodname24 = ''
            woodname25 = ''
            woodname26 = ''
            woodname27 = ''
            woodname28 = ''
        elif getseries2 == 'Light Adolescence':
            woodname21 = LightAdolescence[0]
            woodname22 = LightAdolescence[1]
            woodname23 = LightAdolescence[2]
            woodname24 = LightAdolescence[3]
            woodname25 = LightAdolescence[4]
            woodname26 = LightAdolescence[5]
            woodname27 = LightAdolescence[6]
            woodname28 = LightAdolescence[7]
        elif getseries2 == 'Elder Brilliance':
            woodname21 = ElderBrilliance[0]
            woodname22 = ElderBrilliance[1]
            woodname23 = ElderBrilliance[2]
            woodname24 = ElderBrilliance[3]
            woodname25 = ElderBrilliance[4]
            woodname26 = ElderBrilliance[5]
            woodname27 = ElderBrilliance[6]
            woodname28 = ElderBrilliance[7]
        elif getseries2 == 'Solid Wood':
            woodname21 = SolidWood[0]
            woodname22 = SolidWood[1]
            woodname23 = SolidWood[2]
            woodname24 = SolidWood[3]
            woodname25 = SolidWood[4]
            woodname26 = SolidWood[5]
            woodname27 = SolidWood[6]
            woodname28 = SolidWood[7]
        elif getseries2 == 'Gentlemens Leather':
            woodname21 = GentlemensLeather[0]
            woodname22 = GentlemensLeather[1]
            woodname23 = GentlemensLeather[2]
            woodname24 = GentlemensLeather[3]
            woodname25 = GentlemensLeather[4]
            woodname26 = GentlemensLeather[5]
            woodname27 = GentlemensLeather[6]
            woodname28 = GentlemensLeather[7]
        elif getseries2 == 'Cherry Passion':
            woodname21 = CherryPassion[0]
            woodname22 = CherryPassion[1]
            woodname23 = CherryPassion[2]
            woodname24 = CherryPassion[3]
            woodname25 = CherryPassion[4]
            woodname26 = CherryPassion[5]
            woodname27 = CherryPassion[6]
            woodname28 = CherryPassion[7]
        elif getseries2 == 'Earth Valley':
            woodname21 = EarthValley[0]
            woodname22 = EarthValley[1]
            woodname23 = EarthValley[2]
            woodname24 = EarthValley[3]
            woodname25 = EarthValley[4]
            woodname26 = EarthValley[5]
            woodname27 = EarthValley[6]
            woodname28 = EarthValley[7]
        elif getseries2 == 'Red Inspire':
            woodname21 = RedInspire[0]
            woodname22 = RedInspire[1]
            woodname23 = RedInspire[2]
            woodname24 = RedInspire[3]
            woodname25 = RedInspire[4]
            woodname26 = RedInspire[5]
            woodname27 = RedInspire[6]
            woodname28 = RedInspire[7]
        elif getseries2 == 'Supreme Wood':
            woodname21 = SupremeWood[0]
            woodname22 = SupremeWood[1]
            woodname23 = SupremeWood[2]
            woodname24 = SupremeWood[3]
            woodname25 = SupremeWood[4]
            woodname26 = SupremeWood[5]
            woodname27 = SupremeWood[6]
            woodname28 = SupremeWood[7]
        elif getseries2 == 'Timeless Wisdom':
            woodname21 = TimelessWisdom[0]
            woodname22 = TimelessWisdom[1]
            woodname23 = TimelessWisdom[2]
            woodname24 = TimelessWisdom[3]
            woodname25 = TimelessWisdom[4]
            woodname26 = TimelessWisdom[5]
            woodname27 = TimelessWisdom[6]
            woodname28 = TimelessWisdom[7]
        elif getseries2 == 'Dark Chocolate':
            woodname21 = DarkChocolate[0]
            woodname22 = DarkChocolate[1]
            woodname23 = DarkChocolate[2]
            woodname24 = DarkChocolate[3]
            woodname25 = DarkChocolate[4]
            woodname26 = DarkChocolate[5]
            woodname27 = DarkChocolate[6]
            woodname28 = DarkChocolate[7]

        # Get links
        if getseries1 == '':
            getlinks1 = ''
            getlinks2 = ''
            getlinks3 = ''
            getlinks4 = ''
            getlinks5 = ''
            getlinks6 = ''
            getlinks7 = ''
            getlinks8 = ''

        elif getseries1 == 'Light Adolescence':
            getlinks1 = 'http://http://afloorinpictures.co/pratooak'
            getlinks2 = 'http://http://afloorinpictures.co/francemaple'
            getlinks3 = 'http://http://afloorinpictures.co/trentooak'
            getlinks4 = 'http://http://afloorinpictures.co/oxidizedwood'
            getlinks5 = 'http://http://afloorinpictures.co/paleoak'
            getlinks6 = ''
            getlinks7 = ''
            getlinks8 = ''

        elif getseries1 == 'Elder Brilliance':
            getlinks1 = 'http://http://afloorinpictures.co/balsawood'
            getlinks2 = 'http://http://afloorinpictures.co/tulepowood'
            getlinks3 = 'http://http://afloorinpictures.co/spruceomorika'
            getlinks4 = 'http://http://afloorinpictures.co/easternhemlock'
            getlinks5 = 'http://http://afloorinpictures.co/oakfalcata'
            getlinks6 = ''
            getlinks7 = ''
            getlinks8 = ''

        elif getseries1 == 'Solid Wood':
            getlinks1 = 'http://http://afloorinpictures.co/blackwood'
            getlinks2 = 'http://http://afloorinpictures.co/boxelderwood'
            getlinks3 = 'http://http://afloorinpictures.co/hazelplum'
            getlinks4 = 'http://http://afloorinpictures.co/plumdosato'
            getlinks5 = 'http://http://afloorinpictures.co/sessileoak'
            getlinks6 = 'http://http://afloorinpictures.co/thaiteak'
            getlinks7 = 'http://http://afloorinpictures.co/oakespana'
            getlinks8 = 'http://http://afloorinpictures.co/fanooak'

        elif getseries1 == 'Gentlemens Leather':
            getlinks1 = 'http://http://afloorinpictures.co/ambrosiacedar'
            getlinks2 = 'http://http://afloorinpictures.co/catalpawood'
            getlinks3 = 'http://http://afloorinpictures.co/cherrywood'
            getlinks4 = 'http://http://afloorinpictures.co/movinguiwood'
            getlinks5 = ''
            getlinks6 = ''
            getlinks7 = ''
            getlinks8 = ''
       
        elif getseries1 == 'Cherry Passion':
            getlinks1 = 'http://http://afloorinpictures.co/canarywood'
            getlinks2 = 'http://http://afloorinpictures.co/cherryprunus'
            getlinks3 = 'http://http://afloorinpictures.co/jabilloglory'
            getlinks4 = 'http://http://afloorinpictures.co/oakcorilona'
            getlinks5 = ''
            getlinks6 = ''
            getlinks7 = ''
            getlinks8 = ''

        elif getseries1 == 'Earth Valley':
            getlinks1 = 'http://http://afloorinpictures.co/amarellowood'
            getlinks2 = 'http://http://afloorinpictures.co/laureloak'
            getlinks3 = 'http://http://afloorinpictures.co/mountainash'
            getlinks4 = 'http://http://afloorinpictures.co/scafitiwalnut'
            getlinks5 = 'http://http://afloorinpictures.co/southernmagnolia'
            getlinks6 = ''
            getlinks7 = ''
            getlinks8 = ''

        elif getseries1 == 'Red Inspire':
            getlinks1 = 'http://http://afloorinpictures.co/afomosiawood'
            getlinks2 = 'http://http://afloorinpictures.co/amaziquewood'
            getlinks3 = 'http://http://afloorinpictures.co/baliteak'
            getlinks4 = ''
            getlinks5 = 'http://http://afloorinpictures.co/romaniaalder'
            getlinks6 = 'http://http://afloorinpictures.co/macacaubawood'
            getlinks7 = ''
            getlinks8 = ''

        elif getseries1 == 'Supreme Wood':
            getlinks1 = ''
            getlinks2 = ''
            getlinks3 = 'http://http://afloorinpictures.co/berliniawood'
            getlinks4 = 'http://http://afloorinpictures.co/walnutmimosa'
            getlinks5 = 'http://http://afloorinpictures.co/rhodesianwood'
            getlinks6 = ''
            getlinks7 = ''
            getlinks8 = ''

        elif getseries1 == 'Timeless Wisdom':
            getlinks1 = 'http://http://afloorinpictures.co/albiziawood'
            getlinks2 = 'http://http://afloorinpictures.co/anziochestnut'
            getlinks3 = 'http://http://afloorinpictures.co/blackpalm'
            getlinks4 = 'http://http://afloorinpictures.co/chestnutafrica'
            getlinks5 = ''
            getlinks6 = ''
            getlinks7 = ''
            getlinks8 = ''

        elif getseries1 == 'Dark Chocolate':
            getlinks1 = 'http://http://afloorinpictures.co/blackacacia'
            getlinks2 = 'http://http://afloorinpictures.co/chadblackwood'
            getlinks3 = 'http://http://afloorinpictures.co/hormigowood'
            getlinks4 = ''
            getlinks5 = ''
            getlinks6 = ''
            getlinks7 = ''
            getlinks8 = ''

        if getseries2 == '':
            getlinks21 = ''
            getlinks22 = ''
            getlinks23 = ''
            getlinks24 = ''
            getlinks25 = ''
            getlinks26 = ''
            getlinks27 = ''
            getlinks28 = ''

        elif getseries2 == 'Light Adolescence':
            getlinks21 = 'http://http://afloorinpictures.co/pratooak'
            getlinks22 = 'http://http://afloorinpictures.co/francemaple'
            getlinks23 = 'http://http://afloorinpictures.co/trentooak'
            getlinks24 = 'http://http://afloorinpictures.co/oxidizedwood'
            getlinks25 = 'http://http://afloorinpictures.co/paleoak'
            getlinks26 = ''
            getlinks27 = ''
            getlinks28 = ''

        elif getseries2 == 'Elder Brilliance':
            getlinks21 = 'http://http://afloorinpictures.co/balsawood'
            getlinks22 = 'http://http://afloorinpictures.co/tulepowood'
            getlinks23 = 'http://http://afloorinpictures.co/spruceomorika'
            getlinks24 = 'http://http://afloorinpictures.co/easternhemlock'
            getlinks25 = 'http://http://afloorinpictures.co/oakfalcata'
            getlinks26 = ''
            getlinks27 = ''
            getlinks28 = ''

        elif getseries2 == 'Solid Wood':
            getlinks21 = 'http://http://afloorinpictures.co/blackwood'
            getlinks22 = 'http://http://afloorinpictures.co/boxelderwood'
            getlinks23 = 'http://http://afloorinpictures.co/hazelplum'
            getlinks24 = 'http://http://afloorinpictures.co/plumdosato'
            getlinks25 = 'http://http://afloorinpictures.co/sessileoak'
            getlinks26 = 'http://http://afloorinpictures.co/thaiteak'
            getlinks27 = 'http://http://afloorinpictures.co/oakespana'
            getlinks28 = 'http://http://afloorinpictures.co/fanooak'

        elif getseries2 == 'Gentlemens Leather':
            getlinks21 = 'http://http://afloorinpictures.co/ambrosiacedar'
            getlinks22 = 'http://http://afloorinpictures.co/catalpawood'
            getlinks23 = 'http://http://afloorinpictures.co/cherrywood'
            getlinks24 = 'http://http://afloorinpictures.co/movinguiwood'
            getlinks25 = ''
            getlinks26 = ''
            getlinks27 = ''
            getlinks28 = ''

        elif getseries2 == 'Cherry Passion':
            getlinks21 = 'http://http://afloorinpictures.co/canarywood'
            getlinks22 = 'http://http://afloorinpictures.co/cherryprunus'
            getlinks23 = 'http://http://afloorinpictures.co/jabilloglory'
            getlinks24 = 'http://http://afloorinpictures.co/oakcorilona'
            getlinks25 = ''
            getlinks26 = ''
            getlinks27 = ''
            getlinks28 = ''

        elif getseries2 == 'Earth Valley':
            getlinks21 = 'http://http://afloorinpictures.co/amarellowood'
            getlinks22 = 'http://http://afloorinpictures.co/laureloak'
            getlinks23 = 'http://http://afloorinpictures.co/mountainash'
            getlinks24 = 'http://http://afloorinpictures.co/scafitiwalnut'
            getlinks25 = 'http://http://afloorinpictures.co/southernmagnolia'
            getlinks26 = ''
            getlinks27 = ''
            getlinks28 = ''
            
        elif getseries2 == 'Red Inspire':
            getlinks21 = 'http://http://afloorinpictures.co/afomosiawood'
            getlinks22 = 'http://http://afloorinpictures.co/amaziquewood'
            getlinks23 = 'http://http://afloorinpictures.co/baliteak'
            getlinks24 = ''
            getlinks25 = 'http://http://afloorinpictures.co/romaniaalder'
            getlinks26 = 'http://http://afloorinpictures.co/macacaubawood'
            getlinks27 = ''
            getlinks28 = ''

        elif getseries2 == 'Supreme Wood':
            getlinks21 = ''
            getlinks22 = ''
            getlinks23 = 'http://http://afloorinpictures.co/berliniawood'
            getlinks24 = 'http://http://afloorinpictures.co/walnutmimosa'
            getlinks25 = 'http://http://afloorinpictures.co/rhodesianwood'
            getlinks26 = ''
            getlinks27 = ''
            getlinks28 = ''

        elif getseries2 == 'Timeless Wisdom':
            getlinks21 = 'http://http://afloorinpictures.co/albiziawood'
            getlinks22 = 'http://http://afloorinpictures.co/anziochestnut'
            getlinks23 = 'http://http://afloorinpictures.co/blackpalm'
            getlinks24 = 'http://http://afloorinpictures.co/chestnutafrica'
            getlinks25 = ''
            getlinks26 = ''
            getlinks27 = ''
            getlinks28 = ''

        elif getseries2 == 'Dark Chocolate':
            getlinks21 = 'http://http://afloorinpictures.co/blackacacia'
            getlinks22 = 'http://http://afloorinpictures.co/chadblackwood'
            getlinks23 = 'http://http://afloorinpictures.co/hormigowood'
            getlinks24 = ''
            getlinks25 = ''
            getlinks26 = ''
            getlinks27 = ''
            getlinks28 = ''

        #a = [x for xs in tsv for x in xs]
        #get results for selection corner
        result2 = tsv[0]
        result3 = tsv[1]
        result4 = tsv[2]
        result5 = tsv[3]
        result6 = tsv[4]
        result7 = tsv[5]



        # and show the greeting page    
        return render_template('survey/answers.html', getseries1=getseries1, getseries2=getseries2, result2=result2, result3=result3, result4=result4, result5=result5, result6=result6, result7=result7, 
            getseriespic1='../static/images/img/all/' + getseriespic1 + '.jpg',
            getseriespic2='../static/images/img/all/' + getseriespic2 + '.jpg',
            getseriespic3='../static/images/img/all/' + getseriespic3 + '.jpg',
            getseriespic4='../static/images/img/all/' + getseriespic4 + '.jpg',
            getseriespic5='../static/images/img/all/' + getseriespic5 + '.jpg',
            getseriespic6='../static/images/img/all/' + getseriespic6 + '.jpg',
            getseriespic7='../static/images/img/all/' + getseriespic7 + '.jpg',
            getseriespic8='../static/images/img/all/' + getseriespic8 + '.jpg',
            getlinks1 = getlinks1,
            getlinks2 = getlinks2,
            getlinks3 = getlinks3,
            getlinks4 = getlinks4,
            getlinks5 = getlinks5,
            getlinks6 = getlinks6,
            getlinks7 = getlinks7,
            getlinks8 = getlinks8,
            woodname1=woodname1,
            woodname2=woodname2,
            woodname3=woodname3,
            woodname4=woodname4,
            woodname5=woodname5,
            woodname6=woodname6,
            woodname7=woodname7,
            woodname8=woodname8,
            getseries2pic1='../static/images/img/all/' + getseries2pic1 + '.jpg',
            getseries2pic2='../static/images/img/all/' + getseries2pic2 + '.jpg',
            getseries2pic3='../static/images/img/all/' + getseries2pic3 + '.jpg',
            getseries2pic4='../static/images/img/all/' + getseries2pic4 + '.jpg',
            getseries2pic5='../static/images/img/all/' + getseries2pic5 + '.jpg',
            getseries2pic6='../static/images/img/all/' + getseries2pic6 + '.jpg',
            getseries2pic7='../static/images/img/all/' + getseries2pic7 + '.jpg',
            getseries2pic8='../static/images/img/all/' + getseries2pic8 + '.jpg',
            getlinks21 = getlinks21,
            getlinks22 = getlinks22,
            getlinks23 = getlinks23,
            getlinks24 = getlinks24,
            getlinks25 = getlinks25,
            getlinks26 = getlinks26,
            getlinks27 = getlinks27,
            getlinks28 = getlinks28,
            woodname21=woodname21,
            woodname22=woodname22,
            woodname23=woodname23,
            woodname24=woodname24,
            woodname25=woodname25,
            woodname26=woodname26,
            woodname27=woodname27,
            woodname28=woodname28,
            )
    #else:
        # otherwise showing the index page with the questions
    return render_template('survey/index.html', form=form)





