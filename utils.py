from datetime import datetime
from storage import read_csvfile

# Format date from (eg. 10/2026 to October 2026)
def format_date(old):
    new = datetime.strptime(old, "%m/%Y")
    return new.strftime("%B %Y")


def yes_no_loop(question):
    while True:
        confirm = input(question).lower()
        if confirm == "y" or confirm == "n":
            return confirm

        print("Invalid input. Try Again.")


def x_selected(option):
    if option.lower() == "x":
        return True

    return False


# input/data validation for date
def validate_format(date):
    try:
        datetime.strptime(date, "%m/%Y")
        return True
    except ValueError:
        return False


def fix_date_format(date):
    return datetime.strptime(date, "%m/%Y").strftime("%m/%Y")


def get_options(options):
    option_description = ""
    # Display menu_options
    for option in options.values():
        option_description = option_description + option + "\n"

    return option_description


def select_and_validate(options):
    while True:
        try:
            selected_option = int(input("Select an option: "))

        except ValueError:
            print("Invalid option. Try Again")
            continue

        if 0 < selected_option <= len(options):
            return selected_option

        print("Invalid option. Try Again")


def match_dates(budget_list, date):
    for row in budget_list:
        if row["date"] == date:
            return True
        
    return False


# Get budget records from from csv file
def get_budget_list():
    return read_csvfile("budget.csv")