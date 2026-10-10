from datetime import datetime
from decimal import Decimal, InvalidOperation
from storage import read_csvfile, add_budget
from utils import format_date, yes_no_loop, get_amount_date


def show_budget():
    print("=======================")
    print("        BUDGET")
    print("=======================")
    budget = get_budget()
    # Asks user to enter budget if no data was entered before
    if not budget:
        print("No monthly budget previously saved.")

        # Loop for input validation
        confirm = yes_no_loop("Would you like to enter this month's budget?[y/n]: ")

        if confirm == "y":
            input_budget()

        return

    for row in budget:
        print(f"Date: {format_date(row['date'])}")
        print(f"Budget: ${Decimal(row['budget']):,.2f}")
        print("=======================")

    add = yes_no_loop("Would you like to add a new budget? [y/n]: ")
    if add == "n":
        return

    input_budget()


# Get budget records from from csv file
def get_budget():
    return read_csvfile("budget.csv")


def input_budget():
    if not (record := get_amount_date()):
        return
    
    budget, date = record
    
    add_budget("budget.csv", date, budget)
    print("=======================")
    print("Budget successfully added.")
    print("=======================")
    input()


def current_budget():
    budget_list = get_budget()
    today = datetime.today()
    today = today.strftime("%m/%Y")

    for budget in budget_list:
        if budget["date"] == today:
            return budget
