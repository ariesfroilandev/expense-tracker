expense_categories = [
    "Food",
    "Transportation",
    "Bills",
    "Shopping",
    "Entertainment",
    "Health",
    "Others",
]

menu_options = {
    1 : "[1] to add a new category",
    2 : "[2] to go back to main menu",
}


def show_expense_categories():
    print("================")
    print("   CATEGORIES   ")
    print("================")
    # Display list of categories
    for category in expense_categories:
        print(category)

    print("================")

    while True:
        # Display menu_options
        for option in menu_options.values():
            print(option)

        try:
            selected_option = int(input("Select an option: "))

        except ValueError:
            print("Invalid option. Try Again")
            continue

        if 0 < selected_option < 3:
            return selected_option

        print("Invalid option. Try Again")
