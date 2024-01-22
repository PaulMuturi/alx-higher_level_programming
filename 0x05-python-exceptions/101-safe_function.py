#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    result = 0

    try:
        result = fct(*args)
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
    else:
        return result
