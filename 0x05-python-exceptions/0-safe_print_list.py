#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    item_count = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end='')
        except IndexError:
            break
        except Exception:
            pass
        else:
            item_count += 1

    print()
    return item_count
