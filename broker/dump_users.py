#!/usr/bin/python

import pymongo
import sys
import json
import os

cfg = json.load(file(os.path.join(os.path.dirname(__file__), "conf.json")))

client = pymongo.MongoClient(host=cfg["MONGO_HOST"], port=cfg["MONGO_PORT"])
if cfg["MONGO_AUTH"]:
    client.hpfeeds.authenticate(cfg["MONGO_USER"], cfg["MONGO_PASSWORD"], mechanism=cfg["MONGO_AUTH_MECHANISM"])
for doc in client.hpfeeds.auth_key.find():
    print doc


