from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Note:
            - Can't rob 2 adjacent houses
                - must take atleast i + 2 step IF I robbed house at i
            - I'm not required to rob house at each i
                - I can skip for next optimal number
            - Pattern:
                - Choices:
                    1. Steal at i
                        - if I steal at i, then I cannot steal at i + 1
                    2. Don't steal at i
                        - I can steal i + 1
        Intuition:
            - Basic Recursion:
                - recurse from i = 0
                - recursion function:
                    - base case: if i >= len(nums):
                        - return 0
                    - return the maximum between nums[i] + dfs(i + 2) or nums[i + 1]
                        - repeat recursion
            - Dynamic Programming:
                - sub problems:
                    1. steal at i and steal at i + 2 th or later
                    2. don't steal at i and steal i + 1 or later
                - iterate from the back of the nums and update maximum nums[i] at each point
        """

        # Dynamic Programming:
        # 1. steal at i and i + 2 or later
        # 2. don't steal at i and steal i + 1 or later
        if len(nums) <= 2:
            return max(nums)

        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])

        return max(nums[0], nums[1])

        # Recursion
        # TC: O(2^n) / SC: O(n)
        def dfs(i: int) -> int:
            if i >= len(nums):
                return 0
            return max(nums[i] + dfs(i + 2), dfs(i + 1))

        return dfs(0)


start_time = time.time()
solution = Solution()
print(solution.minCostClimbingStairs(10))
print("--- %s seconds ---" % (time.time() - start_time))
