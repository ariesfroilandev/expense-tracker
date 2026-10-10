from datetime import datetime
from decimal import Decimal, InvalidOperation

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

# Asks user for amount and date
def get_financial_record():
    print("Input [x] anytime to cancel and go back to main menu.")
    # Input validation for amount
    while True:
        amount_input = input("Amount: ")
        if x_selected(amount_input):
            return
        
        try:
            amount = Decimal(amount_input)
            if amount.is_finite() and amount > 0:
                break
            
        except InvalidOperation:
            print("Invalid input.")

        print("Please enter a valid amount.")

    # Input validation for date
    while True:
        date = input("Date(MM/YYYY): ")

        if x_selected(date):
            return

        if validate_format(date):
            break

        print("Invalid input. Date format should be (MM/YYYY)")

    return amount, date