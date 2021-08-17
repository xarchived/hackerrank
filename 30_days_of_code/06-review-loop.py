#!/bin/python3


def main():
    t = int(input())

    for i in range(t):
        s = input()
        print(s[::2], s[1::2])


if __name__ == '__main__':
    main()
