todo_list = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("✅ Task added!")

def view_tasks():
    if not todo_list:
        print("📭 No tasks found.")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if not todo_list:
        return
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"❌ Removed task: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
