import sys
from expense_categories import show_expense_categories
from add_expense import add_expense
from expense_history import show_expenses
from budget import show_budget
from dashboard import get_dashboard
from classes import Expense


# Dictionary for menu options and their functions
menu_options = {
    1 : ["[1] Dashboard", get_dashboard],
    2 : ["[2] Add Expense", Expense.add],
    3 : ["[3] Expense History", show_expenses],
    4 : ["[4] Expense Categories", show_expense_categories],
    5 : ["[5] Budget", show_budget],
    6 : ["[6] Exit", sys.exit],
}


def main():
    # Index 1 to call the function in menu_option
    call_function = 1

    while True:
        print("=======================")
        print("    EXPENSE TRACKER")
        print("=======================")
        select = main_menu()
        menu_options[select][call_function]()


# Display options in main menu
def main_menu():
    # Index 0 for description of the menu_option
    description = 0
    
    for option in menu_options.values():
        print(option[description])

    # Input validation for selecting menu option
    while True:
        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if option in menu_options:
            return option

        print("Invalid option. Try again.")


if __name__ == "__main__":
    main()