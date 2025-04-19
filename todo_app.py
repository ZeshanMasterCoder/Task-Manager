import json
import os
from datetime import datetime

# Task Manager Application
# Developed by Zeshan Noor
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file or initialize an empty list if file is missing."""
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON file. Initializing empty task list.")
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """Save tasks to JSON file with proper formatting."""
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def validate_date(date_str):
    """Validate date format (YYYY-MM-DD) and ensure it's not in the past."""
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d")
        if input_date.date() < datetime.now().date():
            return False, "Due date cannot be in the past."
        return True, input_date.strftime("%Y-%m-%d")
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD."

def add_task(tasks, description, category="General", due_date=None):
    """Add a new task with description, category, due date, and timestamp."""
    try:
        task = {
            "id": len(tasks) + 1,
            "description": description,
            "category": category,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "due_date": due_date
        }
        tasks.append(task)
        save_tasks(tasks)
        due_msg = f", Due: {due_date}" if due_date else ""
        print(f"Task added: {description} (Category: {category}{due_msg})")
    except Exception as e:
        print(f"Error adding task: {e}")

def mark_complete(tasks, task_id):
    """Mark a task as completed by its ID."""
    try:
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                save_tasks(tasks)
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Error: Task ID {task_id} not found.")
    except Exception as e:
        print(f"Error marking task: {e}")

def delete_task(tasks, task_id):
    """Delete a task by its ID."""
    try:
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                deleted_task = tasks.pop(i)
                save_tasks(tasks)
                print(f"Task {task_id} deleted: {deleted_task['description']}")
                return
        print(f"Error: Task ID {task_id} not found.")
    except Exception as e:
        print(f"Error deleting task: {e}")

def display_tasks(tasks, incomplete_only=False):
    """Display tasks, optionally showing only incomplete tasks with due date status."""
    if not tasks:
        print("No tasks found.")
        return
    current_date = datetime.now().date()
    for task in tasks:
        if incomplete_only and task["completed"]:
            continue
        status = "✓" if task["completed"] else " "
        due_status = ""
        if task["due_date"]:
            due_date = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
            due_status = f" | Due: {task['due_date']}"
            if not task["completed"] and due_date < current_date:
                due_status += " (Overdue)"
        print(f"[{status}] ID: {task['id']} | {task['description']} | Category: {task['category']}{due_status} | Created: {task['created_at']}")

def main():
    """Run the Task Manager application."""
    tasks = load_tasks()
    
    print("""
    ==========================================
          Task Manager by Zeshan Noor
    ==========================================
    Organize your tasks with ease and efficiency.
    """)
    
    while True:
        print("\n=== Task Manager Menu ===")
        print("1. Add Task")
        print("2. Mark Task Completed")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. View Incomplete Tasks")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            description = input("Enter task description: ").strip()
            if description:
                category = input("Enter category (e.g., Work, Personal, or press Enter for General): ").strip() or "General"
                due_date_input = input("Enter due date (YYYY-MM-DD, or press Enter to skip): ").strip()
                if due_date_input:
                    is_valid, result = validate_date(due_date_input)
                    if not is_valid:
                        print(f"Error: {result}")
                        continue
                    due_date = result
                else:
                    due_date = None
                add_task(tasks, description, category, due_date)
            else:
                print("Error: Task description cannot be empty.")
                
        elif choice == '2':
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                mark_complete(tasks, task_id)
            except ValueError:
                print("Error: Please enter a valid numeric ID.")
                
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(tasks, task_id)
            except ValueError:
                print("Error: Please enter a valid numeric ID.")
                
        elif choice == '4':
            display_tasks(tasks)
            
        elif choice == '5':
            display_tasks(tasks, incomplete_only=True)
            
        elif choice == '6':
            print("Thank you for using Task Manager by Zeshan Noor.")
            break
            
        else:
            print("Invalid option. Please select 1-6.")

if __name__ == "__main__":
    main()