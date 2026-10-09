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
            value = float(amount)
        except ValueError: 
            raise ValueError("Input must be a float/integer.") from None
        
        if value < 1:
            raise ValueError("Amount must be greater than zero.")

        self._amount = round(value, 2)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not validate_date(date):  
            raise ValueError("Invalid input. Date format (MM/YYYY)") from None

        self._date = date
    

def add_expense():
    print("=======================")
    print("      ADD EXPENSE")
    print("=======================")

    show_expense_categories(True)
    category_list = get_category_list()
    # Input validation for category
    while True:
        category = input("Category: ").capitalize()
        if category in category_list:
            break

        print("Category not on the list. Please pick an existing category or add a new category to the list.")
    
    # Input validation for amount
    while True:
        try: 
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Invalid input.")

        if amount < 1:
            print("Amount must be greater than zero.")

    # Input validation for date
    while True:
        date = input("Date(MM/YYYY): ")

        if validate_date(date):
            break

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


# input/data validation for date
def validate_date(date):
    try:
        datetime.strptime(date, "%m/%Y")
        return True
    except ValueError:
        return False
