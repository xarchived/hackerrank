#!/bin/python3


def second_lowest(arr):
    return list(reversed(sorted(set(arr))))[-2]


def main():
    names = []
    scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        names.append(name)
        scores.append(score)

    sm = second_lowest(scores)

    tmp = []
    for index, score in enumerate(scores):
        if score == sm:
            tmp.append(names[index])

    for name in sorted(tmp):
        print(name)


if __name__ == '__main__':
    main()
