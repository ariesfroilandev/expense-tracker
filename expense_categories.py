import storage

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
    if not category_list:
        print("No existing category.")

    else:    
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

            if selected_option > len(category_options):
                print("Invalid option. Try Again")
                continue

            # Checks which action to do next based on selected option
            if selected_option == len(category_options):
                return

            match selected_option:
                case 1:
                    add_category()
                

def add_category():
    while True:
        # Validate if input is just whitespace
        new_category = input("Type new category: ").strip()

        if new_category:
            category_list = get_category_list()

            # Breaks from loop if list is empty
            if not category_list:
                break

            # Breaks from loop if new catergory is not on the existing category list
            if not (new_category.capitalize() in category_list):
                break

            print("Category already on the list.")
            continue

        print("Category can't be blank.")
            
    storage.add_category("expense_categories.txt", new_category)
    print("Category added.")


# Get category list and remove whitespaces
def get_category_list():
    return storage.read_txtfile("expense_categories.txt")
