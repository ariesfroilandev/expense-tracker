from decimal import Decimal
from expenses import get_expenses


def get_total_expenses(date=None):
    expenses = get_expenses(date)
    total_expenses = Decimal("0.00")
    
    if not expenses:
        return total_expenses
    
    for row in expenses:
        total_expenses += Decimal(row["amount"])

    return total_expenses


def get_remaining_budget(budget, expenses):
    return Decimal(budget) - Decimal(expenses)
