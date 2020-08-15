#!/bin/python3


def special_round(grade):
    if grade < 38:
        return grade

    dist = 5 - (grade % 5)
    if dist < 3:
        return grade + dist

    return grade


def main():
    grades_count = int(input().strip())

    for _ in range(grades_count):
        grade = int(input().strip())
        grade = special_round(grade)
        print(grade)


if __name__ == '__main__':
    main()
