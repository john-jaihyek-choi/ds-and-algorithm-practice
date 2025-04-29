from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


# Leetcode 59:
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Note:
            - n * n matrix
            - input == n
            - spiral pattern:
                1. top
                2. right
                3. bottom
                4. left
        Intuition:
            - define left, right, top, and bottom boundary
            - fill elements by i (iterating from 1 to n)
                - ex) input = n = 3
                    - 3 x 3 matrix will have up to 9
        General steps:
            - define left and top boundary to 0
            - define right and bottom boundary to n - 1
            - initialize cell_val at 1
            - initialize an empty n x n grid
            - iterate while left and right boundary and top and bottom boundary doesn't meet:
                - iterate from left to right (start = left, end = right, col = i)
                    - grid[top][col] = cell_val
                    - cell_val += 1
                - update top boundary
                - iterate from top to bottom (start = top, end = right, row = i)
                    - grid[row][right] = cell_val
                    - cell_val += 1
                - update right boundary
                - iterate from right to left (start = right, end = left - 1, col = i)
                    - grid[top][col] = cell_val
                    - cell_val += 1
                - update bottom boundary
                - iterate from bottom to top (start = bottom, end = top - 1, row = i)
                    - grid[row][left] = cell_val
                    - cell_val += 1
                - update left boundary
        """

        # TC: O(n^2) / SC: O(n^2) including output matrix space
        matrix = [[0 for i in range(n)] for i in range(n)]
        left = top = 0
        right = bottom = n
        cell_val = 1

        while cell_val <= pow(n, 2):
            # iterate left to right
            for col in range(left, right):
                matrix[top][col] = cell_val
                cell_val += 1
            top += 1

            # iterate from top to bottom
            for row in range(top, bottom):
                matrix[row][right - 1] = cell_val
                cell_val += 1
            right -= 1

            # iterate right to left
            for col in range(right - 1, left - 1, -1):
                matrix[bottom - 1][col] = cell_val
                cell_val += 1
            bottom -= 1

            # iterate bottom to top
            for row in range(bottom - 1, top - 1, -1):
                matrix[row][left] = cell_val
                cell_val += 1
            left += 1

        return matrix


solution = Solution()
start_time = time.time()
print(solution.generateMatrix(9))
print("--- %s seconds ---" % (time.time() - start_time))
