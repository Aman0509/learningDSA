# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/

import copy


def max_increase_keeping_skyline(grid):
    """
    :type grid: List[List[int]]
    """
    sum = 0
    n = len(grid)
    row_max = []
    col_max = []
    grid_new = copy.deepcopy(grid)
    for i in range(n):
        row_max.append(grid[i][0])
        col_max.append(grid[i][i])
        for j in range(n):
            if row_max[i] < grid[i][j]:
                row_max[i] = grid[i][j]
            if col_max[i] < grid[j][i]:
                col_max[i] = grid[j][i]
    for i in range(n):
        for j in range(n):
            sum += min(row_max[i], col_max[j]) - grid[i][j]
            grid_new[i][j] = min(row_max[i], col_max[j])
    return sum, grid_new
