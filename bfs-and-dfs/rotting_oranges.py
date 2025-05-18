from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Note:
            - m x n grid
                - max 10 by 10
            - cell value could be 0, 1, 2
                - 0: empty
                - 1: fresh orange
                - 2: rotten orage
            - each adjacent move is 1 min
        Intuition:
            - BFS:
                - iterate every cell
                    - if rotten orange:
                        - do BFS on adjacent cells
                - BFS function
                    - define queue to store directly adjacent cells
                        - start with current cell
                    - intitialize minutes to track
                    - while q is non-empty:
                        - move in 4 directions
                            - left
                                - if col-1 within bound AND grid[row][col-1]:
                                    - add to the queue
                            - right
                                - if col+1 within bound AND grid[row][col+1]:
                                    - add to the queue
                            - top
                                - if row-1 within bound AND grid[row-1][col]:
                                    - add to the queue
                            - bottom
                                - if row+1 within bound AND grid[row+1][col]:
                                    - add to the queue
                        - increment minutes by 1
                    - update min_minutes
        """

        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:  # Initialize list of rotten oranges
                    q.append([row, col])
                if grid[row][col] == 1:  # Count initial fresh oranges
                    fresh_oranges += 1

        minutes = 0
        while (
            fresh_oranges > 0 and q
        ):  # Loop if there's fresh_oranges remaining or q's non-empty
            minutes += 1

            for _ in range(len(q)):
                r, c = q.popleft()
                # left
                if 0 <= c - 1 < cols and grid[r][c - 1] == 1:
                    fresh_oranges -= 1
                    grid[r][c - 1] = 2
                    q.append([r, c - 1])
                # right
                if 0 <= c + 1 < cols and grid[r][c + 1] == 1:
                    fresh_oranges -= 1
                    grid[r][c + 1] = 2
                    q.append([r, c + 1])
                # top
                if 0 <= r - 1 < rows and grid[r - 1][c] == 1:
                    fresh_oranges -= 1
                    grid[r - 1][c] = 2
                    q.append([r - 1, c])
                # bottom
                if 0 <= r + 1 < rows and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    fresh_oranges -= 1
                    q.append([r + 1, c])

        return (
            minutes if fresh_oranges == 0 else -1
        )  # if there are remaining fresh oranges, return -1 else return number of minutes


solution = Solution()
start_time = time.time()
print(
    solution.orangesRotting(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
print("--- %s seconds ---" % (time.time() - start_time))
