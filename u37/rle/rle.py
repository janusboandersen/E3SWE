"""
A simple run-length encoder used for testing the test software
https://en.wikipedia.org/wiki/Run-length_encoding
"""
import os

print(os.getcwd())

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