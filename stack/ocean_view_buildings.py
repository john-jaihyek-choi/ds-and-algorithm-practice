from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
from operator import add, sub, mul, truediv
import time


# Leetcode 1762:
class Solution4:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        Alternative solution:
            - Monotonic stack, traversing backwards:
                - initialize stack
                    - maintain items in monotonic increasing order
                - iterate heights from the end of the array:
                    - while stack is non-empty and heights[stack[-1]] >= heights[i]:
                        - pop from the stack
                    - append current i to the stack
                - return the stack
        """

        # TC: O(n) / SC: O(1) and O(n) if includes output res as extra space
        max_right = 0
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if max_right < heights[i]:
                res.append(i)

                max_right = heights[i]

        res.reverse()
        return res


class Solution3:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        Alternative solution:
            - Monotonic stack, traversing backwards:
                - initialize stack
                    - maintain items in monotonic increasing order
                - iterate heights from the end of the array:
                    - while stack is non-empty and heights[stack[-1]] >= heights[i]:
                        - pop from the stack
                    - append current i to the stack
                - return the stack
        """

        # TC: O(n) / SC: O(n)
        stack = []
        res = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()

            if not stack:
                res.append(i)

            stack.append(i)

        res.reverse()
        return res


class Solution2:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        Alternative solution:
            - Stack to store indicies in order:
                - initialize an empty stack
                    - will be storing heights in monotonic decreasing order
                        - descending
                - iterate heights:
                    - if stack is non-empty and the height at the index at the top of the stack is smaller
                        - pop the stack
                    - append the current index
                - return the stack
        """

        # TC: O(n) / SC: O(1) and O(n) if includes output res as extra space
        res = []
        for i, h in enumerate(heights):
            while res and heights[res[-1]] <= h:
                res.pop()
            res.append(i)

        return res


class Solution1:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        Note:
            - n buildings
            - heights array:
                - heights[i] = height of the building
            - ocean view:
                - if building to max heights[i]'s right < heights[i]:
                    - ocean view
                - else:
                    - not an ocean view
            - return indicies of the buildings WITH ocean view
        Intuition:
            - monitor right max traversing backwards from the array
                - initialize deque to append from left (for ordering)
                - initialize max building at 0 (max_right)
                - iterate from the end of the heights array:
                    - if heights[i] > max_right:
                        - append i to to the deque from the left
                - return the deque
        """

        # TC: O(n) / SC: O(n)
        res = deque()
        max_right = 0

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_right:
                res.appendleft(i)

            max_right = max(max_right, heights[i])

        return list(res)
