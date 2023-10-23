#!/usr/bin/python3
"""Accesses a REST API for an employee ID and exports data in JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)
    employee_data = response.json()
    employee_name = employee_data.get('name')

    todo_url = f"{url}/todos"
    tasks = requests.get(todo_url).json()

    user_tasks = [{"task": task['title'], "completed": task['completed'],
                   "username": employee_name} for task in tasks]

    output_data = {employee_id: user_tasks}
    output_file = f"{employee_id}.json"

    with open(output_file, 'w') as json_file:
        json.dump(output_data, json_file)

    print(f"Data exported to {output_file}")
