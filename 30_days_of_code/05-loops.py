#!/bin/python3


def main():
    n = int(input().strip())

    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')


if __name__ == '__main__':
    main()
