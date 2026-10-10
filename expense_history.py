from decimal import Decimal
from services import get_expenses


def show_expenses():
    print("=======================")
    print("    EXPENSE HISTORY")
    print("=======================")
    
    rows = get_expenses()
    if not rows:
        print("No expenses recorded.")

    else:
        for row in rows:
            print(f"Amount: ${Decimal(row['amount']):,.2f}")
            print(f"Category: {row['category']}")
            print(f"Date: {row['date']}")
            print(f"Note: {row['note']}")
            print("=======================")

    input()