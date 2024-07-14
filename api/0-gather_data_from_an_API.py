#!/usr/bin/python3

import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        # Fetch employee details
        user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
        user_response.raise_for_status()  # Raise an HTTPError for bad responses
        user = user_response.json()
        
        # Fetch employee TODO list
        todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
        todos_response.raise_for_status()  # Raise an HTTPError for bad responses
        todos = todos_response.json()
        
        # Employee name
        employee_name = user['name']
        
        # Calculate TODO list progress
        total_tasks = len(todos)
        done_tasks = [task for task in todos if task['completed']]
        number_of_done_tasks = len(done_tasks)
        
        # Print the progress
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task['title']}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except KeyError as e:
        print(f"Unexpected response structure: missing key {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
