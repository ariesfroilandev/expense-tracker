import csv
from expense_categories import show_expense_categories, get_category_list
from datetime import datetime
from decimal import Decimal, InvalidOperation
import storage
from services import x_selected

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
            if not value.is_finite() or value < 1:
                raise ValueError("Amount must not be infinite and must be greater than zero.")
            
        except InvalidOperation: 
            raise ValueError("Input must be a number.") from None

        self._amount = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not validate_format(date):  
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
    print("Input [x] anytime to cancel and go back to main menu.")
    while True:
        category = input("Category: ").strip().capitalize()
        if x_selected(category):
            return
        
        if category in category_list:
            break

        print("Category not on the list. Please pick an existing category or add a new category to the list.")
    
    # Input validation for amount
    while True:
        amount_input = input("Amount: ")
        if x_selected(amount_input):
            return
        
        try:
            amount = Decimal(amount_input)
            if not amount.is_finite() or amount < 1:
                print("Please enter a valid amount.")
                continue

            break

        except InvalidOperation:
            print("Invalid input.")

    # Input validation for date
    while True:
        date = input("Date(MM/YYYY): ")

        if x_selected(date):
            return

        if validate_format(date):
            break

        print("Invalid input. Date format should be (MM/YYYY)")

    note = input("Note: ")

    if x_selected(note):
        return
    
    expense = Expense(category, amount, date, note)
    storage.add_expense("expenses.csv", expense)
    print("Expense added")


# input/data validation for date
def validate_format(date):
    try:
        datetime.strptime(date, "%m/%Y")
        return True
    except ValueError:
        return False
