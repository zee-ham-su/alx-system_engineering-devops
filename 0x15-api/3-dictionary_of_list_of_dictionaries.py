#!/usr/bin/python3
"""Accesses a REST API for an employee ID and exports data in JSON format."""
import json
import requests
import sys


import json
import requests
import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(base_url)
    users = response.json()

    employee_data = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        user_url = (
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(user_id)
        )
        todo_url = user_url + '/todos/'
        response = requests.get(todo_url)
        tasks = response.json()

        employee_data[user_id] = [
                {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
                }
                for task in tasks
            ]
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(employee_data, json_file)
