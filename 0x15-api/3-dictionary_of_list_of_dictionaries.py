#!/usr/bin/python3
""" script to export data in the JSON format."""
import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + 'users').json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in requests.get(
                url + "todos?userId=" + str(user.get('id'))).json()]
            for user in users}, jsonfile)
