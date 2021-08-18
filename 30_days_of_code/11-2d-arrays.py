#!/bin/python3


def matrix(r, c):
    return [[0 for _ in range(c)] for _ in range(r)]


def shape(mat):
    r = len(mat)
    c = len(mat[0])

    return r, c


def windows(mat, r, c):
    max_row, max_col = shape(mat)

    i = 0
    j = 0

    while True:
        window = matrix(r, c)
        for row in range(r):
            cur_row = row + i
            if row == 1:
                window[row][1] = mat[cur_row][cur_col - 1]
                continue

            for col in range(c):
                cur_col = col + j

                if cur_row >= max_row or cur_col >= max_col:
                    continue

                window[row][col] = mat[cur_row][cur_col]

        yield window

        if j + c < max_col:
            j += 1
            continue

        if i + r < max_row:
            j = 0
            i += 1
            continue

        break


def mat_sum(mat):
    s = 0
    for row in mat:
        for col in row:
            s += col

    return s


def print_mat(mat):
    for row in mat:
        for col in row:
            print(col, end='\t')
        print()


def main():
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    m = 0
    for window in windows(arr, 3, 3):
        m = max(mat_sum(window), m)

    print(m)


if __name__ == '__main__':
    main()
