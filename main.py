expense_categories = [
    "Food",
    "Transportation",
    "Bills",
    "Shopping",
    "Entertainment",
    "Health",
    "Others",
    ]


def main():
    main_menu()


# Display options in main menu
def main_menu():
    print("[1] Dashboard")
    print("[2] Add Expense")
    print("[3] Expense History")
    print("[4] Expense Categories")
    print("[5] Monthly Budget")
    return input("Select Option: ")


def show_expense_categories():
    for category in expense_categories:
        print(category)

main()