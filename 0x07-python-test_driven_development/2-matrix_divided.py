#!/usr/bin/python3

"""
Multiplies elements of a matrix list  with a given number

Functions:
    matrix_divided: Multiplies list elements \
    within a matrix  with a given factor
"""


def matrix_divided(matrix, div):
    """
    Multiplies list elements within a matrix  with a given factor
    Args:
        matrix: a list containing a list on integers/floats
        div: The dividing factor

    Returns: A new list with the results of the division

    Raises:
        TypeError: if the the lists in the matrix doesn't\
        contain an integer or float.
        TypeError: if the matrix contains lists of different length
        TypeError: if div is not a number
        ZerodivisionError: if div equals zero (0)
    """

    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = []
    lst_len = len(matrix[0])

    for lst in matrix:
        if (lst_len == len(lst)):
            sub_list = []
            for i in lst:
                if not isinstance(i, float) and not isinstance(i, int):
                    raise TypeError("matrix must be a matrix (list of lists)"
                                    " of integers/floats")
                else:
                    sub_list.append(round((i / div), 2))

            new_list.append(sub_list)
        else:
            raise TypeError("Each row of the matrix must have the same size")
    return new_list


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
