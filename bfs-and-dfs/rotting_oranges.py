from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Note:
            - cell values:
                - 0: empty
                - 1: fresh
                - 2: rotten
            - oranges adjacent to a rotton orange will rot each minute
            - return minimum number of minutes for all oranges to rot
                - if impossible, return -1
                    - if there's more than 0 fresh oranges after rotting all possible oranges
            - 1 <= m, n <= 10
                - at most 100 oranges
        Intuition:
            - Matrix BFS:
                - define q
                - define rows and cols
                - initialize count for fresh oranges
                - iterate each cells
                    - if a cell is a fresh orange:
                        - increment fresh count
                    - if a cell is a rotten orange:
                        - add the coordinates to the q
                            - ex) q = (r, c)
                - process rotten oranges simultaneously (BFS logic):
                    - while fresh_oranges and q:
                        - iterate q's length many times:
                            - orange = q.popleft()
                                - r, c = orange
                            - check 4 adjacent oranges iteratively
                                - right: c + 1
                                    - mark orange rotten and decrement fresh count
                                - bottom: r + 1
                                    - mark orange rotten and decrement fresh count
                                - left: c - 1
                                    - mark orange rotten and decrement fresh count
                                - top: r - 1
                                    - mark orange rotten and decrement fresh count
                        - increment minute + 1
                - return minutes
        """

        # TC: O(R * C) / SC: O(R * C)
        rotten = deque()  # SC: O(R * C)
        rows, cols = len(grid), len(grid[0])
        fresh = 0

        # iterate, count fresh oranges and register rotten oranges
        for row in range(rows):  # TC: O(R * C)
            for col in range(cols):
                orange = grid[row][col]
                if orange == 1:  # fresh
                    fresh += 1
                if orange == 2:  # rotten
                    rotten.append((row, col))

        minutes = 0
        while fresh and rotten:  # TC: O(R * C)
            minutes += 1
            for _ in range(len(rotten)):
                orange = rotten.popleft()
                r, c = orange

                # check right
                if 0 <= c + 1 < cols and grid[r][c + 1] == 1:
                    rotten.append((r, c + 1))
                    fresh -= 1
                    grid[r][c + 1] = 2
                # check bottom
                if 0 <= r + 1 < rows and grid[r + 1][c] == 1:
                    rotten.append((r + 1, c))
                    fresh -= 1
                    grid[r + 1][c] = 2
                # check left
                if 0 <= c - 1 < cols and grid[r][c - 1] == 1:
                    rotten.append((r, c - 1))
                    fresh -= 1
                    grid[r][c - 1] = 2
                # check top
                if 0 <= r - 1 < rows and grid[r - 1][c] == 1:
                    rotten.append((r - 1, c))
                    fresh -= 1
                    grid[r - 1][c] = 2

        return -1 if fresh else minutes


solution = Solution()
start_time = time.time()
print(solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print("--- %s seconds ---" % (time.time() - start_time))
