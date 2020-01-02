"""
A simple run-length encoder used for testing the test software
https://en.wikipedia.org/wiki/Run-length_encoding

Janus Bo Andersen, 2019
"""

# This import uses rle.rle.encode (as PyCharm expects), by way of the __init__.py file, which
# forces the pytest basedir to be u37/ ...so in relation to u37: rle.rle.encode.
# The import is always executed by pytest in relation to the basedir.
from rle.rle import encode, decode

# For testing encoder
def test_enc_real():
    assert encode('aa') == '2a'
    assert encode('wwwwwbbb') == '5w3b'
    assert encode('aab') == '2a1b'

def test_enc_empty_string():
    assert encode('') == ''

def test_enc_none_string():
    assert encode(None) == ''

def test_enc_integer():
    assert encode(1234321) == ''

def test_enc_alphanumeric():
    assert encode('aabc1123') == '2a1b1c211213'


# For testing decoder
def test_dec_roundtrip():
    msg = 'wwwwwbbb'
    assert decode(encode(msg)) == msg

def test_dec_real():
    assert decode('2k3b') == 'kkbbb'

def test_dec_erroneous():
    assert decode('kk') == ''
    assert decode('k2') == ''

def test_dec_empty():
    assert decode(None) == ''

def test_dec_numeric():
    assert decode(1234321) == ''
