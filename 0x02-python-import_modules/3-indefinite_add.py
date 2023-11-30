#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_of_argument = 0
    x = 0
    for a in sys.argv:
        if x > 0:
            sum_of_argument += int(a)
        x += 1
    print(sum_of_argument)

