#!/usr/bin/python3
""" Solve the island_perimeter """


def island_perimeter(grid):
    """island_perimeter
    """
    cases = 0
    size = 0
    w = len(grid[0])
    h = len(grid)

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    cases += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    cases += 1
    return size * 4 - cases * 2
