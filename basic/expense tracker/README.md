# 💰 Personal Expense Tracker

A simple command-line **Personal Expense Tracker** built using Python.

The application allows users to record, view, search, analyze, and delete their daily expenses. All expense data is stored permanently in a JSON file.

---

## 🚀 Features

* ➕ Add new expenses
* 📋 View all expenses
* 🔍 Search expenses by category
* 💰 Calculate total spending
* 📅 Generate monthly spending summaries
* 🗑️ Delete expenses
* 💾 Persistent data storage using JSON
* ✅ Input validation
* 🆔 Automatic expense ID generation

---

## 🛠️ Technologies Used

* Python 3
* JSON
* File Handling
* Functions
* Lists
* Dictionaries
* Exception Handling
* `datetime`
* `os`

No external Python libraries are required.

---

## 📁 Project Structure

```text
expense-tracker/
│
├── expense_tracker.py
├── expenses.json
└── README.md
```

### `expense_tracker.py`

Contains the complete application logic.

### `expenses.json`

Stores expense data permanently.

### `README.md`

Project documentation.

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/expense-tracker.git
```

### 2. Open the project

```bash
cd expense-tracker
```

### 3. Run the program

```bash
python expense_tracker.py
```

---

## 🖥️ Menu

When the program starts, you will see:

```text
========================================
       PERSONAL EXPENSE TRACKER
========================================

1. Add Expense
2. View All Expenses
3. Search by Category
4. Total Expenses
5. Monthly Summary
6. Delete Expense
7. Exit

========================================
```

---

## 📌 Example

### Adding an expense

```text
========== Add Expense ==========

Enter amount: ₹250
Enter category: Food
Enter description: Lunch
Enter date (YYYY-MM-DD) or press Enter for today:

Expense added successfully!
```

The data is stored in `expenses.json`:

```json
[
    {
        "id": 1,
        "amount": 250.0,
        "category": "Food",
        "description": "Lunch",
        "date": "2026-09-20"
    }
]
```

---

## 📊 Monthly Summary

Example:

```text
========== Monthly Summary ==========

Enter month (YYYY-MM): 2026-09

Total spending in 2026-09: ₹3250.00

Category-wise spending:
Food: ₹1500.00
Travel: ₹1000.00
Shopping: ₹750.00
```

---

## 🧠 Concepts Practiced

This project demonstrates several important Python concepts:

### 1. Functions

The project is divided into separate functions such as:

```python
add_expense()
view_expenses()
delete_expense()
monthly_summary()
```

### 2. Lists and Dictionaries

Each expense is represented using a dictionary:

```python
{
    "id": 1,
    "amount": 250,
    "category": "Food",
    "description": "Lunch",
    "date": "2026-09-20"
}
```

All expenses are stored inside a list.

### 3. JSON File Handling

Data is saved using:

```python
json.dump()
```

and loaded using:

```python
json.load()
```

### 4. Exception Handling

Invalid numerical input and invalid dates are handled using:

```python
try:
    ...
except ValueError:
    ...
```

### 5. Date Handling

Python's `datetime` module is used to validate and process dates.

---

## 🔮 Future Improvements

Possible upgrades for this project:

* [ ] Edit an existing expense
* [ ] Add income tracking
* [ ] Calculate balance
* [ ] Add budget limits
* [ ] Budget exceeded notifications
* [ ] Export data to CSV
* [ ] Generate PDF reports
* [ ] Add graphs using Matplotlib
* [ ] Add SQLite database
* [ ] Build a GUI using Tkinter
* [ ] Build a web version using Flask
* [ ] Add user authentication
* [ ] Build a Streamlit dashboard

---

## 👨‍💻 Author

**Rohit**

B.Tech Computer Science
NIT Delhi

---

## 📜 License

This project is created for learning and educational purposes.
