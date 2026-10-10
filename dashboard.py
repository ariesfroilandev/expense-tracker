from datetime import datetime
from budget import current_budget
from decimal import Decimal
from services import get_total_expenses, get_remaining_budget, format_date


def get_dashboard():
    print("=======================")
    print("       DASHBOARD")
    print("=======================")

    budget_dict = current_budget()
    # Checks if budget returns a value
    if budget_dict is None:
        print("No budget set for this month.")
        input()
        return

    # Unpack budget_dict
    date, budget = budget_dict.values()
    date = format_date(date)

    print(f"{date.upper()}")
    print(f"Budget: ${Decimal(budget):,.2f}")

    current_expenses = get_total_expenses()
    if current_expenses == 0:
        print(f"Total Expenses: $0.00")
    else:
        print(f"Total Expenses: ${Decimal(current_expenses):,.2f}")

    # Returns the remaining budget value as Decimal
    remaining_budget = get_remaining_budget(budget, current_expenses)
    print(f"Remaining Budget: ${remaining_budget:,.2f}")

    input()
