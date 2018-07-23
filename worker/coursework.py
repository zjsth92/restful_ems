# -*- coding: utf-8 -*-
import os
import sys
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'model'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'parser'))
import coursework_parser
import model.coursework as Coursework

def save_coursework(trimester, work, code, section):
    course_id = trimester+'_'+code+'_'+section
    Coursework.insert(trimester, work, course_id, section)

def update_coursework(course_link, cookies, trimester, course_code, section):
    session = requests.Session()
    r = session.get(course_link+"/coursework", cookies=cookies)
    courseworks = coursework_parser.parse(r.content)
    course_id = trimester+'_'+course_code+'_'+section
    for coursework in courseworks:
        coursework.update( {"course_code":course_code})
        Coursework.update(trimester, coursework, course_id, section)