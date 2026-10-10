from datetime import datetime

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