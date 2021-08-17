#!/bin/python3


def odd(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def even(n):
    return n % 2 == 0


def main():
    n = int(input().strip())
    if odd(n):
        print('Weird')
    elif even(n) and 2 <= n <= 5:
        print('Not Weird')
    elif even(n) and 6 <= n <= 20:
        print('Weird')
    elif even(n) and n > 20:
        print('Not Weird')


if __name__ == '__main__':
    main()
