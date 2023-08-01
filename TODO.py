import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def display_menu(name):
    clear_screen()
    print(f"📝 Todo List Manager - Welcome, {name}! 🎉\n")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Quit\n")

def add_task(tasks):
    name = input("\nEnter the name of the task: ")
    while True:
        priority = input("Enter the priority of the task (High/Medium/Low): ").lower()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Invalid priority. Please enter High, Medium, or Low.")
    due_date = input("Enter the due date for the task (dd/mm/yyyy): ")
    category = input("Enter the category of the task (Work/Personal/School etc.): ")
    tasks.append({"name": name, "completed": False, "priority": priority, "due_date": due_date, "category": category})

def view_tasks(tasks):
    if tasks:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✅ Completed" if task["completed"] else "❌ Not completed"
            print(f"{i}. {task['name']} - {status} - Priority: {task['priority'].capitalize()} - Due: {task['due_date']} - Category: {task['category']}")
    else:
        print("\nNo tasks yet. Start by adding a task!")

def mark_task_as_completed(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = input("\nEnter the number of the task to mark as completed (or 'back' to go back): ")
        if task_num.lower() == 'back':
            return
        if task_num.isdigit() and 0 < int(task_num) <= len(tasks):
            tasks[int(task_num)-1]["completed"] = True
        else:
            print("Invalid task number!")

if __name__ == "__main__":
    name = input("Please enter your name: ")
    tasks = []
    while True:
        display_menu(name)
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_as_completed(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please choose a number between 1 and 4.")
        input("\nPress enter to continue...")
