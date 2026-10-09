import time
from datetime import datetime
import csv
import re
from budget import get_budget


def get_dashboard():
    print("=======================")
    print("       DASHBOARD")
    print("=======================")

    budget = current_budget(get_budget())
    date = format_date(budget["date"])
    print(f"{date}: PHP {budget["budget"]}")

    input()


def current_budget(budget_list):
    today = datetime.today()
    today = today.strftime("%m/%Y")

    for budget in budget_list:
        if budget["date"] == today:
            return budget


def format_date(old):
    new = datetime.strptime(old, "%m/%Y")
    return new.strftime("%B %Y")