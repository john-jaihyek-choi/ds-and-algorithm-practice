from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


# Leetcode 885:


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        """
        Note:
            - start at (rStart, cStart) of matrix
            - navigate in clockwise spiral shape in every position in the grid
                - if outside the boundary of matrix, walk without recording the coordinate
        Constraints:
            - 1 <= rows, cols <= 100
            - 0 <= rStart < rows
            - 0 <= cStart < cols
        Pattern:
            - from starting point...
                - x starting from 1
                - move left to right by x
                - move top to bottom by x
                - move right to left by x + 1
                - move bottom to right by x + 1
                - increment x by 2
        Intuition:
            - initialize x at 1
            - cur = [rStart, cStart]
            - output = [current]
            - use while loop to loop while len(output) < (rows * cols)
                - go left to right by 1
                    iterate x many times
                        - cur = [cur[0], cur[1] + 1]
                        - if cur[0] < row and cur[1] < col:
                            - output.append(cur)
                - go top to bottom by 1
                    iterate x many times
                        - cur = [cur[0] + 1, cur[1]]
                        - if cur[0] < row and cur[1] < col:
                            - output.append(cur)
                - go right to left by x + 1
                    iterate x + 1 many times
                        - cur = [cur[0], cur[1] - 1]
                        - if cur[0] < row and cur[1] < col:
                            - output.append(cur)
                - go bottom to top by x + 1
                    iterate x + 1 many times
                        - cur = [cur[0] - 1, cur[1]]
                        - if cur[0] < row and cur[1] < col:
                            - output.append(cur)
                - increment x += 2
        """

        # TC: O(rows * cols) / SC: O(1) / O(rows * cols) for output array
        x = 1
        cur = [rStart, cStart]
        output = [cur]

        while len(output) < (rows * cols):
            # move left to right
            for _ in range(1, x + 1):
                cur = [cur[0], cur[1] + 1]
                if self.isWithinBoundary(cur, rows, cols):
                    output.append(cur)

            # move top to bottom
            for _ in range(1, x + 1):
                cur = [cur[0] + 1, cur[1]]
                if self.isWithinBoundary(cur, rows, cols):
                    output.append(cur)

            # move right to left
            for _ in range(1, x + 2):
                cur = [cur[0], cur[1] - 1]
                if self.isWithinBoundary(cur, rows, cols):
                    output.append(cur)

            # left bottom to top
            for _ in range(1, x + 2):
                cur = [cur[0] - 1, cur[1]]
                if self.isWithinBoundary(cur, rows, cols):
                    output.append(cur)

            x += 2

        return output

    def isWithinBoundary(self, coord: [int, int], r, c) -> bool:
        if 0 <= coord[0] < r and 0 <= coord[1] < c:
            return True

        return False


solution = Solution()
start_time = time.time()
print(solution.generateMatrix(9))
print("--- %s seconds ---" % (time.time() - start_time))
