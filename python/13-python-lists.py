#!/bin/python3


def main():
    tmp = []

    for _ in range(int(input())):
        cmd, *args = input().split()
        args = map(int, args)

        if cmd == 'insert':
            tmp.insert(*args)
        if cmd == 'remove':
            tmp.remove(*args)
        if cmd == 'append':
            tmp.append(*args)
        if cmd == 'print':
            print(tmp)
        if cmd == 'sort':
            tmp = list(sorted(tmp))
        if cmd == 'pop':
            tmp.pop()
        if cmd == 'reverse':
            tmp = list(reversed(tmp))


if __name__ == '__main__':
    main()
