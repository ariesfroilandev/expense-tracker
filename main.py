import sys
from expense_categories import show_expense_categories
from expenses import show_expenses, expense_add
from budget import show_budget
from dashboard import dashboard
from utils import select_and_validate


# Dictionary for menu options and their functions
menu_options = {
    1 : ["[1] Dashboard", dashboard],
    2 : ["[2] Add Expense", expense_add],
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
    return select_and_validate(menu_options)


if __name__ == "__main__":
    main()