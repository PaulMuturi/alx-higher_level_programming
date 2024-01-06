#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupvals = []
    for i in range(2):
        x, y = 0, 0
        if (len(tuple_a) > i):
            x = tuple_a[i]
        if (len(tuple_b) > i):
            y = tuple_b[i]

        tupvals.append(x+y)

    return (tupvals[0], tupvals[1])
