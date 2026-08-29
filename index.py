Expenses = []

def AddExpenses():

    title = input("Expense for (breakfat/lunch/dinner/etc) :")
    amount = float(input("Enter the amount :"))
    date = input("Enter the date: ")
    category = input("Enter category (food/healthcare/daily-needs/etc) : ")

    item = {
        'id' : len(Expenses) + 1,
        'title' : title,
        'amount' : amount,
        'date' : date,
        'category' : category
    }

    Expenses.append(item)

    print("Expense Sucessfully registered!!")


def ViewExpenses():

    print("\n===============================")
    print("        My-Expense-list          ")
    print("===============================")

    for item in Expenses:

        DisplayExpenses(item)

        print("===============================")


def DisplayExpenses(item):
     
     print(f"\nid : {item['id']}")
     print(f"title : {item['title']}")
     print(f"amount : {item['amount']}")
     print(f"date : {item['date']}")
     print(f"category : {item['category']}")
    

def SearchExpenses():

    searchFor = int(input("Search with Id{1}, title{2}, amount{3}, date{4}, category{5}: " ))

    if searchFor == 1:

        SearchId = int(input("Enter id for expense : "))

        for item in Expenses:

            if SearchId == item['id']:

                DisplayExpenses(item)

                return

        print(f"Could not find item with Id: {SearchId}")

    elif searchFor == 2:

        SearchTitle = input("Enter title for expense : ")

        for item in Expenses:

            if SearchTitle == item['title']:

                DisplayExpenses(item)

                return

        print(f"Could not find item with Title: {SearchTitle}")

    elif searchFor == 3:

        searchAmount = float(input("Enter amount for expense : "))

        for item in Expenses:

            if searchAmount == item['amount']:

                DisplayExpenses(item)

                return

        print(f"Could not find item with Amount: {searchAmount}")

    elif searchFor == 4:

        SearchDate = input("Enter Date for expense : ")

        for item in Expenses:

            if SearchDate == item['date']:

                DisplayExpenses(item)

                return

        print(f"Could not find item with Date: {SearchDate}")

    elif searchFor == 5:

        searchCategory  = input("Enter Category for Expense : ")

        for item in Expenses:

            if searchCategory == item['category']:

                DisplayExpenses(item)

                return

        print(f"Could not find item with Category: {searchCategory}")

def UpdateExpenses():

    UpdateId = int(input("Enter expense ID to Update : "))

    for item in Expenses:

        if UpdateId == item['id']:

            updateFor = int(input("Update Title{1}, Amount{2}, Date{3}, Category{4}"))

            if updateFor == 1:
                 
                 newTitle = input("Enter new title : ")
                 item['title'] = newTitle

            elif updateFor == 2:

                newAmount = float(input("Enter new amount :"))
                item['amount'] = newAmount

            elif updateFor == 3:

                newDate = input("Enter new date : ")
                item['date'] = newDate

            elif updateFor == 4:

                newCategory = input("Enter new Category : ")
                item['category'] = newCategory

            print("Expense Updated Succesfullyy !!")
            return
        
    print(f"Soryy! Could not find expense with ID : {UpdateId} ")

def DeleteExpense():

    DeleteId = int(input("Enter Id to delete Expense :"))

    for item in Expenses:

        if DeleteId == item['id']:

            Confirm = input("Are You Sure You Want To Delete This Expnese ( yes{y}/No{n}) : ")

            if Confirm == "y":

                Expenses.remove(item)
                print("Expense Deleted Succesfully !!")
                return

            elif Confirm == "n":

                print("Cancelled deletion!!")
                return

            else:
                print("invalid Choice!!")
                return
            
    print(f"Could not find expense with ID: {DeleteId}")

while True :

    print("\n=====================")
    print("      Expense-li       ")
    print("=======================")
    print("1. Add New Expense")
    print("2. View Expense List")
    print("3. Search Expense")
    print("4. Update Existing Expense")
    print("5. Delete Expense")
    print("=======================")

    ExpenseTask = int(input("select task (1{1},2{2},3{3},4{4},5{5}):  "))

    if ExpenseTask == 1:
        AddExpenses()
    elif ExpenseTask == 2:
        ViewExpenses()
    elif ExpenseTask == 3:
        SearchExpenses()
    elif ExpenseTask == 4:
        UpdateExpenses()
    elif ExpenseTask == 5:
        DeleteExpense()
    else :
        print("Invalid Task!!")
        break







    
