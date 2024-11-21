from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 1004:
class Solution2:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Note:
            # input:
                # nums: List[int]
                # k: int
            # output:
                # output: int
            # goal:
                # given list of integer and an inter, nums and k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's
        # Edgecase?
            # empty nums
                # 1 <= nums.length <= 105
            # k == 0
                # no replacement availble, return the longest consecutive 1's in subarray
            # all 1's or 0's in nums
                # all 1's:
                    # returns the length of num 
                # all 0's:
                    # return k
            # nums[i] != 1 or != 0
                # nums[i] is guaranteed to be 0 or 1
        # Ideas:
            # Bruteforce:
                # 2 nested loops (i and j)
                    # i loops from 0 to len(s)
                    # j starts at i until the end of nums
                        # if nums[j] == 0:
                            # increment zero counts
                            # once zero count exceeds k break out of loop
                        # increment j
                    # compute max_count
            # Sliding window:
                # use 2 pointers, l and r, for boundary
                # keep count of 0s
                # expand the window while count of 0's are less than k
                # if count of 0's exceed k:
                    # shrink window from left (l += 1)
                        # before shrinking, decrement 0 count if nums[l] is 0
                # the boundary will maintain the largest window by the end of the loop

        # Brute-force (TC: O(n^2) / SC: O(1))
        # max_count = 0
        # for i in range(len(nums)):
        #     j = i
        #     zeros = 0
        #     while j < len(nums):
        #         if nums[j] == 0:
        #             zeros += 1
        #             if zeros > k:
        #                 break
        #         j += 1
            
        #     max_count = max(max_count, j - i)
                
        # return max_count

        # Sliding window:
        # 1. expand the window while 0 counts <= k
        # 2. contract the window (from left) if 0 counts > k
            # update the 0 count prior to shift

        # Pseudocode:
        # initialize l = 0
        # z_count = 0
        # iterate the nums array (r = index)
            # if nums[r] == 0:
                # z_count += 1
            # if z_count > k:
                # if nums[l] == 0:
                    # z_count += 1
                # l += 1
        # return r - l + 1

        l = z_count = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                z_count += 1

            if z_count > k:
                if nums[l] == 0:
                    z_count -= 1
                l += 1
            
        return r - l + 1


class Solution1:
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


solution = Solution2()
start_time = time.time()
print(solution.longestOnes([0,0,0,1], 4))
print("--- %s seconds ---" % (time.time() - start_time))
