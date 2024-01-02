#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdgt = abs(number) % 10

if (number < 0):
    lastdgt *= -1
if (lastdgt > 5):
    msg = "and is greater than 5"
elif (lastdgt == 0):
    msg = "and is 0"
elif (lastdgt < 6):
    msg = "and is less than 6 and not 0"

print(f"Last digit of {number} is {lastdgt} {msg}")
