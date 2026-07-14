print("=================")
print("  TASKFLOW CLI")
print("=================")

print()

# Functions

def greet_user(name):
    print(f"Hello {name}")

def add_the_task(task):
    print(f"Task Added: {task}")

def add_the_list(task_list, task):
    task_list.append(task)

def view_the_task(index, task):
    print(f"{index}. {task['Name']} - {task['Status']}")
    
def menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Status")
    print("4. Delete Tasks")

#---------------

user_name = input("Enter your name: ")

print()

greet_user(user_name)

print()

menu()

print()

tasks = []



while True:
    choice = input("Choose an Action: ")

    print()

    if choice == "4":
        print("My Tasks")

        if not tasks:
            print("No Task Added Yet")
            print()
            continue

        for index, task in enumerate(tasks, start=1):
            view_the_task(index, task)

        print()

        task_number = int(input("Which Task do you want to delete?: "))

        deleted_task = tasks.pop(task_number - 1)

        print(f"\nDeleted Task: {deleted_task['Name']}")

        print("\nUpdated Tasks:\n")

        for index, task in enumerate(tasks, start=1):
            view_the_task(index, task)

        print()

    elif choice == "3":
        print("My Tasks")

        if not tasks:
            print("No Task Added Yet")
            print()
            continue

        for index, task in enumerate(tasks, start=1):
            view_the_task(index, task)

        print()

        task_number = int(input("Which Task is Done?: "))

        selected_task = tasks[task_number - 1]

        selected_task["Status"] = "Done"

        print("\nUpdated Tasks:\n")

        for index, task in enumerate(tasks, start=1):
            view_the_task(index, task)

    elif choice == "1":

        chosen_task = input("What task?: ")

        task = {
            "Name": chosen_task,
            "Status": "Pending"
        }

        print()

        add_the_task(chosen_task)
        add_the_list(tasks, task)
        
        print()

    elif choice == "2":
         print("My Tasks")

         if not tasks:
            print("No Task Added Yet")
         print()

         for index, task in enumerate(tasks, start=1):
            view_the_task(index, task)

    else:
        print("invalid option")

    print()

    menu()













    





