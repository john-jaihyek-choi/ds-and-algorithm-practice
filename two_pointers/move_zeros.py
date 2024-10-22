import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 283:
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # input:
            # nums: List[int]
        # goal: return the updated input nums array
            # all 0's must be moved to the end of the list
        # Two-pointer approach:
            # l and r pointer
                # when does l move?
                    # l moves when nums[l] is not 0
                # when does r move?
                    # r moves each iteration
            # loop while r is less than the length of the nums
        # Variables to track:
            # l: int
            # r: int
        # Pseudocode:
            # initialize a l and r pointer
                # l and r starting from 0
            # iterate the nums array while r less than length of the nums
                # if nums[l] is not 0:
                    # increment l by 1
                # if nums[l] equal to 0 and nums[r] not equal to 0
                    # switch nums[l] with nums[r]
                # increment r by 1
            # return the nums array
        
        if len(nums) <= 1:
            return nums

        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0 and nums[l] == 0:
                temp = nums[l]
                nums[l], nums[r] = nums[r], temp
            r += 1

            

        return nums
        

solution = Solution()
start_time = time.time()
print(solution.moveZeroes([1,0]))
print("--- %s seconds ---" % (time.time() - start_time))