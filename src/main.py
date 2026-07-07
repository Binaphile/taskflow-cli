print("=================")
print("  TASKFLOW CLI")
print("=================")

print()

user_name = input("Enter your name: ")

print()

print(f"Hello {user_name}")


print()

print("1. Add Task")
print("2. Exit")

print()

task_name = input("Choose an Action: ")

print()

if task_name == "1":
    chosen_task = input("What Task: ")
    print()
    print("Task Added Successfully!")
    print()
    print(f"Current Task: {chosen_task}")

elif task_name == "2":
    print("ByeBye")

else:
    print("Invalid Option")


