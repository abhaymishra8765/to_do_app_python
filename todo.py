import os

Task_File = "tasks.txt"

def load_tasks():
    if not os.path.exists(Task_File):
        return []
    with open(Task_File, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(Task_File, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = input("Enter a task: ").strip()
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"{task} added successfully.")

def view_tasks():
    tasks = load_tasks()
    if len(tasks) == 0:
        print("No tasks.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        print()

def delete_task():
    view_tasks()
    tasks = load_tasks()
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            deleted_task = tasks.pop(task_number)
            save_tasks(tasks)
            print(f"Task '{deleted_task}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_as_completed():
    view_tasks()
    tasks = load_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number] = f"[✓] {tasks[task_number]}"
            save_tasks(tasks)
            print(f"Task '{tasks[task_number]}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_as_completed()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
