#!/bin/python3


def kangaroo(x1, v1, x2, v2):
    try:
        x = (x2 - x1) / (v1 - v2)
    except ZeroDivisionError:
        return 'NO'

    f = x - int(x)
    if x > 0 and f == 0:
        return 'YES'
    return 'NO'


def main():
    line = input().split()
    x1 = int(line[0])
    v1 = int(line[1])
    x2 = int(line[2])
    v2 = int(line[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)


if __name__ == '__main__':
    main()
