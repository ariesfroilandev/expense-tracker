from classes import Expense
from decimal import Decimal
import pytest


def test_valid_input(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])
    
    expense = Expense("Food", "10000", "10/2026", "test")

    assert expense.category == "Food"
    assert expense.amount == Decimal("10000")
    assert expense.date == "10/2026"
    assert expense.note == "test"


def test_expense_rejects_invalid_category(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])

    with pytest.raises(ValueError):
        Expense("Misc", "10000", "10/2026", "test")


def test_expense_accepts_updating_to_valid_category(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])

    expense = Expense("Food", "10000", "10/2026", "test")
    expense.category = "Bills"
    
    assert expense.category == "Bills"


def test_expense_rejects_updating_to_invalid_category(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])

    expense = Expense("Food", "10000", "10/2026", "test")

    with pytest.raises(ValueError):
        expense.category = "Misc"


def test_expense_rejects_invalid_amount_during_init(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])
    
    with pytest.raises(ValueError):
        Expense("Food", "abc", "10/2026", "test")


def test_expense_rejects_invalid_date_during_init(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])
    
    with pytest.raises(ValueError):
        Expense("Food", "10000", "abc", "test")


def test_expense_inherits_date_property(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])

    expense = Expense("Food", "10000", "10/2026", "test")

    assert expense.date == "10/2026"


def test_expense_inherited_date_setter_accepts_valid_date(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])

    expense = Expense("Food", "10000", "10/2026", "test")
    expense.date = "11/2026"

    assert expense.date == "11/2026"


def test_expense_inherited_amount_returns_decimal(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])

    expense = Expense("Food", "10000", "10/2026", "test")
    assert expense.amount == Decimal("10000")


def test_expense_inherited_amount_setter_accepts_valid_amount(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])

    expense = Expense("Food", "10000", "10/2026", "test")
    expense.amount = "123456"

    assert expense.amount == Decimal("123456")


def test_expense_rejects_incorrect_date_format(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])
    
    with pytest.raises(ValueError):
        Expense("Food", "10000", "10-2026", "test")


def test_expense_rejects_incorrect_date(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])
    
    with pytest.raises(ValueError):
        Expense("Food", "10000", "13/2026", "test")



def test_expense_rejects_zero_amount(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])
    
    with pytest.raises(ValueError):
        Expense("Food", "0", "10/2026", "test")


def test_expense_rejects_negative_amount(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])
    
    with pytest.raises(ValueError):
        Expense("Food", "-10.05", "10/2026", "test")


def test_expense_preserve_category_after_updating_with_invalid_input(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list", 
        lambda: ["Food", "Bills", "Transportation"])
    
    expense = Expense("Food", "10000", "10/2026", "test")

    with pytest.raises(ValueError):
        expense.category = "Misc"

    assert expense.category == "Food"


def test_expense_amount_setter_rejects_invalid_amount(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list",
        lambda: ["Food", "Bills", "Transportation"]
    )

    expense = Expense("Food", "100", "10/2026", "test")

    with pytest.raises(ValueError):
        expense.amount = "abc"


def test_expense_date_setter_rejects_invalid_date(monkeypatch):
    monkeypatch.setattr(
        "expense_categories.get_category_list",
        lambda: ["Food", "Bills", "Transportation"]
    )

    expense = Expense("Food", "100", "10/2026", "test")

    with pytest.raises(ValueError):
        expense.date = "13/2026"

    assert expense.date == "10/2026"