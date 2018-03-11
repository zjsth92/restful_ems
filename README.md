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

| Parameter | Description | Data Type |
|-----------|------|-----|-----------|
| email | *Required*. The ITU student email |string |
| password | *Required* | string |

### List Courseworks

List all course works and sorted with due

#### Endpoint definition
`/courseworks`

#### HTTP method
GET

#### Parameters

| Parameter | Description | Data Type |
|-----------|------|-----|-----------|
| session_id | *Required*. Login Session ID |string |

### Get Assignment Details

Get assignment details including description and all attachments

#### Endpoint definition
`/assignment`

#### HTTP method
GET

#### Parameters

| Parameter | Description | Data Type |
|-----------|------|-----|-----------|
| session_id | *Required*. Login Session ID |string |
| assignment_link | *Required*. Assginment link |string |