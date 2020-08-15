#!/bin/python3


def breaking_records(scores):
    minimum = None
    maximum = None
    total_min = 0
    total_max = 0

    for score in scores:
        if minimum is None and maximum is None:
            minimum = score
            maximum = score
            continue

        if minimum > score:
            total_min += 1
            minimum = score

        if maximum < score:
            total_max += 1
            maximum = score

    return f'{total_max} {total_min}'


def main():
    n = int(input())

    scores = map(int, input().rstrip().split())

    result = breaking_records(scores)

    print(result)


if __name__ == '__main__':
    main()
