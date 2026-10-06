import sys
from expense_categories import show_expense_categories


# Dictionary for menu options and their functions
menu_options = {
    1 : ["[1] Dashboard", None],
    2 : ["[2] Add Expense", None],
    3 : ["[3] Expense History", None],
    4 : ["[4] Expense Categories", show_expense_categories],
    5 : ["[5] Monthly Budget", None],
    6 : ["[6] Exit", sys.exit],
}


def main():
    # Index 1 to call the function in menu_option
    call_function = 1

    select = main_menu()
    menu_options[select][call_function]()



# Display options in main menu
def main_menu():
    for option in menu_options.values():
        print(option[0])
    return int(input("Select Option: "))


main()