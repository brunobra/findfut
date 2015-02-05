import urllib2
import pymongo
import json


class Pessoa:
	def __init__(self, db):
		self.db = db
		self.users = db.users

	def find_location(self, address):
		add = address.replace(" ", "+")
		api_key = "AIzaSyBk_IAok7qdMik0U8iTyZ3h09xKJ9kBtNs"
		URL="https://maps.googleapis.com/maps/api/geocode/json?address=" + add + "&key=" + api_key
		req = urllib2.Request(URL)
		response = urllib2.urlopen(req)
		data = json.load(response)
		location = data['results'][0]['geometry']['location']
		return(location)

	def insert_user(self, nome, address):
		add = self.find_location(address)
		data = {
			'name':nome,
			'address':address,
			'loc':{
				'type':'Point',
				'coordinates':[
				add['lat'],
				add['lng']
				]
			}
		}
		self.users.insert(data)

class Places:
	def __init__(self, db):
                self.db = db
                self.places = db.places
	
        def find_location(self, address):
                add = address.replace(" ", "+")
                api_key = "AIzaSyBk_IAok7qdMik0U8iTyZ3h09xKJ9kBtNs"
                URL="https://maps.googleapis.com/maps/api/geocode/json?address=" + add + "&key=" + api_key
                req = urllib2.Request(URL)
                response = urllib2.urlopen(req)
                data = json.load(response)
                location = data['results'][0]['geometry']['location']
                return(location)
	
	def insert_place(self, nome, address):
                add = self.find_location(address)
                data = {
                        'name':nome,
                        'address':address,
                        'loc':{
				'type':'Point',
				'coordinates':[
				add['lat'],
				add['lng']
				]
			}
		}
                self.places.insert(data)

