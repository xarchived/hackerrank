#!/bin/python3


def birthday_cake_candles(ar):
    tallest = max(ar)
    return ar.count(tallest)


def main():
    _ = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = birthday_cake_candles(ar)
    print(result)


if __name__ == '__main__':
    main()
