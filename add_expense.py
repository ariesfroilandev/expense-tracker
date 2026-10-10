import csv
from expense_categories import show_expense_categories, get_category_list
from datetime import datetime
from decimal import Decimal, InvalidOperation
import storage

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
            value = Decimal(amount)
            if value < 1:
                raise ValueError("Amount must be greater than zero.")
            
        except InvalidOperation: 
            raise ValueError("Input must be a number.") from None

        self._amount = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not validate_date(date):  
            raise ValueError("Invalid input. Date format (MM/YYYY)") from None

        self._date = date

    @classmethod
    def get(cls):
        ...

    

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
            amount = Decimal(input("Amount: "))
            if amount < 1:
                print("Amount must be greater than zero.")
                continue

            break

        except InvalidOperation:
            print("Invalid input.")


    # Input validation for date
    while True:
        date = input("Date(MM/YYYY): ")

        if validate_date(date):
            break

        print("Invalid input. Date format should be (MM/YYYY)")

    note = input("Note: ")
    
    expense = Expense(category, amount, date, note)
    storage.add_expense("expenses.csv", expense)
    print("Expense added")


# input/data validation for date
def validate_date(date):
    try:
        datetime.strptime(date, "%m/%Y")
        return True
    except ValueError:
        return False
