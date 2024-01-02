#!/usr/bin/python3
def pow(a, b):
    result = 1
    abs_b = abs(b)

    for i in range(abs_b):
        if (b >= 0):
            result = result * a
        else:
            result = result / a
    return result
