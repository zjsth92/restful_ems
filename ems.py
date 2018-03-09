import requests
import constants
import parser.dashboard_parser as dashboard_parser
import parser.coursework_parser as coursework_parser
import parser.login_parser as login_parser

def login(username, password):
    credentials = {'user[email]': username, 'user[password]': password, 'commit': "Login"}
    session = requests.Session()
    r = session.post(constants.EMS_SIGNIN_URL, credentials)

    login_success = False
    if r.status_code == requests.codes.ok:
        login_success = login_parser.parse(r.content)
            
    session_id = session.cookies.get_dict()['_session_id']

    return {
        "loginSuccess": login_success,
        "sessionId": session_id,
        "errorMsg": "Invalid email or password"
    }
    

def get_courses(session_id):
    cookies = {'_session_id': session_id}
    session = requests.Session()
    r = session.get("https://ems.itu.edu/student", cookies=cookies)
    courses = dashboard_parser.parse(r.content)
    return courses

def get_course_work(session_id, course):
    course_link = course['link']
    cookies = {'_session_id': session_id}
    session = requests.Session()
    r = session.get(course_link+"/coursework", cookies=cookies)
    courseworks = coursework_parser.parse(r.content)
    for coursework in courseworks:
        coursework.update( {"course_code":course['code']})
    return courseworks