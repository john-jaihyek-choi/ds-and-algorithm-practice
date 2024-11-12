from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 34

# Note:
    # nums is guaranteed to be in an non-decreasing order
# Goal:
    # find the starting and the ending position of a given target value in the nums array
# Potential Edge-cases:
    # no target in the array:
        # [-1,-1]
    # no items in the nums array:
        # return [-1, -1]
    # non digit character in nums array:
        # the constraint gurantees an integer at nums[i]
    # what if there's only 1 target in the nums array?
        # Do I need to return starting and ending position as the same index?
            # Assumption: set ending position equal to starting position

# Bruteforce:
    # iterate the nums array from left
        # when a nums[i] == target
            # store the index in the starting position output[0]
            # stop iterating
    # iterate the nums array from the right
        # when nums[i] == target
            # store the index in the ending position output[1]

# TC: O(n) / SC: O(1)
class Solution1:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]
        for i, n in enumerate(nums):
            if n == target:
                output[0] = i
                break
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                output[1] = i
                break
        
        return output
    
# Optimization Idea:
    # Because the array is sorted, binary search could help with reducing the time complexity by eliminating the half of the array each loop
    # If nums[m] == target:
        # nums[m] is potentially a starting or an ending position of the target
        # which of the two section, right or left, can I eliminate?
            # Both can be useful
                # so, 2 separate loops with 2 separate conditions
    # 2 separate loops with unique conditions:
        # 1. search for a value strictly less than 8
            # by the end of the iteration, l should ideally point to first instance of target at i
        # 2. search for a value strictly greater than 8
            # by the end of the iteration, r should ideally point to the last instance of target at i
    # What if nums[l] or nums[r] are not target?
        # if both aren't target:
            # return [-1, -1]
        # if either aren't target:
            # return [l or r, l or r]
        # if both are target:
            # return [l, r]

class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Pseudocode:
            # initialize an output array
                # output = []
            # 1. binary search nums for value strictly less than target
                # l, r = 0, len(nums) - 1
                # while l <= r:
                    # m = (l + r) // 2
                    # if nums[m] < target:
                        # l = m + 1
                    # else:
                        # r = m - 1
            # 2. binary search nums for value strictly greater than target
                # l, r = 0, len(nums) - 1
                # while l <= r:
                    # m = (l + r) // 2
                    # if nums[m] > target:
                        # r = m - 1
                    # else:
                        # l = m + 1

        # TC: O(log n) / SC: O(1)
        l1, r1 = 0, len(nums) - 1
        while l1 <= r1:
            m = (l1 + r1) // 2
            if nums[m] < target:
                l1 = m + 1
            else:
                r1 = m - 1

        l2, r2 = 0, len(nums) - 1
        while l2 <= r2:
            m = (l2 + r2) // 2
            if nums[m] > target:
                r2 = m - 1
            else:
                l2 = m + 1

        if (l1 < len(nums) and r2 >= 0) and (nums[l1] == target and nums[r2] == target):
            return [l1, r2]
        
        return [-1, -1]
    
# Cleaner / Concise version:
class Solution3:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        def searchPosition(isLeft: bool) -> int:
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target or (isLeft and nums[m] == target):
                    r = m - 1
                else:
                    l = m + 1
            return l if isLeft else r

        l_index = searchPosition(True)
        r_index = searchPosition(False)

        if (l_index < len(nums) and r_index >= 0) and (nums[l_index] == target and nums[r_index] == target):
            return [l_index, r_index]
        
        return [-1, -1]



solution = Solution1()
start_time = time.time()
print(solution.search([-1,0,2,4,6,8], 0))
print("--- %s seconds ---" % (time.time() - start_time))