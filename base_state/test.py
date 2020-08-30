#!/usr/bin/env python3

import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "api/get_key/data")
print(response.json())

response = requests.get(BASE + "api/insert/test=test")
print(response.json())

response = requests.get(BASE + "api/get_key/test")
print(response.json())

response = requests.get(BASE + "api/get_state")
print(response.json())

response = requests.get(BASE + "api/update/data=blah")
print(response.json())

response = requests.get(BASE + "api/get_state")
print(response.json())

response = requests.get(BASE + "api/delete/test")
print(response.json())

response = requests.get(BASE + "api/get_state")
print(response.json())