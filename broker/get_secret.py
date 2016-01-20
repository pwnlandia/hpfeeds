import pymongo
import sys
import json
import os

cfg = json.load(file(os.path.join(os.path.dirname(__file__), "conf.json")))

ident = sys.argv[1]
client = pymongo.MongoClient(host=cfg["MONGO_HOST"], port=cfg["MONGO_PORT"])
results = client.hpfeeds.auth_key.find({'identifier': ident})
if results.count() > 0:
    print results[0]['secret']
