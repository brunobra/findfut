import pymongo

conn = pymongo.MongoClient('localhost, 27017')
db = conn.futeba

data = {}
user = raw_input("Qual o seu nome?\n")
address = raw_input("Qual o seu endereco?\n")

data['user'] = user
data['address'] = address

db.users.insert(data)
#users = db.users.find()
#print users[0]
