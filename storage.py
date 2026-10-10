import csv

def read_csvfile(file_name):
    try:
        with open(file_name, newline="") as file:
            # Returns row of data other than the fieldnames
            return list(csv.DictReader(file))
    except FileNotFoundError:
        # Return empty list if file does not exist
        return []


def read_txtfile(file_name):
    try:
        with open(file_name) as file:
            # Return list without whitespaces
            return [items.strip() for items in file]
    except FileNotFoundError:
        return []


def add_expense(file_name, expense):
    # Validate if csv file exist
    try:
        with open(file_name, "x", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["category", "amount", "date", "note"])
            writer.writeheader()
    except FileExistsError:
        pass
    
    with open(file_name, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["category", "amount", "date", "note"])
        writer.writerow({
            "category": expense.category, 
            "amount": expense.amount,
            "date": expense.date,
            "note": expense.note,
            })


def add_budget(file_name, date, budget):
# Validate if csv file exist
    try:
        with open(file_name, "x", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "budget"])
            writer.writeheader()
    except FileExistsError:
        pass

    
    with open(file_name, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "budget"])
        writer.writerow({
            "date": date,
            "budget": budget,
            })
        
    return


def add_category(file_name, category):
    # Checks for existing file
    try:
        with open(file_name, "x") as file:
            file.write(f"{category.capitalize()}\n")

    except FileExistsError:
        # Append new category to txt file
        with open(file_name, "a") as file:
            file.write(f"{category.capitalize()}\n")