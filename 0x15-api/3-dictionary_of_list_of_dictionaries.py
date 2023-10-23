#!/usr/bin/python3
"""Accesses a REST API for an employee ID and exports data in JSON format."""

import requests
import sys
import json

if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users"
    employees = {}

    for employee_id in range(1, 11):  # Assuming employee IDs are from 1 to 10
        url = f"{base_url}/{employee_id}"
        response = requests.get(url)
        employee_data = response.json()
        employee_name = employee_data.get('name')

        todo_url = f"{url}/todos"
        tasks = requests.get(todo_url).json()

        tasks_data = [{"username": employee_name, "task": task['title'],
                       "completed": task['completed']} for task in tasks]
        employees[str(employee_id)] = tasks_data

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(employees, json_file)
