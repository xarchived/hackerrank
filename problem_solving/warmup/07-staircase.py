#!/bin/python3


def staircase(n):
    for i in range(n):
        pad = n - 1 - i
        print(' ' * pad + '#' * (i + 1))


def main():
    n = int(input())

    staircase(n)


if __name__ == '__main__':
    main()
