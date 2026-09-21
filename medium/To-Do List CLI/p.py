import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


# ==================== FILE HANDLING ====================

def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# ==================== UTILITY FUNCTIONS ====================

def generate_id(tasks):
    """Generate a unique task ID."""
    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1


def validate_date():
    """Get a valid due date from the user."""

    while True:
        date = input(
            "Enter due date (YYYY-MM-DD) or press Enter for none: "
        ).strip()

        if date == "":
            return None

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("❌ Invalid date. Use YYYY-MM-DD.")


def choose_priority():
    """Get task priority."""

    while True:
        print("\nPriority:")
        print("1. Low")
        print("2. Medium")
        print("3. High")

        choice = input("Choose priority: ").strip()

        priorities = {
            "1": "Low",
            "2": "Medium",
            "3": "High"
        }

        if choice in priorities:
            return priorities[choice]

        print("❌ Invalid choice.")


# ==================== ADD TASK ====================

def add_task(tasks):
    print("\n========== ADD TASK ==========")

    title = input("Enter task title: ").strip()

    while not title:
        print("❌ Task title cannot be empty.")
        title = input("Enter task title: ").strip()

    description = input("Enter description: ").strip()

    priority = choose_priority()

    due_date = validate_date()

    task = {
        "id": generate_id(tasks),
        "title": title,
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(task)
    save_tasks(tasks)

    print("\n✅ Task added successfully!")


# ==================== VIEW TASKS ====================

def display_task(task):
    status = "Completed" if task["completed"] else "Pending"

    print(
        f"\nID          : {task['id']}"
        f"\nTitle       : {task['title']}"
        f"\nDescription : {task['description'] or 'N/A'}"
        f"\nPriority    : {task['priority']}"
        f"\nDue Date    : {task['due_date'] or 'No due date'}"
        f"\nStatus      : {status}"
        f"\nCreated     : {task['created_at']}"
    )

    print("-" * 40)


def view_tasks(tasks):
    print("\n========== ALL TASKS ==========")

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        display_task(task)


# ==================== PENDING TASKS ====================

def view_pending(tasks):
    print("\n========== PENDING TASKS ==========")

    pending = [
        task for task in tasks
        if not task["completed"]
    ]

    if not pending:
        print("🎉 No pending tasks!")
        return

    for task in pending:
        display_task(task)


# ==================== COMPLETED TASKS ====================

def view_completed(tasks):
    print("\n========== COMPLETED TASKS ==========")

    completed = [
        task for task in tasks
        if task["completed"]
    ]

    if not completed:
        print("No completed tasks.")
        return

    for task in completed:
        display_task(task)


# ==================== COMPLETE TASK ====================

def complete_task(tasks):
    print("\n========== COMPLETE TASK ==========")

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    for task in tasks:

        if task["id"] == task_id:

            if task["completed"]:
                print("Task is already completed.")
                return

            task["completed"] = True

            save_tasks(tasks)

            print("✅ Task marked as completed!")
            return

    print("❌ Task not found.")


# ==================== DELETE TASK ====================

def delete_task(tasks):
    print("\n========== DELETE TASK ==========")

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)
            save_tasks(tasks)

            print("🗑️ Task deleted successfully!")
            return

    print("❌ Task not found.")


# ==================== SEARCH TASK ====================

def search_task(tasks):
    print("\n========== SEARCH TASK ==========")

    keyword = input("Enter keyword: ").strip().lower()

    if not keyword:
        print("❌ Search keyword cannot be empty.")
        return

    results = []

    for task in tasks:

        if (
            keyword in task["title"].lower()
            or keyword in task["description"].lower()
        ):
            results.append(task)

    if not results:
        print("No matching tasks found.")
        return

    print(f"\nFound {len(results)} task(s):")

    for task in results:
        display_task(task)


# ==================== UPDATE TASK ====================

def update_task(tasks):
    print("\n========== UPDATE TASK ==========")

    try:
        task_id = int(input("Enter task ID: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    for task in tasks:

        if task["id"] == task_id:

            print("\nLeave input empty to keep the old value.")

            new_title = input(
                f"Title [{task['title']}]: "
            ).strip()

            if new_title:
                task["title"] = new_title

            new_description = input(
                f"Description [{task['description']}]: "
            ).strip()

            if new_description:
                task["description"] = new_description

            change_priority = input(
                "Change priority? (y/n): "
            ).lower()

            if change_priority == "y":
                task["priority"] = choose_priority()

            change_date = input(
                "Change due date? (y/n): "
            ).lower()

            if change_date == "y":
                task["due_date"] = validate_date()

            save_tasks(tasks)

            print("\n✅ Task updated successfully!")
            return

    print("❌ Task not found.")


# ==================== STATISTICS ====================

def show_statistics(tasks):
    print("\n========== TASK STATISTICS ==========")

    total = len(tasks)

    completed = sum(
        task["completed"]
        for task in tasks
    )

    pending = total - completed

    high_priority = sum(
        task["priority"] == "High"
        and not task["completed"]
        for task in tasks
    )

    print(f"Total Tasks        : {total}")
    print(f"Completed Tasks    : {completed}")
    print(f"Pending Tasks      : {pending}")
    print(f"High Priority Left : {high_priority}")

    if total > 0:
        percentage = (completed / total) * 100
        print(f"Completion Rate    : {percentage:.2f}%")


# ==================== MENU ====================

def show_menu():

    print("\n")
    print("=" * 45)
    print("             TO-DO LIST CLI")
    print("=" * 45)

    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks")
    print("4. View Completed Tasks")
    print("5. Complete Task")
    print("6. Update Task")
    print("7. Delete Task")
    print("8. Search Task")
    print("9. Statistics")
    print("10. Exit")

    print("=" * 45)


# ==================== MAIN ====================

def main():

    tasks = load_tasks()

    while True:

        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_pending(tasks)

        elif choice == "4":
            view_completed(tasks)

        elif choice == "5":
            complete_task(tasks)

        elif choice == "6":
            update_task(tasks)

        elif choice == "7":
            delete_task(tasks)

        elif choice == "8":
            search_task(tasks)

        elif choice == "9":
            show_statistics(tasks)

        elif choice == "10":
            print("\n👋 Goodbye!")
            break

        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

