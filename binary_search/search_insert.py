from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Note:
            # 1. check if the target exists in nums array
                # If target exists, return the index of the target in nums
            # 2. If target does not exists, return the index where it would be if it were inserted in order

        # Potential Edge cases:
            # empty array, non digit item in the index:
                # the constraint guarantees that the nums will have atleast 1 value
            # 

        # Bruteforce (O(n) operation):
            # iterate the nums array
                # if nums[i] >= target:
                    # return i
            # if the iteration is complete, return length of the nums array

        # Optimal Solution Idea:
            # search for target num using binary search
                # if nums[m] == target:
                    # return m
            # if no index is returned, return l

        # Pseudocode:
            # initialize l and r pointers:
                # l = 0
                # r = len(nums) - 1
            # while l <= r:
                # m = (l + r) // 2
                # if nums[m] == target;
                    # return m
                # elif nums[m] < target:
                    # l = m + 1
                # else:
                    # r = m - 1
            # return l
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return l
        
    

solution = Solution()
start_time = time.time()
print(solution.searchInsert(10))
print("--- %s seconds ---" % (time.time() - start_time))