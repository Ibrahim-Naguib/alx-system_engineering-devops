#!/usr/bin/python3
# Script that exports data in the JSON format

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get(url + "/users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "/todos", params={"userId": user_id}).json()
                   
    with open("{}.json".format(user_id),"w") as f:
        json.dump({user_id: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            } for todo in todos]}, f)
