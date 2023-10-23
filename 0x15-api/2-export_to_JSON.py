#!/usr/bin/python3
"""Accesses a REST API for an employee ID and exports data in JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    response = requests.get(url)
    username = response.json().get('username')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    employee_data = {
        employee_id: [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            for task in tasks
        ]
    }

    with open('{}.json'.format(employee_id), 'w') as json_file:
        json.dump(employee_data, json_file)
