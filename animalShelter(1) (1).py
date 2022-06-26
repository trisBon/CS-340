from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to access the MongoDB databases and collections 

        self.client = MongoClient('mongodb://%s:%s@localhost:47189' % ("myUserAdmin", "BLB019640!"))
        #self.client = MongoClient('mongodb://%s:%s@localhost:47189' % (username, password))

        # where xxxxx is your unique port number
        self.database = self.client['AAC']

# Search method used by R, U, and D methods
    def search(self,key):
        result = self.database.animals.find(key,{"_id":False})
        if result is None:
            raise Exception("False. No key match found")
        else:
            return result
    def userSearch(self, key):
        result = self.admin.system.user.find(key)
        return result
        
# Create method to implement the C in CRUD.       
    def create(self, data):
        if data is None:
            raise Exception("False. Create Attempt Unsuccessful.")
        else:
            self.database.animals.insert_one(data) 
            print("True. Create Successful!")

# Read method to implement the R in CRUD. 
    def read(self,key):
        output = self.search(key) # variable to hold search result     
        print(output)
             
# Update method to implement the U in CRUD.
    def update(self, key, newKey):
        keyValue = self.search(key)  # check for "key" match in database
        for key in newKey:           # find newKey "key" match in keyValue dict
            for accessKey in keyValue:
                if key == accessKey:
                    self.database.animals.update_one(keyValue, {"$set": newKey})
                    print("Update Successful!")
                    return self.read(newKey)
        raise Exception("False. Update Unsuccessful.") # throw if no matching "key" in keyValue dict
        
# Delete method to implement the D in CRUD.
    def delete(self, key):
        remove = self.search(key)
        self.database.animals.delete_one(remove)
        print("True. Delete successful!")
        return remove
    
    
 # DO NOT ALTER CODE BELOW!!! IT WORKS
 # ReadAll method 
 #   def readAll(self, key):
 #      item = self.database.animals.find_one()
 #      
 #       
 #      for items in item:
 #
 #               json = format(dumps(items))
 #              return json 