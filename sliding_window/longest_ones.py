from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 1004:
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # input:
            # nums: List[int]
                # nums[i] guaranteed to be 1 or 0
            # k: int
                # k always less than or equal to len(nums) AND greater than 1
        # goal: return the integer, maximum number of consecutive 1s, in the array after flipping 0s at most k many times
        # Note:
            # Sliding-window problem
            # no need to contract the window since the goal is to find the maximum length of the subarray
        # Variables to track:
            # l: int
            # r: int
            # 0_counts: int
        # Brainstorm:
            # track 2 pointers, l and r
                # both starting at 0
            # expand the sliding window as long as r - l + 1 (size of the window) - 0_counts <= k
            # else, stop expanding and increment l
                # consideration before incrementing l
                    # if nums[l] is 0, then decrement the 0_count by 1
            # once r reaches the end of the nums length, stop
        # Pseudocode:
            # initialize l pointer to 0 (l)
            # initialize 0_counts to 0
            # iterate the nums array (r = index, n = nums[r])
                # if n == 0:
                    # increment the 0_count by 1
                # if 0_counts > k:
                    # if nums[l] == 0:
                        # decrement the 0_count by 1
                    # increment the l pointer by 1
            # return r - l + 1 

        # TC: O(n) / SC: O(1)
        l, z_counts = 0, 0 # O(1)
        for r, n in enumerate(nums): # O(n)
            if n == 0: # O(1)
                z_counts += 1

            if z_counts > k: # O(1)
                if nums[l] == 0: # O(1)
                    z_counts -= 1
                l += 1
        
        return r - l + 1 # O(1)


solution = Solution()
start_time = time.time()
print(solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print("--- %s seconds ---" % (time.time() - start_time))
