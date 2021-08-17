#!/bin/python3


def main():
    phone_book = {}

    for i in range(int(input())):
        a = input().split()
        phone_book[a[0]] = a[1]

    while b := input():
        if b not in phone_book:
            print('Not found')
        else:
            print(f'{b}={phone_book[b]}')


if __name__ == '__main__':
    try:
        main()
    except EOFError:
        pass
