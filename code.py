import pymongo
from model import Pessoa
from model import Places

conn = pymongo.MongoClient("localhost, 27017")
db = conn.futeba
users = Pessoa(db)
place = Places(db)


choice = raw_input("Quem e voce?\n1 - Usuario\n2 - Estabelecimento\n")
if int(choice) == 1:
	name = raw_input("Qual o seu nome?\n")
	address = raw_input("Qual o seu endereco?\n")
	users.insert_user(name, address)
elif int(choice) == 2:
	name = raw_input("Qual o nome do seu estabelecimento?\n")
	address = raw_input("Qual o endereco?\n")
	place.insert_place(name, address)
