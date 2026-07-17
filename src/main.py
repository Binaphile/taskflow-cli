print("=================")
print("  TASKFLOW CLI")
print("=================\n")


# ---------------- Functions ----------------

def greet_user(name):
    print(f"Hello {name}")


def menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Status")
    print("4. Delete Task")
    print("5. Task Statistics")
    print("6. Exit")


def create_task(name):
    return {
        "Name": name,
        "Status": "Pending"
    }


def add_task(task_list, task):
    task_list.append(task)
    print(f"Task Added: {task['Name']}")


def display_task(index, task):
    print(f"{index}. {task['Name']} - {task['Status']}")


def display_tasks(task_list):
    print("My Tasks")

    if not task_list:
        print("No Task Added Yet")
        return False

    print()

    for index, task in enumerate(task_list, start=1):
        display_task(index, task)

    print(f"\nTotal Tasks: {len(task_list)}")

    return True


def task_exists(task_list, task_name):

    for task in task_list:
        if task["Name"].lower() == task_name.lower():
            return True
        
    return False


def display_statistics(task_list):

    if not task_list:
        print("No Task Added Yet")
        return

    total_tasks = len(task_list)
    completed_tasks = 0
    pending_tasks = 0

    for task in task_list:

        if task["Status"] == "Done":
            completed_tasks += 1
        else:
            pending_tasks += 1

    print("Task Statistics")
    print("----------------")
    print(f"Total Tasks     : {total_tasks}")
    print(f"Completed Tasks : {completed_tasks}")
    print(f"Pending Tasks   : {pending_tasks}")


# ---------------- Main Program ----------------

user_name = input("Enter your name: ")
print()

greet_user(user_name)

tasks = []

while True:
    print()
    menu()
    print()

    choice = input("Choose an Action: ")

    print()

    # Add Task
    if choice == "1":

        task_name = input("What task?: ")

        if task_exists(tasks, task_name):
            print("Task already exists.")

        else:
            task = create_task(task_name)
            add_task(tasks, task)  
     

    # View Tasks
    elif choice == "2":

        display_tasks(tasks)

    # Update Status
    elif choice == "3":

        if not display_tasks(tasks):
            continue

        print()

        task_number = int(input("Which task is done?: "))

        selected_task = tasks[task_number - 1]
        selected_task["Status"] = "Done"

        print("\nUpdated Tasks:\n")

        display_tasks(tasks)

    # Delete Task
    elif choice == "4":

        if not display_tasks(tasks):
            continue

        print()

        task_number = int(input("Which task do you want to delete?: "))

        deleted_task = tasks.pop(task_number - 1)

        print(f"\nDeleted Task: {deleted_task['Name']}")

        print("\nUpdated Tasks:\n")

        display_tasks(tasks)       

    # Task Statistics and Exit
    elif choice == "5":

        display_statistics(tasks)

    # Exit
    elif choice == "6":

        print("Goodbye!")
        break

    


    