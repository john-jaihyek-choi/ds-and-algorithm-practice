from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
from operator import add, sub, mul, truediv
import time


# Leetcode 1762:
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

        # TC: O(n) / SC: O(n) if includes output res as extra space
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
