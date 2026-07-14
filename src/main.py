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
    print("5. Exit")


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

    return True


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

    # Exit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")