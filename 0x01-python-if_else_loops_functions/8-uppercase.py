#!/usr/bin/python3
def uppercase(str):
    a = ord('a')
    z = ord('z')
    A = ord('A')
    factor = a - A

    for i in range(len(str)):
        c = str[i]
        asc_c = ord(c)

        if (asc_c >= a and asc_c <= z):
            c = chr(asc_c - factor)
        print("{}".format(c), end='')
    print()
