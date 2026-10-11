from decimal import Decimal
from expenses import get_current_expenses


def get_total_expenses():
    expenses = get_current_expenses()
    if not expenses:
        return 0

    total_expenses = Decimal("0.00")
    for row in expenses:
        total_expenses += Decimal(row["amount"])

    return total_expenses


def get_remaining_budget(budget, expenses):
    return Decimal(budget) - Decimal(expenses)
