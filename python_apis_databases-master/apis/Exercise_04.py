'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''

import requests
from pprint import pprint
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "id": 24,
    "first_name": "Lukas",
    "last_name": "Herrmann",
    "email": "lumaherr@gmail.com"
}

response = requests.put(base_url, json=body)
print(response.status_code)
response = requests.get(base_url)
pprint(f"Response Content: {response.content}")