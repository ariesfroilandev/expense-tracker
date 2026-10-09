import csv

def show_expenses():
    print("=======================")
    print("    EXPENSE HISTORY")
    print("=======================")
    with open("expenses.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
                print(f"Amount: ${float(row['amount']):,.2f}")
                print(f"Category: {row['category']}")
                print(f"Date: {row['date']}")
                print(f"Note: {row['note']}")
                print("=======================")

    input()