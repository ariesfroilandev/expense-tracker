from datetime import datetime
from decimal import Decimal, InvalidOperation
from storage import read_csvfile, add_budget


def show_budget():
    print("=======================")
    print("        BUDGET")
    print("=======================")
    budget = get_budget()
    # Asks user to enter budget if no data was entered before
    if not budget:
        print("No monthly budget previously saved.")
        # loop for input validation
        while True:
            confirm = input("Would you like to enter this month's budget?[y/n]: ").lower()
            if confirm == "y" or confirm == "n":
                break

            print("Invalid input. Try Again.")

        if confirm == "y":
            input_budget()

        return

    for row in budget:
        print(f"Date: {row['date']}")
        print(f"Budget: ${Decimal(row['budget']):,.2f}")

    input()
    

# Get budget records from from csv file
def get_budget():
    return read_csvfile("budget.csv")


def input_budget():
    # Input Validation for budget
    while True:
        try:
            budget = Decimal(input("Budget Amount: "))
            if budget < 0:
                print("Please enter valid amount.")
            else:
                break
        except InvalidOperation:
            print("Invalid input. Try again.")

    # Input validation for date
    while True:    
        date = input("Confirm date this budget is for (MM/YYYY): ")
        try:
            datetime.strptime(date, "%m/%Y")
            break
        except:
            print("Invalid date. Try again.")

    add_budget("budget.csv", date, budget)

    print("Budget successfully added.")


def current_budget():
    budget_list = get_budget()
    today = datetime.today()
    today = today.strftime("%m/%Y")

    for budget in budget_list:
        if budget["date"] == today:
            return budget
