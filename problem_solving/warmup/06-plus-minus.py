#!/bin/python3


def plus_minus(arr):
    length = len(arr)
    negatives = len([x for x in arr if x < 0])
    positives = len([x for x in arr if x > 0])
    zeros = len([x for x in arr if x == 0])

    print(f'{(positives / length):.6f}')
    print(f'{(negatives / length):.6f}')
    print(f'{(zeros / length):.6f}')


def main():
    _ = int(input())
    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)


if __name__ == '__main__':
    main()
