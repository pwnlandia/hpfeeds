#!/usr/bin/python

import pymongo
import sys
import json
import os

client = pymongo.MongoClient(host=os.getenv("MONGO_HOST"), port=os.getenv("MONGO_PORT"))
if os.getenv("MONGO_AUTH") == "true":
    client.hpfeeds.authenticate(os.getenv("MONGO_USER"), os.getenv("MONGO_PASSWORD"), mechanism=os.getenv("MONGO_AUTH_MECHANISM"))
for doc in client.hpfeeds.auth_key.find():
    print doc


