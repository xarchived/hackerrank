#!/bin/python3


def swap_case(s):
    tmp = []
    for c in s:
        if c.islower():
            tmp.append(c.upper())
        else:
            tmp.append(c.lower())

    return ''.join(tmp)


def main():
    s = input()
    result = swap_case(s)
    print(result)


if __name__ == '__main__':
    main()
