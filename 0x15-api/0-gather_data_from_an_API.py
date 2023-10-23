#!/usr/bin/python3
"""Accesses a REST API for an employee ID"""

import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done_tasks = [task for task in tasks if task.get('completed')]
    done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
