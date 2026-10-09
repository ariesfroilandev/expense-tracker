import csv
from datetime import datetime


def show_budget():
    print("=======================")
    print("        BUDGET")
    print("=======================")
    budget = get_budget()
    # Asks user to enter budget if no data was entered before
    if budget == "empty":
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
        print(f"Budget: ${float(row['budget']):,.2f}")

    input()
    

# Get budget records from from csv file
def get_budget():
    return read_file("budget.csv")


def read_file(csv_file):
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        # Returns row of data other than the fieldnames
        rows = list(reader)
        if not rows:
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


def current_budget():
    budget_list = get_budget()
    today = datetime.today()
    today = today.strftime("%m/%Y")

    for budget in budget_list:
        if budget["date"] == today:
            return budget
