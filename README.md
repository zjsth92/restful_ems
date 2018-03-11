# EMS RESTFul

This is a RESTFul crawler for [ITU Educational Management System](https://ems.itu.edu/)

## Run

Before runing the app, please make sure that you have all required dependences installed. Using **pip** to install dependences

```
pip3 install -r requirements.txt
```

Run this app as a simple FLASK APP
```
flask run --host=0.0.0.0
```

## Debug

If you want to enable the debug mode. Please change the value of **Debug** into **True** in ```app.py```, and then run it in python3

```
python3 app.py
```

## Quick Look

### Login

Login into EMS system with Email and Password

#### Endpoint definition
`/login`

#### HTTP method
POST

#### Parameters

Content Type: **JSON**

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| email | *Required*. The ITU student email |string |
| password | *Required* | string |

#### Result Example

```json
{
    "errorMsg": null,
    "loginSuccess": true,
    "sessionId": "sessionId",
    "userinfo": {
        "avatar": "https://s3.amazonaws.com/itu.ems.production/avatars/xxxx",
        "username": "Your Name"
    }
}
```

### List Courseworks

List all course works and sort them by due

#### Endpoint definition
`/courseworks`

#### HTTP method
GET

#### Parameters

Content Type: **JSON**

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| session_id | *Required*. Login Session ID |string |

#### Result Example

```json
[
    {
        "available": "Jan 10  1:00 PM",
        "course_code": "SWE 680",
        "due": "Jan 13 11:00 PM",
        "link": "/student/sections/5675/quizzes/3564",
        "point": "30.0",
        "submit": "",
        "title": "Quiz 1B",
        "type": "Quizzes"
    },
    {
        "available": "Jan 8 12:00 AM",
        "course_code": "SWE 680",
        "due": "Jan 13 11:59 PM",
        "link": "/student/sections/5675/quizzes/3565",
        "point": "30.0",
        "submit": "",
        "title": "Quiz 1 ( Chapter 1 and 2)",
        "type": "Quizzes"
    }
]
```

### Get Assignment Details

Get assignment details including description and all attachments

#### Endpoint definition
`/assignment`

#### HTTP method
GET

#### Parameters

Content Type: **JSON**

| Parameter | Description | Data Type |
|-----------|-------------|-----------|
| session_id | *Required*. Login Session ID |string |
| assignment_link | *Required*. Assginment link |string |

#### Result Example

```json
{
    "desc": [
        "\n",
        "See the attached instructions.",
        "\n"
    ],
    "documents": [
        {
            "link": "https://s3.amazonaws.com/itu.ems.production/attachments/xxxxx",
            "name": "Homework.pdf",
            "size": "427 KB"
        }
    ],
    "title": "First week homework"
}
```
