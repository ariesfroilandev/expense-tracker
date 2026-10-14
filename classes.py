from utils import validate_format, x_selected, yes_no_loop, match_dates, get_budget_list, fix_date_format
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
            if not value.is_finite() or value <= 0:
                raise ValueError("Amount must not be infinite and must be greater than zero.")
            
        except InvalidOperation, ValueError: 
            raise ValueError("Input must be a number.") from None

        self._amount = value


    @classmethod
    def get(cls, update=False, for_expense_class=False):
        # set Param update to True if updating an existing budget
        # default Param False if adding a new budget
        print("Input [x] anytime to cancel and go back to main menu.")

        # Input validation for date
        while True:
            date = input("Enter date(MM/YYYY): ")

            if x_selected(date):
                return

            if validate_format(date):
                date = fix_date_format(date)
                break

            print("Invalid input. Date format should be (MM/YYYY)")

        if not for_expense_class:
            budget_list = get_budget_list()
            match = match_dates(budget_list, date)

            if not match and update:
                print(f"No existing budget recorded for {date}.")
                exit = yes_no_loop(f"Would you like to add a budget for {date}? [y/n]: ")

                if exit == "n":
                    return
                # update set to False to indicate the process is now adding instead of updating
                update = False

            if match and not update:
                print(f"Existing budget found for {date}.")
                if yes_no_loop(f"Would you like to update the budget for {date}? [y/n]: ") == "n":
                    return

                update = True

        # Input validation for amount
        while True:
            amount_input = input("Enter amount: ")
            if x_selected(amount_input):
                return
            
            try:
                amount = Decimal(amount_input)
            except InvalidOperation, ValueError:
                print("Invalid input.")
                continue

            if amount.is_finite() and amount > 0:
                break

            print("Please enter a valid amount.")

        return date, amount, update


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

        if not (record := super().get(for_expense_class=True)):
            return

        date, amount, _ = record

        show_expense_categories(True)
        category_list = get_category_list()
        # Input validation for category
        while True:
            category = input("Category: ").strip().capitalize()
            if x_selected(category):
                return
            
            if category in category_list:
                break

            print("Category not on the list. Please pick an existing category.")

        note = input("Note: ")

        if x_selected(note):
            return
        
        expense = cls(category, amount, date, note)
        storage.add_expense("expenses.csv", expense)
        print("=======================")
        print("Expense added")
        print("=======================")
        input()
   