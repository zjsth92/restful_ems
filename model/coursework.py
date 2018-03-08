# -*- coding: utf-8 -*-
import os
import sys
import pymongo
# import db
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'db'))

import mongodb
db = mongodb.get_db()
db.courses.create_index([('course_id', p ymongo.ASCENDING)],unique=True)

def insert(trimester, coursework, course_id):
    course_id = course['code']+'_'+course['section']
    course['course_id'] = course_id
    db.courses.insert_one(course)

def find_by_code_and_section(code, section):
    course_id = code+'_'+section
    return db.courses.find_one({"course_id": course_id})
