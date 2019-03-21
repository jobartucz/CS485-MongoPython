# There is a great getting started tutorial at
# https://api.mongodb.com/python/current/tutorial.html

from pymongo import MongoClient
client = MongoClient()

db = client['demo_database']       # I already created this on my local machine
collection = db['demo_collection'] # and this too, but if you don't it will still work

documents = collection.find()

print("All the current documents in our collection:")
for doc in documents:
    print(doc)
    
new_item = {"name" : "Zeus",
            "age" : 99999,
            "height" : 499,
            "deceased" : True}

collection.insert_one(new_item)

print("The row we just inserted:")
one_doc = collection.find_one({"name":"Zeus"})
print(one_doc)
