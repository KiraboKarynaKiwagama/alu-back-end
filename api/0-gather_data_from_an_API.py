#!/usr/bin/python3
"""Script to gather employee TODO list progress from a REST API."""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)

    user_info = requests.get(url).json()
    todo_info = requests.get(todo_url).json()

    employee_name = user_info.get("name")
    completed_tasks = [task for task in todo_info if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todo_info)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_number_of_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
