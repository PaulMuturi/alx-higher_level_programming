#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    ch = None

    if (str_len > 0):
        ch = sentence[0]
    tup = (str_len, ch)

    return tup
