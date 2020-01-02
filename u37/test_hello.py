"""
This is the first test using PyTest
"""

def func(x):
    return x + 1

def test_answer():
    assert func(3)  == 4
