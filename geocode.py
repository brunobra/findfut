import urllib2
import pymongo
import json

conn = pymongo.MongoClient('localhost, 27017')
db = conn.futeba

user = "Bruno"
address = "Rua Capitao Ferraiuolo, 71"
add = address.replace(" ", "+")

URL="https://maps.googleapis.com/maps/api/geocode/json?address=" + add + "&key=AIzaSyBk_IAok7qdMik0U8iTyZ3h09xKJ9kBtNs"

req = urllib2.Request(URL)
response = urllib2.urlopen(req)
data = json.load(response)
location =  data['results'][0]['geometry']['location']

user_data = {
	'Name':user,
	'address':address,
	'loc':{
		'type':'Point',
		'coordinates':[location['lat'], location['lng']]
	}
}

db.users.insert(user_data)
