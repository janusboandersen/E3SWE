"""
A simple run-length encoder used for testing the test software
https://en.wikipedia.org/wiki/Run-length_encoding

"""

# This import uses rle.rle.encode (as PyCharm expects), by way of the __init__.py file, which
# forces the pytest basedir to be u37/ ...so in relation to u37: rle.rle.encode.
# The import is always executed by pytest in relation to the basedir.
from rle.rle import encode

def test_encode():
    assert encode('aa') == '2a'
    assert encode('wwwwwbbb') == '5w3b'
    assert encode('aab') == '2a1b'

def test_empty_string():
    assert encode('') == ''

def test_none_string():
    assert encode(None) == ''

def test_integer():
    assert encode(1234321) == ''

def test_alphanumeric():
    assert encode('aabc1123') == '2a1b1c211213'