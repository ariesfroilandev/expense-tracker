from budget import get_budget
from decimal import Decimal
from services import get_total_expenses, get_remaining_budget
from utils import format_date, get_options, select_and_validate, validate_format, fix_date_format
from datetime import datetime


options = {
    1: "[1] Select month",
    3: "[2] Go back to main menu"
}


def dashboard():
    print("=======================")
    print("       DASHBOARD")
    print("=======================")
    get_monthly_report("current")
    while True:
        print(get_options(options), end="")
        selected_option = select_and_validate(options)
        if selected_option == len(options):
            return

        match selected_option:
            case 1:
                get_monthly_report("specific")


def get_monthly_report(month):
    if month == "specific":
        while True:
            date = input("Enter date(MM/YYYY): ")
            if validate_format(date):
                date = fix_date_format(date)
                break

            print("Invalid input. Date format should be (MM/YYYY)")
        budget = get_budget(date)

    elif month == "current":
        date = datetime.today()
        date = date.strftime("%m/%Y")
        budget = get_budget()

    # Checks if budget returns a value
    if budget is None:
        print("=======================")
        print("No budget set for this month.")
        print("=======================")
        return

    budget_date, budget_amount = budget.values()
    budget_date = format_date(budget_date)

    print("=======================")
    print(f"{budget_date.upper()}")
    print(f"Budget: ${Decimal(budget_amount):,.2f}")

    expenses = get_total_expenses(date)
    if expenses == 0:
        print(f"Total Expenses: $0.00")
    else:
        print(f"Total Expenses: ${Decimal(expenses):,.2f}")

    # Returns the remaining budget value as Decimal
    remaining_budget = get_remaining_budget(budget_amount, expenses)
    print(f"Remaining Budget: ${remaining_budget:,.2f}")
    print("=======================")