#!/usr/bin/python

import pymongo
import sys
import json
import os

cfg = json.load(file(os.path.join(os.path.dirname(__file__), "conf.json")))

client = pymongo.MongoClient(host=cfg["MONGO_HOST"], port=cfg["MONGO_PORT"])
for doc in client.hpfeeds.auth_key.find():
    print doc


