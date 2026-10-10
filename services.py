from storage import read_csvfile
from decimal import Decimal
from datetime import datetime

def get_total_expenses():
    expenses = get_expenses()
    if not expenses:
        return 0

    total_expenses = Decimal("0.00")
    for row in expenses:
        total_expenses += Decimal(row["amount"])

    return total_expenses


def get_expenses():
    return read_csvfile("expenses.csv")


def get_remaining_budget(budget, expenses):
    return Decimal(budget) - Decimal(expenses)


def x_selected(option):
    if option.lower() == "x":
        return True

    return False


# Format date from (eg. 10/2026 to October 2026)
def format_date(old):
    new = datetime.strptime(old, "%m/%Y")
    return new.strftime("%B %Y")


def yes_no_loop(question):
    while True:
        confirm = input(question).lower()
        if confirm == "y" or confirm == "n":
            return confirm

        print("Invalid input. Try Again.")