from decimal import Decimal
from classes import FinancialRecord
import pytest


def test_valid_record():
    record = FinancialRecord("10/2026", "100.50")

    assert record.date == "10/2026"
    assert record.amount == Decimal("100.50")


def test_invalid_date_format():
    with pytest.raises(ValueError):
        FinancialRecord("2026-10", "100.50")


def test_amount_below_zero_is_rejected():
    with pytest.raises(ValueError):
        FinancialRecord("10/2026", "-0.01")


def test_infinite_amount_is_rejected():
    with pytest.raises(ValueError):
        FinancialRecord("10/2026", "Infinity")


def test_date_setter_accepts_valid_date():
    record = FinancialRecord("10/2026", "100")

    record.date = "11/2026"

    assert record.date == "11/2026"


def test_date_setter_rejects_invalid_date():
    record = FinancialRecord("10/2026", "100")

    with pytest.raises(ValueError):
        record.date = "13/2026"


def test_date_getter_returns_correct_date():
    record = FinancialRecord("10/2026", "100")

    assert record.date == "10/2026"


def test_invalid_month():
    with pytest.raises(ValueError):
        FinancialRecord("13/2026", "100")


def test_invalid_date_input():
    with pytest.raises(ValueError):
        FinancialRecord("October 2026", "100")


def test_missing_month_input():
    with pytest.raises(ValueError):
            FinancialRecord("2026", "100")


def test_missing_year_input():
    with pytest.raises(ValueError):
            FinancialRecord("10", "100")


def test_invalid_amount_input():
    with pytest.raises(ValueError):
        FinancialRecord("10/2026", "abc")


def test_amount_integer_input():
    record = FinancialRecord("10/2026", "100")

    assert record.amount == Decimal("100")


def test_amount_decimal_input():
    record = FinancialRecord("10/2026", "100.50")
    
    assert record.amount == Decimal("100.50")


def test_amount_setter_accepts_valid_amount():
    record = FinancialRecord("10/2026", "100.50")
    record.amount = 200.75

    assert record.amount == Decimal("200.75")


def test_amount_rejects_input_zero():
    with pytest.raises(ValueError):
        FinancialRecord("10/2026", "0")


def test_amount_rejects_NaN():
    with pytest.raises(ValueError):
            FinancialRecord("10/2026", "NaN")


def test_amount_accepts_fraction():
    record = FinancialRecord("10/2026", "0.50")

    assert record.amount == Decimal("0.50")