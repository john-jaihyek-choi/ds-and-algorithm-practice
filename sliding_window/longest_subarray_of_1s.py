from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 1493:
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Note:
            # input:
                # nums: List[int]
            # output:
                # output: int
            # goal:
                # given a list of 0s and 1s, nums, return the size of the longest non-empty subarray containing only 1's in the resulting array
                # ** 1 element MUST be deleted
        # Edge-cases?
            # empty array:
                # 1 <= nums.length <= 105
            # all 1's:
                # return len(nums) - 1
            # all 0's:
                # return 0
        # Ideas:
            # brute-force:
                # 2 nested loops:
                    # i starts 0 and ends at len(nums)
                    # j starts at i and ends at len(nums)
                        # if z_count > 1, break out of loop
                        # update max_subarray_length before breaking out
            # optimal approach (sliding window):
                # use l and r for window boundary
                # keep track of 0 counts (z_count)
                # expand window until z_count > 1
                # if z_count > 1:
                    # shrink (from left) the window
                        # before shrinking, decrement z_count if nums[l] is 0
        
        # brute-force:
        # TC: O(n^2) / SC: O(1)
        if sum(nums) == 0:
            return 0

        max_subarray_length = 1
        for i in range(len(nums)):
            z_count = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    z_count += 1

                if z_count > 1:
                    break

                max_subarray_length = max(max_subarray_length, j - i)

        return max_subarray_length

        # Optimal approach (sliding window):
        # initialize l = 0
        # initialize z_count = 0
        # iterate the nums array (r = index)
            # if z_count >1:
                # l += 1
        # return r - l

        # TC: O(n) / SC: O(1)
        l = z_count = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                z_count += 1

            if z_count > 1:
                if nums[l] == 0:
                    z_count -= 1

                l += 1

        return r - l


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