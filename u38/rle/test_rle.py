"""
A simple run-length encoder used for testing the test software
https://en.wikipedia.org/wiki/Run-length_encoding

Janus Bo Andersen, 2019
"""

# This import uses rle.rle.encode (as PyCharm expects), by way of the __init__.py file, which
# forces the pytest basedir to be u38/ ...so in relation to u37: rle.rle.encode.
# The import is always executed by pytest in relation to the basedir.
from rle.rle import encode, decode
import pytest
import string

from hypothesis import given, example, settings
import hypothesis.strategies as st


# For testing RLE encoder
def test_enc_good():
    assert encode('aa') == '2a'
    assert encode('wwwwwbbb') == '5w3b'
    assert encode('aab') == '2a1b'

    # multi-digit coefficient
    assert encode('aaaaaaaaaaab') == '11a1b'

def test_enc_empty_string():
    assert encode('') == ''

def test_enc_none_string():
    assert encode(None) == ''

def test_enc_integer():
    assert encode(1234321) == ''

def test_enc_alphanumeric():
    assert encode('aabc1123') == '2a1b1c211213'


# For testing RLE decoder
def test_dec_roundtrip():
    msg = 'wwwwwbbb'
    assert decode(encode(msg)) == msg

def test_dec_good():
    assert decode('2k3b') == 'kkbbb'

    # multi-digit coefficient
    assert decode('11a1b') == 'aaaaaaaaaaab'

def test_dec_erroneous():
    assert decode('kk') == ''
    assert decode('k2') == ''

def test_dec_empty():
    assert decode(None) == ''

def test_dec_numeric():
    assert decode(1234321) == ''

# @settings(derandomize=True)
# Using hypothesis to test the encoder/decoder
# @given: wraps test function with automatically generated test cases
# st.text: defines how data is generated (the strategy)
# @example: this case will always be checked
# aaabcd -> 3a1b1c1d -> aaabcd

@given(st.text(alphabet=string.printable))
#@given(st.text())
@example('0')
def test_encode_decode(msg):
    print(msg)
    assert (decode(encode(msg))) == msg