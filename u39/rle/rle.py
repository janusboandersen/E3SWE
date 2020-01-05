"""
A simple run-length encoder used for testing the test software
https://en.wikipedia.org/wiki/Run-length_encoding

Janus Bo Andersen, 2019
Week 38
"""
import re
import sys
import time

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

    # Use regex to match patterns, t is then a list of tuples (if any patterns found)
    # '2k3b' -> [('2','k'), ('3','b')]   ...notice that integers are still string-formatted
    t = re.findall(r'(\d+)(\D)', seq)

    # Return if empty
    if not t:
        return ''

    # Use a list comprehension to work on the tuples... Convert integers to int
    # [('2','k'), ('3','b')] -> ['k'*2 , 'b'*3] -> ['kk', 'bbb']
    msg = [c*int(i) for i,c in t]

    # Concatenate without separators, msg is now a string
    msg = ''.join(msg)

    return msg

# For starting from the command line
if __name__ == '__main__':

    # Error handler
    def err(point="N/A"):
        print(f"Invalid usage at {point}.")
        print(f"Usage examples: Decode using {sys.argv[0]} -d filename, encode using {sys.argv[0]} -e filename.")
        time.sleep(1)
        exit(1)

    # Handle input arguments
    # TODO: replace this hacky implementation with argparse

    # We require len(sys.argv) > 2 and sys.argv[1] == '-d' / '-e'

    if '-d' in  sys.argv:
        # User wants to decode (2k3b -> kkbbb)
        fn = decode
        idx = sys.argv.index('-d')
    elif '-e' in sys.argv:
        # User wants to encode (kkbbb -> 2k3b)
        fn = encode
        idx = sys.argv.index('-e')
    else:
        err("96")

    # Try to extract filename and open file
    try:
        filename = sys.argv[idx + 1]

        # open file from fuzzer as binary file and read contents
        with open(filename, 'rb') as f:
            data = f.read()
    except:
        err("106")

    print(f"Received (binary): {data}.")

    # Attempt to convert to UTF-8 encoded string -> if not possible, it's not a valid UTF-8 sequence
    try:
        data_txt = data.decode("utf-8")
    except:
        # If an error occurs
        print("Bytestring from fuzzer could not be parsed as valid UTF-8.")
        time.sleep(1)
        exit(0) # OK, error handled!

    # Call and output the encode/decode function
    try:
        print(f"Result (UTF-8): {fn(data_txt)}.")
    except:
        # If an error occurs
        print("Function could not handle input.")
        time.sleep(1)
        exit(1)

    time.sleep(1)
    exit(0) # OK!