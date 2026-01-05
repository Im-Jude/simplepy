import pytest
from main import check_number

def test_positive():
    assert check_number(5) == "Positive"

def test_negative():
    assert check_number(-3) == "Negative"

def test_zero():
    assert check_number(0) == "Zero"