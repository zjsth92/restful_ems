import time

from flask import Flask
from flask import request
from flask import jsonify

import ems
import model.course as Course
import model.user as User
import db.redis as redis

DEBUG = False

TIME_FORMAT = '%b %d %I:%M %p'
redis_db = redis.get_redis()

app = Flask(__name__)

@app.route("/login", methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    result = ems.login(email, password)

    redis_db.setex(result['sessionId'], email, 3600)    
    return jsonify(result)

@app.route("/courseworks", methods=['GET'])
def list_courses():
    session_id = request.args.get('session_id')
    courses_info = ems.get_courses(session_id)

    courseworks = []

    for course in courses_info['courses']:
        works = ems.get_course_work(session_id, course)
        courseworks += works
    
    # sort by due
    courseworks = sorted(courseworks, key = lambda coursework: time.strptime(coursework["due"], TIME_FORMAT))
    return jsonify(courseworks) 

@app.route("/assignment", methods=['GET'])
def get_assignment_details():
    session_id = request.args.get('session_id')
    assignment_link = request.args.get('assignment_link')
    detail = ems.get_assignment_detail(session_id, assignment_link)
    return jsonify(detail) 

if __name__ == '__main__':
    app.run(debug=DEBUG)