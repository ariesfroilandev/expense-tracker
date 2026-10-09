import csv
from datetime import datetime


def show_budget():
    print("=======================")
    print("        BUDGET")
    print("=======================")
    budget = get_budget()

    # Asks user to enter budget if no data was entered before
    if budget == "empty":
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
        print(f"Budget: {row['budget']}")

    input()
    


# Get budget records from from csv file
def get_budget():
    with open("budget.csv") as file:
        reader = csv.DictReader(file)

        # Checks if csv file have budget data other than the fieldnames
        rows = list(reader)
        if not rows:
            print("No monthly budget previously saved.")
            return "empty"

        return rows


def input_budget():
    # Input Validation for budget
    while True:
        try:
            budget = int(input("Budget Amount: "))
            break
        except ValueError:
            print("Invalid input. Try Again.")

    # Input validation for date
    while True:    
        date = input("Confirm date this budget is for (MM/YYYY): ")
        try:
            datetime.strptime(date, "%m/%Y")
            break
        except:
            print("Invalid input. Try Again")


    with open("budget.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "budget"])
        writer.writerow({
            "date": date,
            "budget": budget
            })
