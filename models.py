from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(200))
    text = db.Column(db.Text)
    img = db.Column(db.String(250))
    date = db.Column(db.Date)

class MenuElement(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    link = db.Column(db.String(200))

class SocialNetwork(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    img = db.Column(db.String(200))
    link = db.Column(db.String(250))

class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(350))
    email = db.Column(db.String(250))
    text = db.Column(db.Text())

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(250))

