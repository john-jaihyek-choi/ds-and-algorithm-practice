from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


# Leetcode 885:


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
        Rules:
            1. 3 += identical candies, horizontally and vertically, can be crushed at the SAME TIME
                - position becomes 0
            2. After every crush, if there's items above the crushed candies, it needs to fill the empty spaces
                - no new candies will be dropped
            3. repeat step 1 and step 2
            4. Once no identical items found (stable board), return the board
        General functions:
            1. Mark cells to be crushed
                1. Check/mark Horizontal
                2. Check/mark Vertical
            2. Crush cells and shift
                1. Crush cells
                2. shift cells
            3. Check stability
            4. Repeat

        Intuition:
            1. Mark cells
                1. iterate each rows by window of 3
                    - update left, center, right cells to abs value of itself
                    - if left == center == right:
                        - negate left, center, and right (marking it as "to be crushed")
                        - mark board unstable since change is made to the board
                2. iterate each column by window of 3
                    - update left, center, right cells to abs value of itself
                    - if left == center == right:
                        - negate left, center and right
                        - mark board unstable since change is made to the board
            2. while board is unstable:
                - keep track of current bottom index starting at the len(board[0]) - 1
                - iterate each column from the bottom
                    - if cell value > 0 (positive number):
                        - board[bottom][c] = board[r][c]
                        - update bottom by subtracting 1
            3. return board
        """
        # TC: O(m^2 * n^2) / SC: O(1)
        if not board:
            return board
        stable = self.isStable(board)  # TC: O(m * n) / SC: O(1)

        if not stable:
            self.crushAndShift(board)  # TC: O(m * n + n - k) / SC: O(1)

        return board if stable else self.candyCrush(board)

    # Crush and shift
    def crushAndShift(self, board: List[List[int]]):
        # TC: O(m * (n + n - k)) where k is number of empty cells / SC: O(1)
        # Crush
        for c in range(len(board[0])):
            bottom = len(board) - 1

            for r in range(len(board) - 1, -1, -1):
                if board[r][c] > 0:
                    board[bottom][c] = board[r][c]
                    bottom -= 1

            # Shift
            for r in range(bottom, -1, -1):
                board[r][c] = 0

    # Mark cells to be crushed
    def isStable(self, board: List[List[int]]) -> bool:
        # TC: O(m * n) / SC: O(1)
        stable = True

        # mark rows:
        for r in range(len(board)):
            for c in range(len(board[r]) - 2):
                left = abs(board[r][c])
                center = abs(board[r][c + 1])
                right = abs(board[r][c + 2])

                if left == center and center == right and left != 0:
                    board[r][c] = -abs(left)
                    board[r][c + 1] = -abs(center)
                    board[r][c + 2] = -abs(right)
                    stable = False

        # mark cols:
        for c in range(len(board[0])):
            for r in range(len(board) - 2):
                top = abs(board[r][c])
                center = abs(board[r + 1][c])
                bottom = abs(board[r + 2][c])

                if top == center and center == bottom and top != 0:
                    board[r][c] = -abs(top)
                    board[r + 1][c] = -abs(center)
                    board[r + 2][c] = -abs(bottom)
                    stable = False

        return stable


solution = Solution()
start_time = time.time()
print(
    solution.candyCrush(
        [
            [110, 5, 112, 113, 114],
            [210, 211, 5, 213, 214],
            [310, 311, 3, 313, 314],
            [410, 411, 412, 5, 414],
            [5, 1, 512, 3, 3],
            [610, 4, 1, 613, 614],
            [710, 1, 2, 713, 714],
            [810, 1, 2, 1, 1],
            [1, 1, 2, 2, 2],
            [4, 1, 4, 4, 1014],
        ]
    )
)
print("--- %s seconds ---" % (time.time() - start_time))
