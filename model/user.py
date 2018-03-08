# -*- coding: utf-8 -*-
import os
import sys
import pymongo
# import db
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'db'))

import mongodb
db = mongodb.get_db()
db.users.create_index([('email', pymongo.ASCENDING)],unique=True)

def insert(email, courses=[]):
    user = {
        'email': email,
        'courses': courses
    }
    db.users.insert_one(user)

def add_courses(email, courses):
    db.users.update_one(
            {"id": criteria},
            {
            "$set": {
                "name":name,
                "age":age,
                "country":country
            }
            }
        )
def find_by_email(email):
    return db.users.find_one({"email": email})
