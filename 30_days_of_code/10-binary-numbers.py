#!/bin/python3


def main():
    n = int(input())
    g = bin(n)[2:].split('0')
    print(len(max(g)))


if __name__ == '__main__':
    main()
