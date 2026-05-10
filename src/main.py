import json
from task import Task
# start off with making an empty list for tasks
tasks = []

def print_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task complete")
    print("4. Exit")

def add_task():
    task = input("Enter a task: ")
    tasks.append(Task(task))
    save_tasks()
    print("Menu has been updated.")

def view_tasks():
    if len(tasks) == 0:
        return print("No tasks yet")
    for index, item in enumerate(tasks, start=1):
        print(index, item["title"], item["completed"])

def mark_task_complete():
    count = 1
    for item in range(0, len(tasks)):
        if tasks[item]["completed"] == False:
            status = " - Not Done"
        else:
            status = " - Done"
        print(count, tasks[item]["title"], status)
        count = count + 1
    choice = int(input("Which task is complete? "))
    tasks[choice - 1]["completed"] = True 
    save_tasks() 
    print("Task has been marked completed.")

def save_tasks():
    saved_tasks = []
    for item in tasks:
        saved_tasks.append(item.to_dict())
    with open("tasks.json", "w") as file:
        json.dump(saved_tasks, file)

def load_tasks():
    global tasks
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    new_tasks = []
    for item in tasks:
        new_object = Task(item["title"], item["completed"])
        new_tasks.append(new_object)
    tasks = new_tasks

load_tasks()
while True:
    print_menu()
    choice = input("Pick a number: ")
    if (choice == "1"):
        add_task()
    elif (choice == "2"):
        view_tasks()
    elif (choice == "3"):
        mark_task_complete()
    elif (choice == "4"):
        print("Goodbye")
        break
    else:
        print("invalid, please try again")