#!/usr/bin/python3
"""
Fetch an employee's name and to-do task completion status from the API.

Usage: python script_name.py <employee_id>
"""

import requests
import sys
 
 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)
 
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("employee_id must be an integer")
        sys.exit(1)
 
    base_url = "https://jsonplaceholder.typicode.com"
 
    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    if user_response.status_code != 200:
        print("Employee not found")
        sys.exit(1)
 
    user_data = user_response.json()
    employee_name = user_data.get("name")
 
    todos_response = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    )
    todos_data = todos_response.json()
 
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)
 
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))
 
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
 

