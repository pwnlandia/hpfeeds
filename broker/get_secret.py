import pymongo
import sys
import json
import os

ident = sys.argv[1]
client = pymongo.MongoClient(host=os.getenv("MONGO_HOST"), port=os.getenv("MONGO_PORT"))
if os.getenv("MONGO_AUTH"):
    client.hpfeeds.authenticate(os.getenv("MONGO_USER"), os.getenv("MONGO_PASSWORD"), mechanism=os.getenv("MONGO_AUTH_MECHANISM"))
results = client.hpfeeds.auth_key.find({'identifier': ident})
if results.count() > 0:
    print results[0]['secret']
