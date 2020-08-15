#!/bin/python3

import os


def main_diagonal(mat):
    dia = []
    col = 0
    for row in mat:
        dia.append(row[col])
        col += 1
    return dia


def anti_diagonal(mat):
    dia = []
    col = len(mat[0]) - 1
    for row in mat:
        dia.append(row[col])
        col -= 1
    return dia


def diagonal_difference(arr):
    d1 = main_diagonal(arr)
    d2 = anti_diagonal(arr)
    return abs(sum(d1) - sum(d2))


def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(arr)

    fptr.write(str(result) + '\n')
    fptr.close()


if __name__ == '__main__':
    main()
