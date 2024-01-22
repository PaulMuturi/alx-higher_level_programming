#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    item_count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            raise
        except (ValueError, Exception):
            pass
        else:
            item_count += 1

    print()
    return item_count
