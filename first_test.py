import pytest
from app.colculator import Calculator


class TestCol:
    def setup(self):
        self.col = Calculator()

    def test_multiplay_Calculator_correctly(self):
        assert self.col.multiply(2, 2) == 4

    def test_division_Calculator_correctly(self):
        assert self.col.division(2, 2) == 1

    def test_subtraction_Calculator_correctly(self):
        assert self.col.subtraction(2, 2) == 0

    def test_adding_Calculstor_correctly(self):
        assert self.col.adding(2, 2) == 4