#!/usr/bin/python3
"""  using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import requests
from sys import argv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = (requests.get(url + 'users',
            params={"id": argv[1]}).json())[0].get("name")
    todos = requests.get(url + 'todos', params={'userId': argv[1]}).json()
    list_obj = [("\t "+object.get("title")) for i, object in enumerate(todos)
                if todos[i].get("completed") is True]
    print('Employee {} is done with tasks({}/{}):'.format(
        user, len(list_obj), len(todos)))
    print("\n".join(list_obj))
