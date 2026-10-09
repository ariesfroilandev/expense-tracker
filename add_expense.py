import csv
from expense_categories import show_expense_categories, get_category_list
from datetime import datetime

class Expense():
    def __init__(self, category, amount, date, note):
        self.category = category
        self.amount = amount
        self.date = date
        self.note = note
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        category_list = get_category_list()
        if category not in category_list:
            raise ValueError("Category not on the list")
        
        self._category = category

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        try:
            value = int(amount)
        except ValueError: 
            raise ValueError("Input must be a number.") from None
        
        if value < 1:
            raise ValueError("Amount must be greater than zero.")

        self._amount = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        try:
            datetime.strptime(date, "%m/%Y")
        except ValueError:
            raise ValueError("Invalid input") from None

        self._date = date
    

def add_expense():
    print("=======================")
    print("      ADD EXPENSE")
    print("=======================")

    show_expense_categories(True)
    category_list = get_category_list()
    # Input validation for category
    while True:
        category = input("Category: ")
        if category in category_list:
            break

        print("Category not on the list. Please pick an existing category or add a new category to the list.")
    
    # Input validation for amount
    while True:
        try: 
            amount = int(input("Amount: "))
            break
        except ValueError:
            print("Invalid input")

    # Input validation for date
    while True:
        date = input("Date(MM/YYYY): ")

        try:
            datetime.strptime(date, "%m/%Y")
            break
        except:
            print("Invalid input. Date format should be (MM/YYYY)")

    note = input("Note: ")
    
    expense = Expense(category, amount, date, note)
    
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount", "date", "note"])
        writer.writerow({
            "category": expense.category, 
            "amount": expense.amount,
            "date": expense.date,
            "note": expense.note,
            })

    print("Expense added")
