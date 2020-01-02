"""
A simple run-length encoder used for testing the test software
https://en.wikipedia.org/wiki/Run-length_encoding

Janus Bo Andersen, 2019
"""
import re

def encode(msg):
    """
    Returns an encoded sequence from contents in msg
    """

    #Corner cases:
    if msg == '':
        return ''   # the empty string yields an empty string

    if not isinstance(msg, str):
        return ''   # What to do on non-strings (isinstance also allows for subclasses)

    if msg == None:
        return ''   # If None (void) is passed in

    res = []        # Store RLE results in dict
    old = msg[0]    # Begin with the first char in the message
    i = 0
    for c in msg:
        if c == old:
            # Another observation of the same char, increase run length by 1
            i += 1
        else:
            # A different char
            # Store results up to now
            res.append(f'{i}{old}')

            # Prepare for next round
            old = c
            i = 1

    res.append(f'{i}{old}')

    # Return the concatenation of all observed run lengths
    return ''.join(res)

def decode(seq):
    """
    Decodes a Run-length encoded sequence such as '2k3b' into 'kkbbb'
    """

    # Handle some corner cases
    if (not seq) or (not isinstance(seq, str)):
        return ''   # Return empty string on non-strings and all non-true values (empty string, None, 0, ...)

    # Use regex to match patters, t is a list of tuples (if any found)
    # '2k3b' -> [('2','k'), ('3','b')]   ...notice that integers are still string-formatted
    t = re.findall(r'(\d)(\D)', seq)

    # Return if empty
    if not t:
        return ''

    # Use a list comprehension to work on the tuples... Convert integers to int
    # [('2','k'), ('3','b')] -> ['k'*2 , 'b'*3] -> ['kk', 'bbb']
    msg = [c*int(i) for i,c in t]

    # Concatenate without separators, msg is now a string
    msg = ''.join(msg)

    return msg