import csv
from budget import read_file


def show_expenses():
    print("=======================")
    print("    EXPENSE HISTORY")
    print("=======================")
    
    rows = get_expenses()
    if rows == "empty":
        print("No expenses recorded.")

    else:
        for row in rows:
            print(f"Amount: ${float(row['amount']):,.2f}")
            print(f"Category: {row['category']}")
            print(f"Date: {row['date']}")
            print(f"Note: {row['note']}")
            print("=======================")

    input()


def get_expenses():
    return read_file("expenses.csv")