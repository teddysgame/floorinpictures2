# forms.py

from wtforms import Form, StringField, SelectField, validators

class VinylSearchForm(Form):
    choices = [('Label', 'Label'),
    		   # ('Brand', 'Brand'),
         #       ('Album', 'Album')]
    # select = SelectField('Search for vinyl:', choices=choices)
    # search = StringField('')


# class AlbumForm(Form):
#     label = StringField('Label')
#     brand = StringField('Brand')
#     title = StringField('Title')
#     code = StringField('Code')
#     price = StringField('Price')
