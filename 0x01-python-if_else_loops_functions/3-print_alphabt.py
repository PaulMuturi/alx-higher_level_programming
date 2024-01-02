#!/usr/bin/python3
for num in range(26):
    if ((chr(ord('a') + num) != 'q') and (chr(ord('a') + num) != 'e')):
        print("{}".format(chr(ord('a') + num)), end='')
