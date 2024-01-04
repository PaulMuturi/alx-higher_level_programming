#!/usr/bin/python3
if (__name__ == "__main__"):
    import hidden_4
    allnames = sorted(dir(hidden_4))
    list_len = len(allnames)

    for i in range(list_len):
        the_name = allnames[i]
        if not the_name.startswith("__"):
            print(f"{allnames[i]}")
