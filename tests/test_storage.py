import csv
import storage
import pytest
from types import SimpleNamespace


def test_read_csvfile_returns_rows(tmp_path):
    csv_file = tmp_path / "budget.csv"

    csv_file.write_text(
        "date,amount\n"
        "10/2026,10000\n"
        "09/2026,9000\n"
    )

    result = storage.read_csvfile(str(csv_file))

    assert result == [
        {
            "date": "10/2026",
            "amount": "10000",
        },
        {
            "date": "09/2026",
            "amount": "9000",
        }
    ]


def test_read_csvfile_returns_empty_list_when_only_headers(tmp_path):
    csv_file = tmp_path / "budget.csv"

    csv_file.write_text(
        "date,amount\n")

    result = storage.read_csvfile(str(csv_file))

    assert result == []


def test_read_csvfile_returns_empty_list_when_file_missing(tmp_path):
    csv_file = tmp_path / "budget.csv"

    result = storage.read_csvfile(str(csv_file))
    
    assert result == []


def test_read_txtfile_returns_items(tmp_path):
    txt_file = tmp_path / "categories.txt"

    txt_file.write_text(
        "Food\n"
        "Bills\n"
        "Transportation\n"
    )

    result = storage.read_txtfile(str(txt_file))

    assert result == ["Food", "Bills", "Transportation"]


def test_read_txtfile_returns_empty_list_when_file_missing(tmp_path):
    txt_file = tmp_path / "categories.txt"

    result = storage.read_txtfile(str(txt_file))

    assert result == []


def test_add_expense_without_existing_file(tmp_path):
    csv_file = tmp_path / "expense.csv"

    expense = SimpleNamespace(
        category = "Food",
        amount = "1000",
        date = "10/2026",
        note = "Test",
        )
        
    storage.add_expense(str(csv_file), expense)

    with csv_file.open(newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert rows == [
        {
            "category": "Food",
            "amount": "1000",
            "date": "10/2026",
            "note": "Test",
        }
    ]

def test_add_expense_appends_existing_file(tmp_path):
    csv_file = tmp_path / "expense.csv"

    first_expense = SimpleNamespace(
        category = "Food",
        amount = "1000",
        date = "10/2026",
        note = "Test",
        )

    second_expense = SimpleNamespace(
            category = "Bills",
            amount = "2000",
            date = "09/2026",
            note = "",
            )
        
    storage.add_expense(str(csv_file), first_expense)
    storage.add_expense(str(csv_file), second_expense)

    with csv_file.open(newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert len(rows) == 2
    assert rows[0]["category"] == "Food"
    assert rows[1]["category"] == "Bills"


def test_add_expense_does_not_duplicate_header(tmp_path):
    csv_file = tmp_path / "expense.csv"

    first_expense = SimpleNamespace(
        category="Food",
        amount="1000",
        date="10/2026",
        note="Test",
        )

    second_expense = SimpleNamespace(
            category="Bills",
            amount="2000",
            date="09/2026",
            note="",
            )
        
    storage.add_expense(str(csv_file), first_expense)
    storage.add_expense(str(csv_file), second_expense)

    with csv_file.open(newline="") as file:
        rows = list(csv.reader(file))

    assert rows.count(["category", "amount", "date", "note"]) == 1


def test_add_budget_without_existing_file(tmp_path):
    csv_file = tmp_path / "budget.csv"
        
    storage.add_budget(str(csv_file), "10/2026", "1000")

    with csv_file.open(newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert rows == [
        {
            "date": "10/2026",
            "amount": "1000",
        }
    ]


def test_add_budget_appends_existing_file(tmp_path):
    csv_file = tmp_path / "budget.csv"
        
    storage.add_budget(str(csv_file), "10/2026", "1000")
    storage.add_budget(str(csv_file), "11/2026", "2000")

    with csv_file.open(newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert len(rows) == 2
    assert rows[0]["date"] == "10/2026"
    assert rows[1]["date"] == "11/2026"


def test_add_budget_does_not_duplicate_header(tmp_path):
    csv_file = tmp_path / "budget.csv"
        
    storage.add_budget(str(csv_file), "10/2026", "1000")
    storage.add_budget(str(csv_file), "11/2026", "2000")

    with csv_file.open(newline="") as file:
        rows = list(csv.reader(file))

    assert rows.count(["date", "amount"]) == 1


def test_add_category_capitalize(tmp_path):
    txt_file = tmp_path / "categories.txt"

    storage.add_category(str(txt_file), "food")

    with txt_file.open(newline="") as file:
        category = list(csv.reader(file))

    assert category[0][0] == "Food"


def test_add_category_appends_existing_file(tmp_path):
    txt_file = tmp_path / "categories.txt"

    storage.add_category(str(txt_file), "Food")
    storage.add_category(str(txt_file), "Bills")

    with txt_file.open(newline="") as file:
        category = list(csv.reader(file))

    assert category[1][0] == "Bills"


def test_delete_line(tmp_path):
    txt_file = tmp_path / "categories.txt"
    txt_file.write_text(
        "Food\n"
        "Bills\n"
        "Tranportation\n"
    )

    storage.delete_line(str(txt_file), "Food")

    with txt_file.open(newline="") as file:
        rows = file.readlines()

    assert len(rows) == 2
