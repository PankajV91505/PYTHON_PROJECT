import json

# File to store tasks
task_file = "tasks.json"

def load_tasks():
    """Load tasks from file."""
    try:
        with open(task_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Save tasks to file."""
    with open(task_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added! ✅")

def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found! ✨")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["completed"] else "❌"
            print(f"{i}. {task['task']} [{status}]")

def mark_completed(task_number):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed! 🎉")
    else:
        print("Invalid task number!")

def delete_task(task_number):
    """Delete a task."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {deleted_task['task']} 🗑")
    else:
        print("Invalid task number!")

def main():
    """Main function to run the to-do list program."""
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_num = int(input("Enter task number to mark as completed: "))
            mark_completed(task_num)
        elif choice == "4":
            view_tasks()
            task_num = int(input("Enter task number to delete: "))
            delete_task(task_num)
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
