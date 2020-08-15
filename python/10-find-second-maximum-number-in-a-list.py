#!/bin/python3


def main():
    _ = input()
    a = list(map(int, input().split()))

    print(list(sorted(set(a)))[-2])


if __name__ == '__main__':
    main()
