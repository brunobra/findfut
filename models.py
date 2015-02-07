import datetime
import requests
from mongoengine import *

connect('futeba')

class Pessoa(Document):
    name = StringField()
    bday = DateTimeField()
    genre = StringField()
    address = StringField()
    city = StringField()
    state = StringField()
    loc = GeoPointField()
    email = EmailField()
    password = StringField()

    def parse_date(self, date):
        d, m, y = date.split("/")
        bday = datetime.date(int(y), int(m), int(d))
        return bday

    def get_loc(self, address):
        add = address.replace(" ", "+")
        API_KEY = "AIzaSyBk_IAok7qdMik0U8iTyZ3h09xKJ9kBtNs"
        URL="https://maps.googleapis.com/maps/api/geocode/json?address=" + add + "&key=" + API_KEY
        req = requests.get(URL)
        resp = req.json()
        loc = resp['results'][0]['geometry']['location']
        return [loc['lat'], loc['lng']]

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