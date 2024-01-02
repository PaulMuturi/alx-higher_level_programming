#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    print(f"{number % 10}", end='')
    return number % 10
