#!/usr/bin/python3
if (__name__ == "__main__"):
    import calculator_1
    import sys

    argv = sys.argv
    argv_count = len(argv_count)

    if (argv_count != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    op = int(argv[2])
    b = int(argv[3])

    if op in {'+', '-', '*', '/'):
        if (op == '+'):
            print(f"{a} {op} {b} = {calculator_1.add(a, b)}")
        if (op == '-'):
            print(f"{a} {op} {b} = {calculator_1.sub(a, b)}")
        if (op == '*'):
            print(f"{a} {op} {b} = {calculator_1.mul(a, b)}")
        if (op == '/'):
            print(f"{a} {op} {b} = {calculator_1.div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
