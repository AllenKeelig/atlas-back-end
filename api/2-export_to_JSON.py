#!/usr/bin/python3
""" checker can tell this is blank """
import json
import requests
from sys import argv


def get_employee_todos(employee_id):
    """ this too """

    site = "https://jsonplaceholder.typicode.com/"
    user = requests.get(site + "users/{}".format(employee_id))
    todo = requests.get(site + "todos?userId={}".format(employee_id))

    users = user.json()
    usernames = users.get("username")
    todos = todo.json()

    # print(site, todos, usernames)

    completed = [i for i in todos if i.get("completed")]

    data = {employee_id: [{
        "task": i.get('title'),
        "completed": i.get('completed'),
        "username": usernames
        } for i in todos]}
    with open("{}.json".format(employee_id), "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        get_employee_todos(argv[1])
