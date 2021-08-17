#!/bin/python3


def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)


def main():
    n = int(input())
    print(factorial(n))


if __name__ == '__main__':
    main()
