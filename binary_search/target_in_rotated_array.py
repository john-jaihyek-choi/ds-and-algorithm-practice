from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time
import math

# Note:
    # 1. nums[i] are all unique
    # 2. array is in a ascending order (but rotated by x times)
    # 3. return target if found, otherwise return -1

# Brainstorm:
    # how can I know which (left or right) of the two side is a sorted array?
        # L < M => L - M = sorted
        # L > M => some parts of M - R is sorted
    # If I know either left or right side is ensured to be sorted,
        # Then I can see if target exists between the sorted array
            # ex) if L - M = [1, 2, 3, 4] and target = 2
                # I can check if L <= target < M
        # If target is within the sorted array, I can remove the other half of the array
    # Once we find the target in the sorted array, we can search the target with basic binary search


# Solution 2:
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2

            if nums[m] == target:
                return m
            elif nums[m] < nums[r]: # right is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else: # left is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
        return -1

# Solution 1:
    # Pseudocode:
        # initialize left and right pointer
            # l starting from 0
            # r starting from length of nums array - 1
        # while l <= r:
            # set mid point to (r + l) // 2 (m)
            # if nums[m] is the target:
                # return m
            # if nums[l] <= nums[m] (sorted at left) and target is between l (inclusive) and m:
                # r = m - 1
            # if nums[l] < nums[m] and target is not between l and m:
                # l = m + 1

# TC: O(log n) / SC: O(1)
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]: # left is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # right is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1
    
solution = Solution2()
start_time = time.time()
print(solution.search([3,1], 1))
print("--- %s seconds ---" % (time.time() - start_time))