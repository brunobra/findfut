import datetime
import requests

from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash

from mongoengine import *

connect('futeba')

class User(UserMixin, Document):
    username = StringField(unique=True)
    bday = DateTimeField()
    genre = StringField()
    address = StringField()
    city = StringField()
    state = StringField()
    loc = GeoPointField()
    email = EmailField(unique=True)
    password = StringField(max_length=100)

    @classmethod
    def create_user(cls, username, bday, genre, address, city, state, email, password):

        def get_loc(address):
            add = address.replace(" ", "+")
            API_KEY = "AIzaSyBk_IAok7qdMik0U8iTyZ3h09xKJ9kBtNs"
            URL="https://maps.googleapis.com/maps/api/geocode/json?address=" + add + "&key=" + API_KEY
            req = requests.get(URL)
            resp = req.json()
            loc = resp['results'][0]['geometry']['location']
            return [loc['lat'], loc['lng']]

        def parse_date(date):
            d, m, y = date.split("/")
            bday = datetime.date(int(y), int(m), int(d))
            return bday


        try:
            cls(
                username = username,
                bday = parse_date(bday),
                genre = genre,
                address = address,
                city = city,
                state = state,
                loc = get_loc(address),
                email = email,
                password = generate_password_hash(password)
            ).save()
        except:
            raise ValueError("User already exists!")


class Place(Document):
    name = StringField()
    address = StringField()
    city = StringField()
    state = StringField()
    loc = DictField()
    sport = StringField()
    obs = StringField()

    def get_loc(self, address):
        add = address.replace(" ", "+")
        API_KEY = "AIzaSyBk_IAok7qdMik0U8iTyZ3h09xKJ9kBtNs"
        URL="https://maps.googleapis.com/maps/api/geocode/json?address=" + add + "&key=" + API_KEY
        req = requests.get(URL)
        resp = req.json()
        loc = resp['results'][0]['geometry']['location']
        return [loc['lat'], loc['lng']]