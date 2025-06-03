from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Note:
            - grid[m][n]:
                - "1" == land
                - "0" == water
            - island:
                - land surrounded by water
            - edges (out of bound):
                - considered water
            - return number of islands
        Intuition:
            - Iterate every cell, dfs to 4 directions (right, bottom, left, up) for lands
                - general steps:
                    - iterate on every cells in the grid
                        - if cell is a land:
                            - increment island counter
                            - dfs on adjacents cells
                    - dfs function:
                        - base case:
                            - if cell == "0":
                                - return
                        - if cell == "1":
                            - recurse again
        """

        rows, cols = len(grid), len(grid[0])

        # DFS
        def dfs(r: int, c: int):
            grid[r][c] = "0"

            # check right
            if 0 <= c + 1 < cols and grid[r][c + 1] == "1":
                dfs(r, c + 1)
            # check bottom
            if 0 <= r + 1 < rows and grid[r + 1][c] == "1":
                dfs(r + 1, c)
            # check left
            if 0 <= c - 1 < cols and grid[r][c - 1] == "1":
                dfs(r, c - 1)
            # check up
            if 0 <= r - 1 < rows and grid[r - 1][c] == "1":
                dfs(r - 1, c)

        # BFS
        def bfs(row: int, col: int):
            q = deque([(row, col)])

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    # check right
                    if 0 <= c + 1 < cols and grid[r][c + 1] == "1":
                        q.append((r, c + 1))
                        grid[r][c + 1] = "0"
                    # check bottom
                    if 0 <= r + 1 < rows and grid[r + 1][c] == "1":
                        q.append((r + 1, c))
                        grid[r + 1][c] = "0"
                    # check left
                    if 0 <= c - 1 < cols and grid[r][c - 1] == "1":
                        q.append((r, c - 1))
                        grid[r][c - 1] = "0"
                    # check up
                    if 0 <= r - 1 < rows and grid[r - 1][c] == "1":
                        q.append((r - 1, c))
                        grid[r - 1][c] = "0"

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    # dfs(r, c)
                    bfs(r, c)

        return islands


class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Note:
            - m x n grid
                - 1 <= m, n <= 300
                - maximum 300 by 300
            - cell values:
                - "1": land
                - "0": water
            - cells outside the boundary are water
            - find total number of islands
        Intuition:
            - DFS to locate size of the island
                - initialize islands
                - iterate on every cells
                    - r, c = row, col
                    - if grid[r][c] == "1":
                        - count island
                        - recurse and stretch 4 directionally
                            - right
                            - bottom
                            - left
                            - up
                - return island
            - BFS:
                - initialize islands
                - define q to store adjacent island coordinates
                - iterate on every cells
                    - if grid[r][c] == "1"
                        - count islands
                        - bfs to q
                - bfs function:
                    - while q is non-empty:
                        - popleft from q
                            - (r, c) pair
                        - Check adjacent cells
                            - if land, add to q
        """
        # TC: O(R * C) / SC: O(1)
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r: int, c: int) -> None:
            # initialize current coordinate
            q = deque([(r, c)])

            while q:
                r, c = q.popleft()

                # check right
                if 0 <= c + 1 < cols and grid[r][c + 1] == "1":
                    q.append((r, c + 1))
                    grid[r][c + 1] = 0
                # check bottom
                if 0 <= r + 1 < rows and grid[r + 1][c] == "1":
                    q.append((r + 1, c))
                    grid[r + 1][c] = 0
                # check left
                if 0 <= c - 1 < cols and grid[r][c - 1] == "1":
                    q.append((r, c - 1))
                    grid[r][c - 1] = 0
                # check top
                if 0 <= r - 1 < rows and grid[r - 1][c] == "1":
                    q.append((r - 1, c))
                    grid[r - 1][c] = 0

        def dfs(r: int, c: int) -> None:
            # flag visited land
            grid[r][c] = -1

            # recurse right
            if 0 <= c + 1 < cols and grid[r][c + 1] == "1":
                dfs(r, c + 1)
            # recurse bottom
            if 0 <= r + 1 < rows and grid[r + 1][c] == "1":
                dfs(r + 1, c)
            # recurse left
            if 0 <= c - 1 < cols and grid[r][c - 1] == "1":
                dfs(r, c - 1)
            # recurse top
            if 0 <= r - 1 < rows and grid[r - 1][c] == "1":
                dfs(r - 1, c)

        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
                    # bfs(row, col)

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
