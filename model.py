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
		return(response)

