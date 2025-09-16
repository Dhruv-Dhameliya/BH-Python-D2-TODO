import os

FILENAME = "tasks.txt"

def load_task():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        tasks = f.read().splitlines()
    return tasks

def save_task(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_task(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    task = input("\nEnter new task: ").strip()
    if task:
        tasks.append(task)
        save_task(tasks)
        print("\nTask added successfully!\n")
    else:
        print("\nTask cannot be empty.\n")

def remove_task(tasks):
    view_task(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_task(tasks)
                print(f"\nTask '{removed}' removed!\n")
            else:
                print("\nInvalid task number.\n")
        except ValueError:
            print("\nPlease enter a valid number.\n")

def main():
    tasks = load_task()
    while True:
        print("==========================")
        print("----- TO-DO LIST APP -----")
        print("==========================\n")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("\nExiting To-Do List. Goodbye! 👋\n")
            break
        else:
            print("\nInvalid choice! Please try again.\n")

if __name__ == "__main__":
    main()