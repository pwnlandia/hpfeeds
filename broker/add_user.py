#!/usr/bin/python

import pymongo
import sys
import json
import os

def handle_list(arg):
    if arg:
        return arg.split(",")
    else:
        return []

if len(sys.argv) < 5:
    print >> sys.stderr, "Usage: %s <ident> <secret> <publish> <subscribe>"%sys.argv[0]
    sys.exit(1)

ident = sys.argv[1]
secret = sys.argv[2]
publish = handle_list(sys.argv[3])
subscribe = handle_list(sys.argv[4])

rec = {
    "identifier": ident,
    "secret": secret,
    "publish": publish,
    "subscribe":subscribe
}

client = pymongo.MongoClient(host=os.getenv("MONGO_HOST"), port=os.getenv("MONGO_PORT"))
if os.getenv("MONGO_AUTH") == "true":
    client.hpfeeds.authenticate(os.getenv("MONGO_USER"), os.getenv("MONGO_PASSWORD"), mechanism=os.getenv("MONGO_AUTH_MECHANISM"))
res = client.hpfeeds.auth_key.update({"identifier": ident}, {"$set": rec}, upsert=True)
client.fsync()
client.close()

if res['updatedExisting']:
    print "updated %s"%rec
else:
    print "inserted %s"%(rec)

