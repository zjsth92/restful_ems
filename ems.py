import requests
import constants
from redis import Redis
from rq import Queue

import parser.dashboard_parser as dashboard_parser
import parser.coursework_parser as coursework_parser
import parser.login_parser as login_parser
import parser.assignment_parser as assignment_parser

import model.coursework as Coursework
import worker.coursework as CourseworkJob


coursework_save_q = Queue('high_coursework_save', connection=Redis())
coursework_update_q = Queue('high_coursework_update', connection=Redis())

def login(username, password):
    credentials = {'user[email]': username, 'user[password]': password, 'commit': "Login"}
    session = requests.Session()
    r = session.post(constants.EMS_SIGNIN_URL, credentials)

    login_success = False
    errorMsg = ""
    userinfo = None
    if r.status_code == 200:
        login_success = login_parser.parse(r.content)
        if login_success:
            userinfo = dashboard_parser.parse_userinfo(r.content)
        else:
            errorMsg = "Invalid email or password"
    else:
        errorMsg = "EMS Error"      
    session_id = session.cookies.get_dict()['_session_id']
    return {
        "loginSuccess": login_success,
        "sessionId": session_id,
        "errorMsg": errorMsg,
        "userinfo": userinfo
    }
    

def get_courses(session_id):
    cookies = {'_session_id': session_id}
    session = requests.Session()
    r = session.get("https://ems.itu.edu/student", cookies=cookies)
    courses_info = dashboard_parser.parse(r.content)
    return courses_info

def get_course_work(session_id, course, trimester):
    courseworks = Coursework.find_all_works(course['code'], course['section'], trimester)
    course_link = course['link']
    cookies = {'_session_id': session_id}
    if not courseworks:
        session = requests.Session()
        r = session.get(course_link+"/coursework", cookies=cookies)
        courseworks = coursework_parser.parse(r.content)
        for coursework in courseworks:
            coursework.update( {"course_code":course['code']})
            # Send to queue and save to db
            coursework_save_q.enqueue_call(
                func=CourseworkJob.save_coursework,
                args=(trimester, coursework, course['code'], course['section'])
            )
    else:
        coursework_update_q.enqueue_call(
            func=CourseworkJob.update_coursework,
            args=(course_link, cookies, trimester, course['code'], course['section'])
        )

    return courseworks

def get_assignment_detail(session_id, link):
    cookies = {'_session_id': session_id}
    session = requests.Session()
    r = session.get("https://ems.itu.edu"+link, cookies=cookies)
    detail = assignment_parser.parse(r.content)
    return detail