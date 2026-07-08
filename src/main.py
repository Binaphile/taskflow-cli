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


while True:
    task_name = input("Choose an Action: ")

    print()

    if task_name == "2":
        print("Exit")

        break
    if task_name != "1":
       
            print("invalid option")
            break
        
    task_name = input("Choose an Action Again: ")


    chosen_task = input("What task?: ")

    print(f"Task Added Successfully: {chosen_task}")
    print()

    print("1. Add Task")
    print("2. Exit")
                











    





