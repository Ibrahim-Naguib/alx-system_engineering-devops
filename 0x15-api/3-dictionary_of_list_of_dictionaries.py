#!/usr/bin/python3
"""Script that exports data in the JSON format"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users").json()
    data = {}
    for user in users:
        username = user.get("username")
        user_id = user.get("id")
        todos = requests.get(url + "/todos", params={"userId": user_id}).json()
        data[user_id] = [{
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                } for todo in todos]
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
