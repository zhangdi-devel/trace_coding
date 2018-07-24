#!/usr/bin/env python
from math import floor, ceil


def eat(garden):
    if len(garden) == 0 or len(garden[0]) == 0:
        # empty garden
        return 0

    m = len(garden)  # number of rows
    n = len(garden[0])  # number of cols

    # find the starting cell
    i, j = center(garden)
    # initial value for sum
    res = garden[i][j]
    # move and eat
    while True:
        garden[i][j] = 0  # set the current to 0
        max = ((0, 0), 0)
        for mi, mj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ci, cj = i + mi, j + mj
            if ci >= 0 and ci < m and cj >= 0 and cj < n and\
                    garden[ci][cj] > max[-1]:
                max = ((ci, cj), garden[ci][cj])
        print(max)
        if max[-1] == 0:
            return res  # sleep
        else:
            i, j = max[0]  # move to next cell
            res += garden[i][j]
    return res


def center(garden):
    """
    Assume the garden is not empty
    """
    m = len(garden)  # number of rows
    n = len(garden[0])  # number of columns
    rows = range(floor((m-1)/2), ceil((m+1)/2))  # center rows
    cols = range(floor((m-1)/2), ceil((n+1)/2))  # center columns
    center_cells = [((i, j), garden[i][j]) for j in cols for i in rows]
    return sorted(center_cells)[-1][0]  # sort the cells by value, return index


if __name__ == '__main__':
    #
    #  1, 2, 0
    #  4, 5, 6
    #  7, 8, 9

    g1 = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]
    print(center(g1))
    print(eat(g1))
