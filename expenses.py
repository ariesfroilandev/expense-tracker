from decimal import Decimal
from datetime import datetime
from storage import read_csvfile


options = {
    1 : "[1] Filter by category",
    2 : "[2] Filter by date",
    3 : "[3] Go back to main menu",
}


def show_expenses():
    print("=======================")
    print("    EXPENSE HISTORY")
    print("=======================")
    
    rows = get_expenses()
    if not rows:
        print("No expenses recorded.")
        input()
        return

    for row in rows:
        print(f"Amount: ${Decimal(row['amount']):,.2f}")
        print(f"Category: {row['category']}")
        print(f"Date: {row['date']}")
        print(f"Note: {row['note']}")
        print("=======================")

    input(get_options())


def get_options():
    option_description = ""
    for option in options.values():
        option_description = option_description + option + "\n"

    return option_description


def get_current_expenses():
    all_expenses = get_expenses()
    if not all_expenses:
        print("No expenses recorded.")

    today = datetime.today()
    today = today.strftime("%m/%Y")

    expenses = []
    # Gets all expenses for the current month
    for row in all_expenses:
        if row["date"] == today:
            expenses.append(row)

    return expenses


def get_expenses():
    return read_csvfile("expenses.csv")