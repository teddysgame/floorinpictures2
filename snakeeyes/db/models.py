#from snakeeyes.app import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, instance_relative_config=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vinyllib.db'
app.secret_key = "flask rocks!"

db = SQLAlchemy(app)

class Label(db.Model):
    __tablename__ = "labels"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "{}".format(self.name)


class Album(db.Model):
    """"""
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String)
    title = db.Column(db.String)
    code = db.Column(db.String)
    price = db.Column(db.Integer)

    label_id = db.Column(db.Integer, db.ForeignKey("labels.id"))
    label = db.relationship("Label", backref=db.backref(
        "albums", order_by=id), lazy=True)
