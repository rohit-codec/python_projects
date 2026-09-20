import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


# -------------------- File Handling --------------------

def load_expenses():
    """Load expenses from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_expenses(expenses):
    """Save expenses to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# -------------------- Utility Functions --------------------

def generate_id(expenses):
    """Generate a unique expense ID."""
    if not expenses:
        return 1

    return max(expense["id"] for expense in expenses) + 1


def get_amount():
    """Get a valid positive expense amount."""
    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


def get_date():
    """Get expense date."""
    while True:
        date_input = input(
            "Enter date (YYYY-MM-DD) or press Enter for today: "
        ).strip()

        if not date_input:
            return datetime.now().strftime("%Y-%m-%d")

        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input

        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")


# -------------------- Expense Operations --------------------

def add_expense(expenses):
    """Add a new expense."""

    print("\n========== Add Expense ==========")

    amount = get_amount()

    category = input("Enter category: ").strip()

    while not category:
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    description = input("Enter description: ").strip()

    date = get_date()

    expense = {
        "id": generate_id(expenses),
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully!")


def view_expenses(expenses):
    """Display all expenses."""

    print("\n========== All Expenses ==========")

    if not expenses:
        print("No expenses found.")
        return

    print(
        f"{'ID':<5}"
        f"{'Date':<15}"
        f"{'Category':<15}"
        f"{'Amount':<12}"
        f"{'Description'}"
    )

    print("-" * 70)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"₹{expense['amount']:<11.2f}"
            f"{expense['description']}"
        )


def search_by_category(expenses):
    """Display expenses belonging to a category."""

    print("\n========== Search by Category ==========")

    if not expenses:
        print("No expenses found.")
        return

    category = input("Enter category: ").strip().lower()

    filtered = [
        expense
        for expense in expenses
        if expense["category"].lower() == category
    ]

    if not filtered:
        print("No expenses found for this category.")
        return

    total = 0

    for expense in filtered:
        print(
            f"ID: {expense['id']} | "
            f"Date: {expense['date']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['description']}"
        )

        total += expense["amount"]

    print("-" * 50)
    print(f"Total spent on {category}: ₹{total:.2f}")


def total_expenses(expenses):
    """Calculate total spending."""

    print("\n========== Total Expenses ==========")

    if not expenses:
        print("No expenses found.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print(f"Total money spent: ₹{total:.2f}")


def monthly_summary(expenses):
    """Display expenses for a particular month."""

    print("\n========== Monthly Summary ==========")

    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month format.")
        return

    monthly_expenses = [
        expense
        for expense in expenses
        if expense["date"].startswith(month)
    ]

    if not monthly_expenses:
        print("No expenses found for this month.")
        return

    total = sum(expense["amount"] for expense in monthly_expenses)

    category_totals = {}

    for expense in monthly_expenses:
        category = expense["category"]

        category_totals[category] = (
            category_totals.get(category, 0)
            + expense["amount"]
        )

    print(f"\nTotal spending in {month}: ₹{total:.2f}")

    print("\nCategory-wise spending:")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")


def delete_expense(expenses):
    """Delete an expense using its ID."""

    print("\n========== Delete Expense ==========")

    if not expenses:
        print("No expenses found.")
        return

    try:
        expense_id = int(input("Enter expense ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for expense in expenses:

        if expense["id"] == expense_id:

            expenses.remove(expense)
            save_expenses(expenses)

            print("Expense deleted successfully!")
            return

    print("Expense ID not found.")


# -------------------- Menu --------------------

def display_menu():
    print("\n")
    print("=" * 40)
    print("       PERSONAL EXPENSE TRACKER")
    print("=" * 40)

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search by Category")
    print("4. Total Expenses")
    print("5. Monthly Summary")
    print("6. Delete Expense")
    print("7. Exit")

    print("=" * 40)


# -------------------- Main Program --------------------

def main():

    expenses = load_expenses()

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            search_by_category(expenses)

        elif choice == "4":
            total_expenses(expenses)

        elif choice == "5":
            monthly_summary(expenses)

        elif choice == "6":
            delete_expense(expenses)

        elif choice == "7":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
