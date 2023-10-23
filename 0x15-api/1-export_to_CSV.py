#!/usr/bin/python3
"""Accessing a REST API for a given employee ID, returns
information about his/her TODO list progress."""

import csv
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

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [employee_id, username, t.get("completed"), t.get("title")]
         ) for t in tasks]
