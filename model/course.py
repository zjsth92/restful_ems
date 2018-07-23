# -*- coding: utf-8 -*-
import os
import sys
import pymongo
# import db
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'db'))

import mongodb
db = mongodb.get_db()
db.courses.create_index([('course_id', pymongo.ASCENDING)],unique=True)

def insert(trimester, course):
    course_id = trimester+'_'+course['code']+'_'+course['section']
    course['course_id'] = course_id
    db.courses.insert_one(course)

def find_one(code, section, trimester):
    course_id = trimester+'_'+code+'_'+section
    return db.courses.find({"course_id": course_id})
