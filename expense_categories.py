category_options = {
    1 : "[1] to add a new category",
    2 : "[2] to go back to main menu",
}


def show_expense_categories(read_only=False):
    print("=======================")
    print("      CATEGORIES   ")
    print("=======================")

    # Display list of categories from txt file
    
    category_list = get_category_list()
    for category in category_list:
        print(category)

    print("=======================")

    # Condition for when function is called only to show categories 
    if not read_only:
        while True:
            # Display menu_options
            for option in category_options.values():
                print(option)

            try:
                selected_option = int(input("Select an option: "))

            except ValueError:
                print("Invalid option. Try Again")
                continue

            # Checks which action to do next based on selected option
            if selected_option == len(category_options):
                return

            match selected_option:
                case 1:
                    add_category()
                

def add_category():
    new_category = input("Type new category: ").lower()

    # Append new category to txt file
    with open("expense_categories.txt", "a") as file:
        file.write(f"{new_category}\n")

    print("Category added.")


# get category list, remove whitespaces and capitalize
def get_category_list():
    with open("expense_categories.txt") as file:
        return [items.strip().capitalize() for items in file]