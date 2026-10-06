import csv


def add_expense():
    print("===================")
    print("    ADD EXPENSE")
    print("===================")
    amount = input("Amount: ")
    category = input("Category: ")
    date = input("Date(MM-DD-YYYY): ")
    note = input("Note: ")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date, note])