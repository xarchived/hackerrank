#!/bin/python3

import itertools


def mini_max_sum(arr):
    sums = []
    for combination in itertools.combinations(arr, 4):
        sums.append(sum(combination))

    print(f'{min(sums)} {max(sums)}')


def main():
    arr = list(map(int, input().rstrip().split()))

    mini_max_sum(arr)


if __name__ == '__main__':
    main()
