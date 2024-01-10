#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(len(my_list)):
        el = my_list[i]
        if (el == search):
            el = replace
        new_list.append(el)

    return new_list
