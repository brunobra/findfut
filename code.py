import pymongo
from model import Pessoa

conn = pymongo.MongoClient("localhost, 27017")
db = conn.futeba

users = Pessoa(db)

nome = raw_input("Qual o seu nome?\n")
address = raw_input("Qual o seu endereco?\n")

users.insert_user(nome, address)
