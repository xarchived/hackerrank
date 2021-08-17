#!/bin/python3

import os


# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    valley = False
    total = 0

    for c in s:
        if c == 'U':
            level += 1
        else:
            level -= 1

        if not valley and level < 0:
            valley = True

        if valley and level == 0:
            valley = False
            total += 1

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
