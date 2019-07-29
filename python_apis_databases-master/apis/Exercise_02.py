'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)

data = response.json()
print(type(data))
data2 = data[0]
pprint(data2)
pprint((data))

lis = []

#data3 = data.get('email')
print(lis)
'''
for k, v in data:
    if k == 'email':
        lis.append(k,v)


for i in data:



data2 = [d['email'] for d in data]
print(data2)
'''