from mongoengine import *

class Pessoa(Document):
    name = StringField()
    bday = DateTimeField()
    genre = StringField()
    address = TextField()
    city = StringField()
    state = StringField()
    loc = DictField()
    email = EmailField()
    password = StringField()

class Place(Document):
    name = StringField()
    address = TextField()
    city = StringField()
    state = StringField()
    loc = DictField()
    sport = StringField()
    obs = TextField()