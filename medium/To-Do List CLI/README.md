# 📝 To-Do List CLI

A command-line **To-Do List application built using Python**.

The application allows users to create, manage, search, update, complete, and delete tasks. Task data is stored permanently in a JSON file.

---

## 🚀 Features

* ➕ Add tasks
* 📋 View all tasks
* ⏳ View pending tasks
* ✅ View completed tasks
* ✔️ Mark tasks as completed
* ✏️ Update tasks
* 🗑️ Delete tasks
* 🔍 Search tasks
* ⭐ Task priorities
* 📅 Due dates
* 📊 Task statistics
* 💾 Persistent JSON storage
* 🆔 Automatic task ID generation
* 🛡️ Input validation

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

No external libraries are required.

---

## 📁 Project Structure

```text
todo-cli/
│
├── todo.py
├── tasks.json
└── README.md
```

### `todo.py`

Contains the main application and all task-management functions.

### `tasks.json`

Stores tasks permanently.

### `README.md`

Contains project documentation.

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/todo-cli.git
```

### 2. Navigate to the project

```bash
cd todo-cli
```

### 3. Run the application

```bash
python todo.py
```

---

## 🖥️ Application Menu

```text
=============================================
             TO-DO LIST CLI
=============================================

1. Add Task
2. View All Tasks
3. View Pending Tasks
4. View Completed Tasks
5. Complete Task
6. Update Task
7. Delete Task
8. Search Task
9. Statistics
10. Exit

=============================================
```

---

## ➕ Adding a Task

Example:

```text
========== ADD TASK ==========

Enter task title: Complete DSA Assignment
Enter description: Solve 5 DP problems

Priority:
1. Low
2. Medium
3. High

Choose priority: 3

Enter due date (YYYY-MM-DD) or press Enter for none: 2026-09-25

✅ Task added successfully!
```

---

## 📄 Stored Data

Tasks are stored in `tasks.json`.

Example:

```json
[
    {
        "id": 1,
        "title": "Complete DSA Assignment",
        "description": "Solve 5 DP problems",
        "priority": "High",
        "due_date": "2026-09-25",
        "completed": false,
        "created_at": "2026-09-21 21:30:00"
    }
]
```

---

## 📊 Statistics

The application provides:

```text
========== TASK STATISTICS ==========

Total Tasks        : 10
Completed Tasks    : 6
Pending Tasks      : 4
High Priority Left : 2
Completion Rate    : 60.00%
```

---

## 🧠 Python Concepts Used

### 1. Functions

The application is divided into reusable functions:

```python
add_task()
delete_task()
update_task()
search_task()
complete_task()
```

### 2. Lists

All tasks are stored in a Python list.

```python
tasks = []
```

### 3. Dictionaries

Each task is represented using a dictionary:

```python
{
    "id": 1,
    "title": "Learn Python",
    "priority": "High",
    "completed": False
}
```

### 4. JSON

Tasks are saved permanently using:

```python
json.dump()
```

and loaded using:

```python
json.load()
```

### 5. Exception Handling

Invalid user input is handled using:

```python
try:
    ...
except ValueError:
    ...
```

### 6. Date Handling

The `datetime` module is used to validate due dates.

---

## 🔮 Future Improvements

Possible upgrades:

* [ ] Sort tasks by priority
* [ ] Sort tasks by due date
* [ ] Detect overdue tasks
* [ ] Add task categories
* [ ] Add recurring tasks
* [ ] Add reminders
* [ ] Export tasks to CSV
* [ ] SQLite database
* [ ] User authentication
* [ ] GUI using Tkinter
* [ ] Web version using Flask
* [ ] Streamlit dashboard

---

## 🎯 Learning Goals

This project is useful for practicing:

```text
Python Basics
     ↓
Functions
     ↓
Lists & Dictionaries
     ↓
File Handling
     ↓
JSON
     ↓
Exception Handling
     ↓
Date & Time
     ↓
CRUD Operations
     ↓
Project Structure
```

---

## 👨‍💻 Author

**Rohit**

B.Tech Computer Science
NIT Delhi

---

## 📜 License

This project is created for educational and learning purposes.
