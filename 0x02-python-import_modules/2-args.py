#!/usr/bin/python3
if (__name__ == '__main__'):
    import sys
    argv = sys.argv
    len_argv = len(argv)
    print(f"{len_argv - 1} arguments", end='')
    ending = ':'

    if (len_argv == 1):
        ending = '.'

    print(f"{ending}")

    if (len_argv > 1):
        for i in range(1, len_argv):
            print(f"{i}: {argv[i]}")
