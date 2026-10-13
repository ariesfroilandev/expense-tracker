from datetime import datetime
from decimal import Decimal
from storage import read_csvfile, add_budget, update_budget_file
from utils import format_date, yes_no_loop, get_options, select_and_validate, get_budget_list
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
    budget = get_budget_list()
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
        print(f"Budget: ${Decimal(row['amount']):,.2f}")
        print("=======================")

    print(get_options(options), end="")
    selected_option = select_and_validate(options)
    if selected_option == len(options):
        return

    match selected_option:
        case 1:
            input_budget(budget)
        case 2:
            update_budget(budget)


def input_budget(budget_list=[]):
    if not (record := FinancialRecord.get()):
        return
    
    date, amount, update_status = record

    if update_status:
        for row in budget_list:
            if row["date"] == date:
                row["amount"] = amount
                
        update_budget_file(budget_list)

    else:
        add_budget("budget.csv", date, amount)

    print("=======================")
    print("Budget successfully added.")
    print("=======================")
    input()


def current_budget():
    budget_list = get_budget_list()
    today = datetime.today()
    today = today.strftime("%m/%Y")

    for budget in budget_list:
        if budget["date"] == today:
            return budget


def update_budget(budget_list):
    if not (record := FinancialRecord.get(True)):
        return

    date, amount, update_status = record
    for row in budget_list:
        if row["date"] == date:
            row["amount"] = amount

    if update_status == False:
        add_budget("budget.csv", date, amount)
        print("=======================")
        print("Budget successfully added.")
        print("=======================")
        input()
        return

    update_budget_file(budget_list)
    print("=======================")
    print("Budget successfully updated.")
    print("=======================")
    input()
