#!/usr/bin/python3
# Script that exports data in the CSV format

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get(url + "/users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "/todos", params={"userId": user_id}).json()
                   
    completed = []
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    with open("{}.csv".format(user_id),"w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, todo.get("completed"), todo.get("title")]
        ) for todo in todos]
