'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)

json_response = response.json()
print(type(json_response))
data = json_response["data"]

lis = []

for i in data:
    data1 = i['email']
    lis.append(data1)

print(lis)