#!/usr/bin/python3
"""My_list module"""


class MyList(list):
    """prints the list, but sorted (ascending sort)"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
