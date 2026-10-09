from datetime import datetime
from budget import current_budget
from expense_history import get_expenses


def get_dashboard():
    print("=======================")
    print("       DASHBOARD")
    print("=======================")

    date, budget = current_budget().values()
    date = format_date(date)
    print(f"{date.upper()}")
    print(f"Budget: ${float(budget):,.2f}")

    current_expenses = get_current_expenses()
    if current_expenses == 0:
        print(f"Total Expenses: 0.00")
    else:
        print(f"Total Expenses: {float(current_expenses):,.2f}")
        
    remaining_budget = get_remaining_budget(float(budget), float(current_expenses))
    print(f"Remaining Budget: {remaining_budget:,.2f}")

    input()


# Format date from (eg. 10/2026 to October 2026)
def format_date(old):
    new = datetime.strptime(old, "%m/%Y")
    return new.strftime("%B %Y")


def get_current_expenses():
    expenses = get_expenses()
    if expenses == "empty":
        return 0

    total_expenses = 0
    for row in expenses:
        total_expenses += float(row["amount"])

    return total_expenses


def get_remaining_budget(budget, expenses):
    return budget - expenses
