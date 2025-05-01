from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 84:


# Retried 5/1/2025
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Intuition:
            - Monotonic stack:
                - keep a stack of visited heights
                    - keep the order of the heights strictly in non-decreasing order
                        - instead of keeping an actual value of heights[i] in the stack
                            - I'd use i and the height pair in the stack
                                - stack = [ (i, height[i]), ...]
                - iterate on heights (i = index, height = heights[i])
                    - while stack and heights[stack[-1]] > heights[i]
                        - pop stack[-1]
                            - when popping stack, compute possible rectangles (both the rectangle itself and where it extends up to current height)
                                - this is possible because I have access to...
                                    - width of the rectagle: i - stack[-1]
                                    - height of the rectangle: heights[i]
                    - append the i and height[i] pair to the stack
                        - I must use the latest popped i in the stack[-1] for i
        Demonstration:
            - stack = [ 1, 5 ]
            - larget_area = 6
        """

        # TC: O(n) / SC: O(n)
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            left_most = i
            while stack and stack[-1][1] > height:
                j, h = stack.pop()
                max_area = max(max_area, (i - j) * h)
                left_most = j

            stack.append((left_most, height))

        while stack:
            i, h = stack.pop()
            max_area = max(max_area, (len(heights) - i) * h)

        return max_area


class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        # stack to store individual bar in an increasing/ascending order
            # when visiting the next bar, if the next bar is smaller, then pop the existing bars until we find a bar <= the current
        """

        stack = []
        max_area = float("-inf")
        for i, h in enumerate(heights):
            pair = [i, h]

            while stack and h < stack[-1][1]:
                j, prev_h = stack.pop()
                pair[0] = j
                max_area = max(max_area, (i - j) * prev_h)

            stack.append(pair)

        while stack:
            i, h = stack.pop()
            w = len(heights) - i
            area = w * h
            max_area = max(max_area, area)

        return max_area


"""
# Note:
    # a bar can can extend to the right if the height of bar in the right is greater than or equal to height of itself
    # bars to the left of itself can be popped until a bar with lower height is found
        # this allows to extend the area to the left of the current bar

# Solution 1:
    # Pseudocode:
        # initialize an empty stack to store the index and height pair (stack)
        # initialize a max area value to 0 (max_area)
        # iterate the heights array from the 0th index
            # set current index and height pair (index, height[i])
            # while there's an item in the stack AND 1th index of the item on the top of the stack is greater than the current height
                # if true:
                    # calculate the area of the item being popped
                        # width = current index - index of the item being deleted
                        # height = stack[-1][1]
                    # set the max_area between itself and the calculated area
                    # overwrite the index of the pair to the index of the pair deleting
                    # pop the top of the stack
            # append the current index and height pair (index, height[i]) to the stack
        # while stack is non-empty:
            # calculate the area
                # len(heights) - index of the pair * height of the pair
                # set the max_area between itself and the calculated area
                # pop the top of the stack
        # return max_area
"""


# TC: O(n * m) where m is length of the stack / SC: O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # O(1)
        max_area = 0  # O(1)

        for i in range(len(heights)):  # O(n)
            pair = [i, heights[i]]  # O(1)

            while (
                stack and stack[-1][1] >= heights[i]
            ):  # O(1) since bar (height[i]) is being popped at most 1 time. It never re-enters the stack
                area = (i - stack[-1][0]) * stack[-1][1]  # O(1)
                max_area = max(max_area, area)  # O(1)
                pair[0] = stack[-1][0]  # O(1)
                stack.pop()  # O(1)

            stack.append(pair)  # O(1)

        while stack:  # O(n)
            area = (len(heights) - stack[-1][0]) * stack[-1][1]  # O(1)
            max_area = max(max_area, area)  # O(1)
            stack.pop()  # O(1)

        return max_area  # O(1)


solution = Solution1()
start_time = time.time()
print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print("--- %s seconds ---" % (time.time() - start_time))
