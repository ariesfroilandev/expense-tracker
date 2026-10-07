import csv
from expense_categories import show_expense_categories, get_category_list
from datetime import datetime


def add_expense():
    print("=======================")
    print("      ADD EXPENSE")
    print("=======================")

    # Input validation for amount
    while True:
        try: 
            amount = int(input("Amount: "))
            break
        except ValueError:
            print("Invalid input")

    show_expense_categories(True)

    category_list = get_category_list()

    # Input validation for category
    while True:
        category = input("Category: ")
        if category in category_list:
            break

        print("Invalid input")

    # Input validation for date
    while True:
        date = input("Date(MM-DD-YYYY): ")

        try:
            datetime.strptime(date, "%m-%d-%Y")
            break
        except:
            print("Invalid input")

    note = input("Note: ")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date, note])

    print("Expense added")