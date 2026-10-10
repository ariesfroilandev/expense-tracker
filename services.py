from storage import read_csvfile
from decimal import Decimal


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