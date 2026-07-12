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
    print("3. Exit")

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

    if choice == "3":
        print("Exit")
        break

    elif choice == "1":

        chosen_task = input("What task?: ")

        task = {
            "Name": chosen_task,
            "Status": "Pending"
        }

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













    





