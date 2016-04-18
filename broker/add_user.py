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

cfg = json.load(file(os.path.join(os.path.dirname(__file__), "conf.json")))

client = pymongo.MongoClient(host=cfg["MONGO_HOST"], port=cfg["MONGO_PORT"])
if cfg["MONGO_AUTH"]:
    db = client.hpfeeds.authenticate(cfg["MONGO_USER"], cfg["MONGO_PASSWORD"], mechanism=cfg["MONGO_AUTH_MECHANISM"])
    res = db.auth_key.update({"identifier": ident}, {"$set": rec}, upsert=True)
else:
    res = client.hpfeeds.auth_key.update({"identifier": ident}, {"$set": rec}, upsert=True)

client.fsync()
client.close()

if res['updatedExisting']:
    print "updated %s"%rec
else:
    print "inserted %s"%(rec)

