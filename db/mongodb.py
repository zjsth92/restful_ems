import os
import yaml
from pymongo import MongoClient

# with open(os.path.join(os.path.dirname(__file__), '..', "config.yaml"), 'r') as config_file:
#     config = yaml.load(config_file)

MONGO_DB_HOST = "localhost"
MONGO_DB_PORT = "27017"
MONGO_DB_USER = "itu_ems"
MONGO_DB_PASS = "itu_ems_db"

DB_NAME = "itu_ems"
MONGO_DB_URL = "mongodb://%s:%s@%s:%s/%s" % (MONGO_DB_USER, MONGO_DB_PASS, MONGO_DB_HOST, MONGO_DB_PORT, DB_NAME)
print("Connect to mongodb: " + MONGO_DB_URL)
client = MongoClient(MONGO_DB_URL)

def get_db(db=DB_NAME):
    db = client[db]
    return db