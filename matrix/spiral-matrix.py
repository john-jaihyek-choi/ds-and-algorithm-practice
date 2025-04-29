from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


# Leetcode 54:
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Patterns:
            - Assuming:
                m = len(matrix) / row
                n = len(matrix[0]) / col
            - Starting at matrix[0][0], where matrix[x][y]
                - go right
                    - [ x, y + 1 ] until boundary
                - go bottom
                    - [ x + 1, y ] until boundary
                - go left
                    - [ x, y - 1 ] until boundary
                - go up
                    - [ x - 1, y ] until boundary
            - What are the boundary?
                4 main boundaries:
                    1. left
                        - 0 initially
                    2. right
                        - n + 1 initially
                    3. top
                        - 0 initially
                    4. bottom
                        - m + 1 initially
            - in each iteration, I could tackle layer by layer
                - ex)
                    outer-most layer of a matrix -> inner-most layer of matrix
        General Steps:
            - initialize 4 boundaries:
                l, t = 0
                r, b = n + 1, m + 1
            - iterate while l < r and t < b:
                1. traverse the matrix right (increment y) until boundary is met
                    - boundary == r
                Update t boundary
                2. traverse the matrix down (increment x) until boundary is met
                    - boundary == b
                Update r boundary
                3. traverse the matrix left (decrement y) until boundary is met
                    - boundary == l
                update b boundary
                4. traverse the matrix up (decrement x) until boundary is met
                    - boundary == t
                update l boundary

        ex)
        [
            [ 1,  2,  3,  4 ],
            [ 5,  6,  7,  8 ],
            [ 9, 10, 11, 12 ]
        ]
        """
        m = len(matrix)
        n = len(matrix[0])

        l = t = 0
        r, b = n, m
        res = []
        while l < r and t < b:
            for col in range(l, r):
                res.append(matrix[t][col])
            t += 1

            for row in range(t, b):
                res.append(matrix[row][r - 1])
            r -= 1

            if t >= b or l >= r:
                break

            for col in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][col])
            b -= 1

            for row in range(b - 1, t - 1, -1):
                res.append(matrix[row][l])
            l += 1

        return res


solution = Solution()
start_time = time.time()
print(
    solution.spiralOrder(
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    )
)
print("--- %s seconds ---" % (time.time() - start_time))
