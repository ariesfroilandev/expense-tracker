from datetime import datetime
from budget import read_file


def get_dashboard():
    print("=======================")
    print("       DASHBOARD")
    print("=======================")

    budget = current_budget(read_file("budget.csv"))
    date = format_date(budget["date"])
    print(date.upper())
    print(f"Budget: ${float(budget["budget"]):,.2f}")
    print(f"Total Expenses: ")

    input()


def current_budget(budget_list):
    today = datetime.today()
    today = today.strftime("%m/%Y")

    for budget in budget_list:
        if budget["date"] == today:
            return budget


def format_date(old):
    new = datetime.strptime(old, "%m/%Y")
    return new.strftime("%B %Y")


def get_current_expenses():
    ...