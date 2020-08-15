#!/bin/python3


def count_apples_and_oranges(s, t, a, b, apples, oranges):
    total_apples = 0
    total_oranges = 0
    house_range = range(s, t + 1)

    for apple in apples:
        if a + apple in house_range:
            total_apples += 1

    for orange in oranges:
        if b + orange in house_range:
            total_oranges += 1

    print(f'{total_apples}\n{total_oranges}')


def main():
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    count_apples_and_oranges(s, t, a, b, apples, oranges)


if __name__ == '__main__':
    main()
