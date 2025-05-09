from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Note:
            - What constitutes Island?
                - 1's surrounded by 0's (up, down, left, right)
            - edgecase:
                - 1 big island
                    - big chunk of 1's that's conected with 1s that's surrounded by 0's or the edges
            - Intuition:
                - given:
                    - m = len(grid)
                    - n = len(grid[0])
                - Iterate on every available cells, if island is found, recurse using dfs to traverse 4-way direction (left, up, right, bottom)
                - General steps:
                    - iterate on a grid
                        - r, c = row, col
                        - current_cell = grid[r][c]
                        - if current_cell == 1:
                            - increment island count
                            - recurse left, up, right, bottom
                        - else (given cell is a water)
                    - Recursion function:
                        - parameters = r and c
                        - visit 4 unique directions
                            1. left:
                                - 0 < c - 1 < n and grid[r][c-1]:
                                - dfs(c - 1, r)
                            2. up:
                                - 0 < r - 1 < m and grid[r-1][c]:
                                - dfs(c, r - 1)
                            3. right:
                                - 0 < c + 1 < n and grid[r][c + 1]:
                                - dfs(c + 1, r)
                            4. bottom:
                                - 0 < r + 1 < m and grid[r+1][c]:
                                - dfs(c, r + 1)
                            5. Else:
                                - Return exit the function
        """

        # TC: O(R * C) / SC: O(1), O(k) for maximum dfs call stack depth
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> None:
            grid[r][c] = "0"
            # Left
            if 0 <= (c - 1) < cols and grid[r][c - 1] == "1":
                dfs(r, c - 1)
            # Up
            if 0 <= r - 1 < rows and grid[r - 1][c] == "1":
                dfs(r - 1, c)
            # Right
            if 0 <= c + 1 < cols and grid[r][c + 1] == "1":
                dfs(r, c + 1)
            # Bottom
            if 0 <= r + 1 < rows and grid[r + 1][c] == "1":
                dfs(r + 1, c)
            return

        islands = 0
        for r in range(rows):  # O(R)
            for c in range(cols):  # O(C)
                cur = grid[r][c]

                if cur == "1":
                    islands += 1
                    dfs(
                        r, c
                    )  # O(k) where k == number of islands. But is guaranteed to be executed exactly once for unique 1s

        return islands


solution = Solution()
start_time = time.time()
print(
    solution.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
print("--- %s seconds ---" % (time.time() - start_time))
