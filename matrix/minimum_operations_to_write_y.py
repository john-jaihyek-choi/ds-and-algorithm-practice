from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


# Leetcode 3071:


class Solution3:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        # TC: O(n^2 + (x + y)) / SC: O(1)
        yCells, nonYCells = [0, 0, 0], [0, 0, 0]  # SC: O(3) -> O(1)
        n = len(grid)

        # O(n^2)
        for row in range(n):  # O(n)
            for col in range(n):  # O(n)
                if self.isYcell(row, col, n):
                    yCells[grid[row][col]] += 1
                    continue
                nonYCells[grid[row][col]] += 1

        min_ops = float("inf")

        # O(x + y)
        for y in range(3):  # O(3) == O(1)
            for nonY in range(3):  # O(3) == O(1)
                if y == nonY:
                    continue

                ops = 0
                ops += sum(yCells) - yCells[y]  # O(x)
                ops += sum(nonYCells) - nonYCells[nonY]  # O(y)

                min_ops = min(min_ops, ops)

        return min_ops

    def isYcell(self, row: int, col: int, n: int) -> bool:
        return (
            row == col
            and row < (n // 2)
            or (row + col + 1) == n
            and row < (n // 2)
            or row >= (n // 2)
            and col == (n // 2)
        )


class Solution2:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        """
        Note:
            Possible Cell values - 0, 1, 2
            Y-Cell:
                1. starting top left cell ending at center of the grid
                2. starting top right cell ending at center of the grid
                3. starting center of the grid ending at bottom center of the grid
            Condition:
                - All Y values must be equal
                - All non-Y values bust be equal
                - Y values MUST be different from non-Y values
            Objective:
                - Return minimum number of operations needed to write letter Y on grid
        Intuition:
            - Identify Y cells in an array
                - ex) [1, 2, 1, 1]
                - left diagonal
                    - if a row == col
                - right diagonals
                    - if row + col == n AND row < (n // 2)
                - bottom Y
                    - if row >= (n // 2) and col == (n // 2)
            - Identify non-Y cells in an array
                - ex) [2, 1, 0, 0, 0]
                - all non Y cells that falls under the "Y-cell" criteria
            - iterate on Y cells (y-cell)
                - iterate on non-Y cells (non-y-cell)
                    - iterate on nested loop with each loop iterating 3 times (0, 1, then 2)
                        - initialize operation count to 0
                        - i = index of outer loop
                        - j = index of inner loop
                        - if i == j value:
                            skip
                        - if y-cell != i or non-cell == i:
                            increment operation counter
                        - after completion of each inner loop, update min ops
        """

        # TC: O(n^2 + (x + y)) / SC: SC: O(n^2)
        yCells, nonYCells = [], []  # SC: O(n)
        n = len(grid)

        # O(n^2)
        for row in range(n):  # O(n)
            for col in range(n):  # O(n)
                if self.isYcell(row, col, n):
                    yCells.append(grid[row][col])
                    continue
                nonYCells.append(grid[row][col])

        min_ops = float("inf")

        # O(x + y)
        for y in range(3):  # O(3) == O(1)
            for nonY in range(3):  # O(3) == O(1)
                if y == nonY:
                    continue

                ops = 0
                ops += sum(
                    1 for cell in yCells if cell != y
                )  # O(x) where x == n - non-Y cells
                ops += sum(
                    1 for cell in nonYCells if cell != nonY
                )  # O(y) where y == n - x

                min_ops = min(min_ops, ops)

        return min_ops

    def isYcell(self, row: int, col: int, n: int) -> bool:
        return (
            row == col
            and row < (n // 2)
            or (row + col + 1) == n
            and row < (n // 2)
            or row >= (n // 2)
            and col == (n // 2)
        )


class Solution1:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        """
        Note:
            - cell belongs to Letter Y if...
                - diagonal starting top-left cell ending at center cell of the grid
                - diagonal starting top-right cell ending at center cell of the grid
                - vertical line starting from center ending at center cell of the grid
        Challenge:
            - identifying which cell belongs to Y and which don't
                - 4 cell are Guaranteed to be part of Y
                    - grid[0][0] == top-left
                    - grid[0][n - 1] == top-right
                    - grid[n][n // 2] == center bottom
                    - grid[n // 2][n // 2] == center of the grid
                - How I would be able to identify if the rest of the cells are part of Y?
                    - if cell's row is greater than or equal to the n // 2 AND column of the cell is n // 2:
                        - it must be part of Y
                    - if cell's row is greater than 0 AND less than n // 2 AND:
                        - there are 2 cells that must be part of Y (the "v" part of the y)
                            - the top left diagonal
                            - the top right diagonal
            - identifying which value to change the "Y" cells into:
                - there's 3 possibilities -> 0, 1, 2
                - to make the minimum operation possible, I'll have to consider:
                    - what other parts of "Y" values are
                    - what the rest of the cells (non-Y cells) has
        Idea:
            - 1. Identify Y cells and non-Y cells
                - Must identify/separate the non-Y cell values and Y-cell values
                - iterate on the grid:
                    - is Y-cell if...
                        - Left-diagonal: x (row) < (n // 2) AND x == y
                        - Right-diagonal: x (row) < (n // 2) AND x + y == n - 1
                        - Center-cell: x (row) == (n // 2) AND x == y
                        - Vertical-cells: x (row) > (n // 2) AND y == (n // 2)
                    - else, it is non-Y cell
            - 2. Identify the minimum operation needed to write letter Y
                - iterate 0, 1, and 2 (i = index)
                    - iterate y-cells (n = y-cells[i])
                        - if y-cells[i] == n:
                            - increment operations by 1
                    - iterate non-y cells  (n = non-y-cells[i])
                        - if non-y-cells[i] == n:
                            - increment operations by 1
                    - update max_operations with total operations for current iteration
        """
        # TC: O(n^2 + (n - k) + k) == O(n^2) / SC: O(n^2)

        n = len(grid)
        y_cells = []
        all_other_cells = []

        for x in range(n):  # TC: O(n)
            for y in range(n):  # TC: O(n)
                if self.isYCell(x, y, n):
                    y_cells.append(grid[x][y])
                else:
                    all_other_cells.append(grid[x][y])

        min_operations = float("inf")

        for y_val in range(3):  # TC: O(3) == O(1)
            for non_y_val in range(3):  # TC: O(3) == O(1)
                if y_val == non_y_val:
                    continue

                operations = 0

                operations += sum(
                    1 for n in y_cells if n != y_val
                )  # TC: O(k) where k == available Y cells
                operations += sum(
                    1 for n in all_other_cells if n != non_y_val
                )  # TC: O(n^2 - k) where n is all items in grid, k is available Y cells

                min_operations = min(min_operations, operations)

        return min_operations

    # identify Y cells and non-Y cells
    def isYCell(self, x: int, y: int, n: int):
        return (
            ((x < (n // 2)) and x == y)
            or ((x < (n // 2)) and x + y == n - 1)
            or ((x >= (n // 2)) and y == (n // 2))
        )


class Solution2:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        """
        Optimization:
            - I must iterate on every grid for me to be able to check if the value is what is expected.
                - So, no real optimization could be done here
            - However, space could be optimized by remembering the count of 0, 1, and 2s when iterating each cells to begin with
                - since 0, 1, and 2 are the only possible cell value:
                    - I can keep count of the 0, 1, and 2s using array indexing
                        - ex)
                            - y_cell_counts = [1, 2, 3]
                            - all_other_cells_count = [1, 5, 2]
        """
        # TC: O(n^2 + 1) == O(n^2) / SC: O(1)

        n = len(grid)
        y_cells_counts = [0, 0, 0]
        all_other_cells_counts = [0, 0, 0]

        for x in range(n):  # TC: O(n)
            for y in range(n):  # TC: O(n)
                cell = grid[x][y]

                if self.isYCell(x, y, n):
                    y_cells_counts[cell] += 1
                else:
                    all_other_cells_counts[cell] += 1

        min_operations = float("inf")

        for y_val in range(3):  # TC: O(3) == O(1)
            for non_y_val in range(3):  # TC: O(3) == O(1)
                if y_val == non_y_val:
                    continue

                operations = 0
                operations += (
                    sum(y_cells_counts) - y_cells_counts[y_val]
                )  # TC: O(3) == O(1)
                operations += (
                    sum(all_other_cells_counts) - all_other_cells_counts[non_y_val]
                )  # TC: O(3) == O(1)

                min_operations = min(min_operations, operations)

        return min_operations

    # identify Y cells and non-Y cells
    def isYCell(self, x: int, y: int, n: int):
        return (
            ((x < (n // 2)) and x == y)
            or ((x < (n // 2)) and x + y == n - 1)
            or ((x >= (n // 2)) and y == (n // 2))
        )


solution = Solution2()
start_time = time.time()
print(solution.minimumOperationsToWriteY([[1, 2, 2], [1, 1, 0], [0, 1, 0]]))
print("--- %s seconds ---" % (time.time() - start_time))
