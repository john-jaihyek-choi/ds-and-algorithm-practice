from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Note:
            - no subset is a valid subset
            - no duplicate subsets
                - ex) where nums = [1, 2, 3]
                    - [1, 2] and [2, 1] are same subsets
                        - using set might be useful here
        Intuition:
            - Basic Recursion:
                - starting with empty subset, [], and i of 0 (from the beginning of the array)
                    - recurse to add nums[i] or don't add nums[i]
                - recursion function:
                    - base case: if i >= len(nums), return out of the recursion function
                    - add nums[i] to the subset, then recurse to i + 1 th scenario
                    - DON'T add nums[i] to the subset, then recurse to i + 1 th scenario
        """

        # Recursion
        # TC: O(n * 2^n) / SC: O(n), O(2^n) for output list
        res = []

        def dfs(subset: List[int], i: int) -> List[int]:
            if i >= len(nums):
                res.append(subset.copy())
                return

            # recurse the path that includes nums[i]
            subset.append(nums[i])
            dfs(subset, i + 1)

            # recurse the path that excludes nums[i]
            subset.pop()
            dfs(subset, i + 1)

        dfs([], 0)
        return res


solution = Solution()
start_time = time.time()
print(solution.subsets([1, 2, 3]))
print("--- %s seconds ---" % (time.time() - start_time))
