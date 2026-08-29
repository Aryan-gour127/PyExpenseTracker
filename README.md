
# 💸 PyExpenseTracker - CLI

````
Expense-li is a simple **CLI-based expense management application** that helps you add, view, search, update, and delete your daily expenses.

This project was created as a Python project to practice **lists, dictionaries, functions, loops, conditions, CRUD operations, and menu-driven programs**. ✨

````
---

````
#🌸 Features

### ➕ Add Expenses
Add a new expense with:

- 🍽️ Expense title
- 💰 Amount
- 📅 Date
- 🏷️ Category
- 🆔 Automatically generated ID

Example:

Expense for (breakfast/lunch/dinner/etc): Lunch
Enter the amount: 150
Enter the date: 29-08-2026
Enter category (food/healthcare/daily-needs/etc): Food

Expense Successfully registered!!
````

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

## 🧠 What I Learned

Building this project helped me practice:

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

---

## 🏗️ Project Structure

```text
Expense-li/
│
├── index.py
│
└── README.md
```

---

## 🎮 How It Works

When the program starts, you get a simple menu:

```text
=======================
      Expense-li
=======================
1. Add New Expense
2. View Expense List
3. Search Expense
4. Update Existing Expense
5. Delete Expense
=======================
select task:
```

Choose an option and manage your expenses directly from the terminal. 💻✨

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Aryan-gour127/PyExpenseTracker
```

### 2️⃣ Open the project

```bash
cd PyExpenseTrackers
```

### 3️⃣ Run the program

```bash
python index.py
```

That's it! 

---

## 🛠️ Tech Used

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| 🐍 Python       | Main programming language |
| 💻 CLI          | User interface            |
| 📦 Lists        | Store expenses            |
| 📖 Dictionaries | Store expense information |
| 🔧 Functions    | Organize program logic    |

---

## 🌱 Future Improvements

This is currently a beginner-friendly version, but there are lots of things I can add later:

* 💰 Total expense calculation
* 📊 Category-wise expense summary
* 📅 Date-based filtering
* 💾 Save expenses to JSON
* 📂 Load expenses from JSON
* 🗃️ SQLite database
* 📈 Spending reports
* 🖥️ GUI version
* 🔐 Better input validation
* 💵 Monthly budget tracking

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

## 🎯 Project Goal

The main goal of **Expense-li** was not to build a complicated financial application.

It was to understand how Python can be used to build a **real, interactive application from scratch**.

From creating an expense ➕

to searching it 🔍

to updating it ✏️

to deleting it 🗑️

this project helped me understand the fundamentals of **CRUD logic in Python**.

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
💸 Expense-list
      ↓
🚀 More projects coming...
```

---

##  Made With

```text
☕ A cup of coffee
🐍 Python and
🧠 debugging
```

---

### ⭐ If you like this project, consider giving it a star!

**Made with 🐍 + 💻**

