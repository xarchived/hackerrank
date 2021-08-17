#!/bin/python3


import collections
import os


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    tmp = collections.Counter(ar)
    total = 0

    for k, v in tmp.items():
        total += int(v / 2)

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
