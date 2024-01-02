#!/usr/bin/python3
for num in range(1, 100):
    if (num / 10 < num % 10):
        if (num > 1):
            print("{}".format(", "), end="")
        print("{:02d}".format(num), end="")
print()
