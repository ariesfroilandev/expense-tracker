import csv
import re
from expense_categories import show_expense_categories


def add_expense():
    print("=======================")
    print("      ADD EXPENSE")
    print("=======================")

    while True:
        try: 
            amount = int(input("Amount: "))
            break
        except ValueError:
            print("Invalid input")

    show_expense_categories(True)

    # Assign list from txt file and remove whitespaces
    with open("expense_categories.txt") as file:
        category_list = [item.strip() for item in file.readlines()]

    while True:
        category = input("Category: ")
        if category in category_list:
            break

        print("Invalid input")

    
    date = input("Date(MM-DD-YYYY): ")
    note = input("Note: ")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date, note])