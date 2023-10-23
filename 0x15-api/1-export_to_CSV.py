#!/usr/bin/python3
"""Accessing a REST API for a given employee ID, returns
information about his/her TODO list progress."""

import csv
import requests
import sys

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w', newline='') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(['USER_ID', 'USERNAME',
                             'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        for task in tasks:
            csv_writer.writerow([employeeId, username,
                                 task.get('completed'), task.get('title')])
