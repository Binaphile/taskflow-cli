print("=================")
print("  TASKFLOW CLI")
print("=================")

print()

user_name = input("Enter your name: ")

print()

print(f"Hello {user_name}")


print()

print("1. Add Task")
print("2. View Tasks")
print("3. Exit")

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

        print()

        print(f"Task Added: {chosen_task}")
        tasks.append(chosen_task)

    elif choice == "2":
         print("My Tasks")

         if not tasks:
            print("No Task Added Yet")
         print()

         for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    else:
        print("invalid option")


    print()

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")













    





