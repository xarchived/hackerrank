#!/bin/python3


def main():
    _ = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))


if __name__ == '__main__':
    main()
