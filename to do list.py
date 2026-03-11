

'''
to - do list..

'''
# Simple To-Do List Manager

tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            status = "✔️ Done" if t["completed"] else "❌ Not Done"
            print(f"{i}. {t['task']} - {status}")

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        tasks[task_num - 1]["completed"] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)
        print(f"Task '{removed['task']}' deleted!")
    except (IndexError, ValueError):
        print("Invalid task number.")

#  # Main Program Loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    
    if choice == "1":  
                         
      add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
# - add_task() → naya kam jodta h
#- view_tasks() → sare kam dhikhata ha
#- mark_completed() → kam ko pura mark karta hai
#- mark_completed() → kam ko pura mark karta hai
#- delete_task() → kam hatata hai

     

