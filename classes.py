from datetime import datetime
from utils import validate_format, x_selected, get_financial_record
from decimal import Decimal, InvalidOperation
from expense_categories import get_category_list, show_expense_categories
import storage

class FinancialRecord():
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not validate_format(date):  
            raise ValueError("Invalid input. Date format (MM/YYYY)") from None

        self._date = date

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


    @classmethod
    def get(cls):
        ...


class Expense(FinancialRecord):
    def __init__(self, category, amount, date, note):
        super().__init__(date, amount)
        self.category = category
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

    @classmethod
    def add(cls):
        print("=======================")
        print("      ADD EXPENSE")
        print("=======================")

        if not (record := get_financial_record()):
            return

        amount, date = record

        show_expense_categories(True)
        category_list = get_category_list()
        # Input validation for category
        while True:
            category = input("Category: ").strip().capitalize()
            if x_selected(category):
                return
            
            if category in category_list:
                break

            print("Category not on the list. Please pick an existing category or add a new category to the list.")

        note = input("Note: ")

        if x_selected(note):
            return
        
        expense = cls(category, amount, date, note)
        storage.add_expense("expenses.csv", expense)
        print("=======================")
        print("Expense added")
        print("=======================")
        input()
   