'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''
import requests
from pprint import pprint

user_input = int(input("Please select from the following options (enter the number of the action you'd like to take):\n 1) Create a new account  (POST)\n 2) View all your tasks (GET)\n 3) View your completed tasks (GET)\n 4) View only your incomplete tasks (GET)\n 5) Create a new task (POST)\n 6) Update an existing task (PATCH/PUT)\n 7) Delete a task (DELETE): "))

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "lUKas",
    "last_name": "HeRRMaNN",
    "email": "lumaherr@email.com",
}
body2 = {
    "id": 26,
    "first_name": "Lukas",
    "last_name": "Herrmann",
    "email": "lumaherr@gmail.com"
}
response = requests.get(base_url)
json_response = response.json()
data = json_response["data"]
list1 = []

for i in data:
    data1 = i["id"]
    list1.append(data1)

last_id = max(list1)

if user_input == 1:
    response = requests.post(base_url, json=body)
elif user_input == 2:
    response2 = requests.get(base_url)
    pprint(response2.content)
elif user_input == 3:
    print("NOT FOUND")
elif user_input == 4:
    print("NOT FOUND")
elif user_input == 5:
    response3 = requests.post(base_url, json=body)
elif user_input == 6:
    response4 = requests.put(base_url, json=body2)
    pprint(response4.content)
elif user_input == 7:
    response5 = requests.delete(base_url + "/" + str(last_id))
    pprint(response5.status_code)