#!/bin/python3

import os


def simple_array_sum(ar):
    return sum(ar)


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    _ = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = simple_array_sum(ar)

    fptr.write(str(result) + '\n')
    fptr.close()


if __name__ == '__main__':
    main()
