use futeba
db.users.ensureIndex({'loc':'2dsphere'})
db.places.ensureIndex({'loc':'2dsphere'})
