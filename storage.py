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


def add_budget(file_name, date, amount):
# Validate if csv file exist
    try:
        with open(file_name, "x", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "amount"])
            writer.writeheader()
    except FileExistsError:
        pass

    
    with open(file_name, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "amount"])
        writer.writerow({
            "date": date,
            "amount": amount,
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


def delete_line(file_name, category):
    with open(file_name, "r") as file:
        lines = file.readlines()

    # Makes a filtered list excluding the category you want to delete
    lines = [
        line for line in lines
        if line.strip() != category
        ]
  
    # Overwrites existing file with the filtered list
    with open(file_name, "w") as file:
        file.writelines(lines)