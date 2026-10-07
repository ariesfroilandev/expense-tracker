import csv

def show_expenses():
    print("=======================")
    print("    EXPENSE HISTORY")
    with open("expenses.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
                print("=======================")
                print(f"Amount: {row["amount"]}")
                print(f"Category: {row["category"]}")
                print(f"Date: {row["date"]}")
                print(f"Note: {row["note"]}")

    input()