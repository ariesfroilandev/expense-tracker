from datetime import datetime
from utils import validate_format
from decimal import Decimal, InvalidOperation

class Budget():
    def __init__(self, date, budget):
        self.date = date
        self.budget = budget

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not validate_format(date):  
            raise ValueError("Invalid input. Date format (MM/YYYY)") from None

        self._date

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, budget):
        try:
            value = Decimal(budget)
            if not value.is_finite() or value < 1:
                raise ValueError("Amount must not be infinite and must be greater than zero.")
            
        except InvalidOperation: 
            raise ValueError("Input must be a number.") from None

        self._amount = value


    @classmethod
    def get():
        ...