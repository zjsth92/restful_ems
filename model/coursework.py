# -*- coding: utf-8 -*-
import os
import sys
import pymongo
import datetime
# import db
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'db'))

import mongodb
db = mongodb.get_db()
db.courseworks.create_index([('course_id', pymongo.ASCENDING)],unique=False)

def insert(trimester, coursework, course_id, section):
    coursework['course_id'] = course_id
    coursework['section'] = section
    coursework['created_at'] = datetime.datetime.now()
    db.courseworks.insert(coursework)

def update(trimester, coursework, course_id, section):
    coursework['course_id'] = course_id
    coursework['section'] = section
    coursework['updated_at'] = datetime.datetime.now()
    db.courseworks.update_one({'course_id': course_id, 'title': coursework['title']}, {"$set": coursework}, upsert=False)

def find_all_works(code, section, trimester):
    course_id = trimester+"_"+code+'_'+section
    cursor = db.courseworks.find({"course_id": course_id})
    works = list()
    for document in cursor:
        document.pop('_id', None)
        works.append(document)
    return works
