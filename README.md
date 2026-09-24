# 💸 PyExpenseTracker - CLI

**PyExpenseTracker** is a simple **CLI-based expense management application** built with Python. It allows you to add, view, search, update, delete, save, and load your daily expenses.

This project was created as a practical Python project to practice **lists, dictionaries, functions, loops, conditions, CRUD operations, file handling, JSON data storage, and menu-driven programs**. ✨

---

## 🌸 Features

### ➕ Add Expenses

Add a new expense with:

* 🍽️ Expense title
* 💰 Amount
* 📅 Date
* 🏷️ Category
* 🆔 Automatically generated ID

Example:

```text
Expense for (breakfast/lunch/dinner/etc): Lunch
Enter the amount: 150
Enter the date: 29-08-2026
Enter category (food/healthcare/daily-needs/etc): Food

Expense Successfully registered!!
```

---

### 👀 View Expenses

View all your saved expenses in a clean format:

```text
===============================
        My-Expense-list
===============================

id       : 1
title    : Lunch
amount   : 150.0
date     : 29-08-2026
category : Food

===============================
```

---

### 🔍 Search Expenses

Search for an expense using:

```text
1 → ID
2 → Title
3 → Amount
4 → Date
5 → Category
```

Example:

```text
Search with Id{1}, title{2}, amount{3}, date{4}, category{5}: 5

Enter Category for Expense: Food
```

The matching expense will then be displayed. 🔎

---

### ✏️ Update Expenses

Update an existing expense using its ID.

You can modify:

```text
1 → Title
2 → Amount
3 → Date
4 → Category
```

Example:

```text
Enter expense ID to Update: 2

Update Title{1}, Amount{2}, Date{3}, Category{4}: 2

Enter new amount: 250

Expense Updated Successfully!!
```

---

### 🗑️ Delete Expenses

Delete an expense by its ID with a confirmation step:

```text
Enter Id to delete Expense: 3

Are You Sure You Want To Delete This Expense?

(yes{y}/no{n}): y

Expense Deleted Successfully!!
```

You can also cancel the deletion. 🌷

---

### 💾 Save Expense Data

The project now supports **saving expense data** so your expenses can be stored and reused instead of disappearing when the program closes.

The save functionality allows the current expense list to be written to a data file.

Example menu option:

```text
6 → Save Expense Data
```

This introduces **file handling and data persistence** into the project. 💾

---

### 📂 Load Expense Data

Previously saved expenses can also be loaded when running the application.

Example menu option:

```text
7 → Load Expense Data
```

This allows the application to restore previously saved expenses.

```text
Application
     ↓
Load saved data
     ↓
Expense List
     ↓
Add / Search / Update / Delete
     ↓
Save updated data
```

This makes the project more like a real application because the data can persist between program sessions. 🚀

---

## 🎮 Menu

The application now provides a menu for managing expenses:

```text
=======================
      Expense-li
=======================

1. Add New Expense
2. View Expense List
3. Search Expense
4. Update Existing Expense
5. Delete Expense
6. Save Expense Data
7. Load Expense Data

=======================

Select Task:
```

Choose an option and manage your expenses directly from the terminal. 💻✨

---

## 🧠 What I Learned

Building and updating this project helped me practice:

* 🐍 Python fundamentals
* 📦 Lists
* 📖 Dictionaries
* 🔁 `for` and `while` loops
* 🔀 `if / elif / else`
* 🧩 Functions
* 🔍 Searching through lists
* ✏️ Updating dictionary values
* 🗑️ Removing items from lists
* 🔢 Working with numbers
* 📝 User input
* ♻️ Reusable functions
* 🛠️ CRUD operations
* 🖥️ Menu-driven CLI applications
* 📁 File handling
* 💾 Saving data
* 📂 Loading data
* 🔄 Data persistence

---

## 🏗️ Project Structure

```text
PyExpenseTracker/

│
├── index.py
│
├── data/
│   └── expenses.json
│
└── README.md
```

---

## 🔄 How Data Persistence Works

The application now follows a simple data flow:

```text
              ┌──────────────────┐
              │   Start Program  │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │  Load Data       │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │  Expense List    │
              └────────┬─────────┘
                       ↓
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
      Add            Update         Delete
        │              │              │
        └──────────────┼──────────────┘
                       ↓
              ┌──────────────────┐
              │    Save Data     │
              └──────────────────┘
```

This means expenses can survive even after the program is closed and restarted.

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Aryan-gour127/PyExpenseTracker
```

### 2️⃣ Open the project

```bash
cd PyExpenseTracker
```

### 3️⃣ Run the program

```bash
python index.py
```

That's it! 🎉

---

## 🛠️ Tech Used

| Technology       | Purpose                              |
| ---------------- | ------------------------------------ |
| 🐍 Python        | Main programming language            |
| 💻 CLI           | User interface                       |
| 📦 Lists         | Store expenses during execution      |
| 📖 Dictionaries  | Store individual expense information |
| 🔧 Functions     | Organize program logic               |
| 📁 File Handling | Read and write stored data           |
| 💾 JSON          | Store expense data persistently      |

---

## 💡 Example Expense

```python
{
    "id": 1,
    "title": "Breakfast",
    "amount": 120.0,
    "date": "29-08-2026",
    "category": "Food"
}
```

---

## 🌱 Future Improvements

Now that basic data persistence has been added, some possible future improvements are:

* 💰 Total expense calculation
* 📊 Category-wise expense summary
* 📅 Date-based filtering
* 🗃️ SQLite database
* 📈 Spending reports
* 📊 Expense visualization
* 🖥️ GUI version
* 🔐 Better input validation
* 💵 Monthly budget tracking
* 📅 Monthly expense reports
* 📤 Export expenses to CSV
* 🔎 Advanced expense filtering

---

## 🎯 Project Goal

The main goal of **Expense-li** was not to build a complicated financial application.

It was to understand how Python can be used to build a **real, interactive application from scratch**.

Starting with basic CRUD operations and now adding data persistence, the project has evolved through:

```text
Create
   ↓
Read
   ↓
Update
   ↓
Delete
   ↓
Save
   ↓
Load
```

This project helped me understand the fundamentals of **CRUD logic, functions, file handling, and persistent data storage in Python**.

---

## 🐍 My Python Journey

This project is part of my journey of learning Python through small practical projects.

```text
📝 To-Do List
      ↓
🌦️ Weather App
      ↓
🔐 Password Generator
      ↓
🎯 Number Guessing Game
      ↓
📞 Contact Book
      ↓
💸 PyExpenseTracker
      ↓
💾 Data Persistence
      ↓
🚀 More projects coming...
```

---

## ☕ Made With

```text
☕ A cup of coffee

🐍 Python

🧠 Debugging

💻 Lots of practice
```

---

### ⭐ If you like this project, consider giving it a star!

**Made with 🐍 + 💻**
