import time

from flask import Flask
from flask import request
from flask import jsonify

import ems
import model.course as Course
import model.user as User
import db.redis as redis

TIME_FORMAT = '%b %d %I:%M %p'
redis_db = redis.get_redis()

app = Flask(__name__)

@app.route("/login", methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']
    result = ems.login(email, password)
    find_user = User.find_by_email(email)
    if find_user is None:
        User.insert(email)

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

if __name__ == '__main__':
    app.run(debug=True)