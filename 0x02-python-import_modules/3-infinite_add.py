#!/usr/bin/python3
if (__name__ == '__main__'):
    import sys
    argv = sys.argv
    argv_count = len(argv)
    sum = 0

    if (argv_count > 1):
        for i in range(1, argv_count):
            sum += int(argv[i])

    print(f"{sum}")
