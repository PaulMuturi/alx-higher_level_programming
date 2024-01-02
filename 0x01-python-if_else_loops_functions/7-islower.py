#!/usr/bin/python3
def islower(c):
    a = ord('a')
    z = ord('z')
    asc_c = ord(c)

    if (asc_c >= a and asc_c <= z):
        return True
    return False
