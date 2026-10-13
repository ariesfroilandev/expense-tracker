from decimal import Decimal
from datetime import datetime
from storage import read_csvfile
from utils import get_options, select_and_validate, validate_format, yes_no_loop
from expense_categories import get_category_list


options = {
    1 : "[1] Filter by category",
    2 : "[2] Filter by date",
    3 : "[3] Go back to main menu",
}


def show_expenses():
    expense_list = get_all_expenses()
    while True:
        print("=======================")
        print("    EXPENSE HISTORY")
        print("=======================")
        
        if not expense_list:
            print("No expenses recorded.")
            input()
            return

        for row in expense_list:
            print(f"Amount: ${Decimal(row['amount']):,.2f}")
            print(f"Category: {row['category']}")
            print(f"Date: {row['date']}")
            print(f"Note: {row['note']}")
            print("=======================")
        
        print(get_options(options), end="")
        selected_option = select_and_validate(options)
        if selected_option == len(options):
            return

        match selected_option:
            case 1:
                expense_list = filter_expenses("category")
            case 2:
                expense_list = filter_expenses("date")


def get_expenses(date=None):
    all_expenses = get_all_expenses()
    expenses = []

    if not all_expenses:
        print("No expenses recorded.")
        return expenses

    if not date:
        date = datetime.today()
        date = date.strftime("%m/%Y")

    # Gets all expenses for the current month
    for row in all_expenses:
        if row["date"] == date:
            expenses.append(row)

    return expenses


def get_all_expenses():
    return read_csvfile("expenses.csv")


def filter_expenses(filter):
    if filter == "category":
        while True:
            input_filter = input(f"Enter {filter}: ").strip().capitalize()
            category_list = get_category_list()
            if input_filter in category_list:
                break
            print(f"{input_filter} is not on the category list.")
            exit = yes_no_loop("Would you like go back to the previous menu? [y/n]: ")
            if exit == "y":
                return

    elif filter == "date":
        while True:
            input_filter = input(f"Enter {filter}(MM/YYYY): ").strip()
            if validate_format(input_filter):
                break
            print("Invalid input.")

    rows = get_expenses()
    filtered_list = [
        row for row in rows
        if row[filter] == input_filter
        ]
    return filtered_list