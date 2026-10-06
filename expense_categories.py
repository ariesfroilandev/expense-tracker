expense_categories = [
    "Food",
    "Transportation",
    "Bills",
    "Shopping",
    "Entertainment",
    "Health",
    "Others",
    ]


def show_expense_categories():
    print("================")
    print("   CATEGORIES   ")
    print("================")
    # Display list of categories
    for category in expense_categories:
        print(category)

    print("================")

    while True:
        print("[1] to add a new category")
        print("[2] to go back to main menu")

        try:
            option = int(input("Select an option: "))

        except ValueError:
            print("Invalid option. Try Again")
            continue

        if 0 < option < 3:
            return option

        print("Invalid option. Try Again")
