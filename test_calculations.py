from calculations import *


def test_add():
    assert addition(3, 4) == 7, "Addition operation failed"


def test_substraction():
    assert substraction(7, 3) == 4, "Substraction operation failed"


def test_multiplication():
    assert multiplication(3, 4) == 12, "Multiplication operation failed"


def test_division():
    assert division(12, 4) == 3, "Division operation failed"


def test_remainder():
    assert remainder(10, 5) == 0, "Remainder operation failed"


def test_division_false():
    assert division(14, 3) != 8, "Division operation should fail now"
