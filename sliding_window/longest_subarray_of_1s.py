from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 1493:
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # input:
            # nums: List[int]
                # nums[i] is binary, 0 or 1
        # goal: return the length of the longest non-empty subarry containing only 1's in the resulting array
            # return 0 if there's no such subarray
                # if nums only contain 0, then the return value would be 0
        # Brainstorm:
            # using sliding window approach
            # 2 pointers, l and r
                # r moves each iteration
                # l moves if the count of 0s in the subarray > 1
                    # before l moves, if the element being removed is 0, then decrement the 0 counter
        # Variable:
            # l: int
            # r: int
            # zero_count: int
                # start at 0
        # Pseudocode:
            # initialize l pointer at 0 (l)
            # initialize zero_count at 0 (zero_count)
            # iterate the nums array (r = index, n = nums[r])
                # if n == 0:
                    # increment the zero_count by 1
                # if zero_count > 1:
                    # if nums[l] == 0:
                        # zero_count -= 1
                    # increment l by 1
            # retun r - l
        
        # TC: O(n) / SC: O(1)
        l, zero_count = 0, 0 # O(1)
        for r, n in enumerate(nums): # O(n)
            if n == 0: # O(1)
                zero_count += 1
            
            if zero_count > 1: # O(1)
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            
        return r - l # O(1)

solution = Solution()
start_time = time.time()
print(solution.longestSubarray([1,1,0,1]))
print("--- %s seconds ---" % (time.time() - start_time))