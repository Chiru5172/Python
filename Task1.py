tasks = []
while True:
    print("\n----- To-Do List Menu -----")
    print("1. Add Task")
    print("2. Update Task")
    print("3. View Tasks")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print("Task added successfully!")
    elif choice == "2":
        if not tasks:
            print("No tasks available. Add a task first.")
        else:
            print("Current Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_index = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_index < len(tasks):
                updated_task = input("Enter the updated task: ")
                tasks[task_index] = updated_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    elif choice == "4":
        print("Exit...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
