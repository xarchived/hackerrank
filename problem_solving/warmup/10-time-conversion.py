#!/bin/python3

import datetime


def time_conversion(s):
    t = datetime.datetime.strptime(s, '%I:%M:%S%p')
    return str(t.time())


def main():
    s = input()
    result = time_conversion(s)
    print(result)


if __name__ == '__main__':
    main()
