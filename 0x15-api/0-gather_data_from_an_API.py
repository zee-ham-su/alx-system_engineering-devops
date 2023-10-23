#!/usr/bin/python3
"""Accessing a REST API for a given employee ID, returns
information about his/her TODO list progress."""

import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_url = f"{url}/todos"
    tasks = requests.get(todo_url).json()

    done_tasks = [task['title'] for task in tasks if task.get('completed')]

    print("Employee {} is done with tasks ({}/{}):"
          .format(employee_name, len(done_tasks), len(tasks)))

    for task_title in done_tasks:
        print("\t {}".format(task_title))
