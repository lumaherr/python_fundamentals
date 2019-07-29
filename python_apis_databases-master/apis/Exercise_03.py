'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests

from pprint import pprint
base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "Lukas",
    "last_name": "Herrmann",
    "email": "lumaherr@gmail.com"
}
response = requests.post(base_url, json=body)

print(response.status_code)

response2 = requests.get(base_url)
pprint(response2.content)