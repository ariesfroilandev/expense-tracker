from datetime import datetime
from decimal import Decimal
from storage import save_budget, update_budget_file
from utils import *
from classes import FinancialRecord


options = {
    1 : "[1] Add a new budget",
    2 : "[2] Update existing budget",
    3 : "[3] Go back to main menu",
}


def show_budget():
    print("=======================")
    print("        BUDGET")
    print("=======================")
    budget_list = get_budget_list()
    # Asks user to enter budget if no data was entered before
    if not budget_list:
        print("No monthly budget previously saved.")

        # Loop for input validation
        confirm = yes_no_loop("Would you like to enter this month's budget?[y/n]: ")

        if confirm == "y":
            add_budget()

        return

    for row in budget_list:
        print(f"Date: {format_date(row['date'])}")
        print(f"Budget: ${Decimal(row['amount']):,.2f}")
        print("=======================")

    print(get_options(options), end="")
    selected_option = select_and_validate(options)
    if selected_option == len(options):
        return

    match selected_option:
        case 1:
            add_budget()
        case 2:
            update_budget(budget_list)


def add_budget(budget_input=None):
    if not budget_input:
        if not (budget_input := FinancialRecord.get_input()):
            return

    save_budget("budget.csv", budget_input.date, budget_input.amount)

    print("=======================")
    print("Budget successfully added.")
    print("=======================")
    input()


def get_budget(date=None):
    budget_list = get_budget_list()

    if not date:
        date = datetime.today()
        date = date.strftime("%m/%Y")

    for budget in budget_list:
        if budget["date"] == date:
            return budget


def update_budget(budget_list):
    if not (budget_input := FinancialRecord.get_input()):
        return

    if not match_dates(budget_list, budget_input.date):
        print(f"No existing budget recorded for {budget_input.date}.")
        confirm = yes_no_loop(f"Would you like to add a budget for {budget_input.date}? [y/n]: ")

        if confirm == "n":
            return

        add_budget(budget_input)
        return

    for row in budget_list:
        if row["date"] == budget_input.date:
            row["amount"] = budget_input.amount

    update_budget_file(budget_list)
    print("=======================")
    print("Budget successfully updated.")
    print("=======================")
    input()
