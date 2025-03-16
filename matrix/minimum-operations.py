from typing import List


# Leetcode 3402
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        # objective:
        # return the minimum number of operations needed to make all columns of grid strictly increasing
        # grid[0][0] < grid[1][0] < grid[2][0] ...
        # brainstorm:
        # ex)
        # [col 1  2
        #     [3, 2],
        #     [1, 3], +3, +0
        #     [3, 4], +2, +0
        #     [0, 1], +6, +4
        # ]
        # things to consider:
        # iterating each column
        # given... grid[i][j]
        # i = row
        # j = col
        # number of columns == len(grid[0])
        # remembering value of the column in the previous row
        # when in row 2 (grid[2][0])
        # I need grid[1][0] value
        # solution:
        # rows = len(grid)
        # cols = len(grid[0])
        # min_operations = 0
        # iterate grid by cols
        # prev = 0
        # iterate grid by rows
        # if prev > grid[row][col]:
        # diff = prev - grid[row][col] + 1
        # operation += diff
        # prev = grid[row][col] + diff
        # return min_operations

        # TC: O(n * m) / SC: O(1)
        rows, cols = len(grid), len(grid[0])
        min_operations = 0
        for col in range(cols):
            prev = -1

            for row in range(rows):
                if prev >= grid[row][col]:
                    diff = prev - grid[row][col] + 1
                    min_operations += diff
                    prev = grid[row][col] + diff
                else:
                    prev = grid[row][col]

        return min_operations

        # Cleaner code and optimization:
        rows, cols = len(grid), len(grid[0])
        min_operations = 0
        for col in range(cols):
            prev = grid[0][col]

            for row in range(1, rows):
                if prev >= grid[row][col]:
                    min_operations += prev - grid[row][col] + 1
                    prev += 1
                else:
                    prev = grid[row][col]

        return min_operations
