import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 283:
class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Note:
            # input:
                # nums: List[int]
            # output:
                # output: None
            # goal:
                # modify nums input in-place so that all 0's in the array are moved to the end of the list
        # potential scenarios:
            # empty list
                # nums arr will have atleast 1 item
            # no 0s
                # no changes to be made
        # Approach:
            # two-pointer:
                # l and r starts at 0
                # if nums[r] > 0
                    # switch nums[l] with nums[r]
                    # increment l
                # increment r
        
        # Pseudocode:
            # l = r = 0
            # while r < len(nums):
                # if nums[r] != 0:
                    # nums[l], nums[r] = nums[r], nums[l]
                    # l += 1
                # r += 1
        
        l = r = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

        



class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # In-place solution
        # input:
            # nums: List[int]
        # goal: return the updated input nums array
            # all 0's must be moved to the end of the list
        # brainstorm:
            # using two pointers to switch numbers
                # when should the number switch?
                    # when nums[r] is not 0
                        # what if nums[l] and nums[r] are both 0?
                            # move the r to next number. eventually l will reach the skipped 0
                # where should each pointers begin?
                    # l and r both 0
                # when should the loop stop?
                    # when r pointer reaches the end of the line
        # Two-pointer approach:
            # l and r pointer
                # when does l move?
                    # when swap happens
                # when does r move?
                    # every iteration
        # Variables to track:
            # l: int
            # r: int
        # Pseudocode:
            # condition guard to return output if length of the input array is less than 2
            # initialize the l pointer
                # l = 0
            # iterate while r is less than the length of the nums array
                # if nums[r] != 0:
                    # switch nums[l] and nums[r]
                    # increment l
            # return nums
        
        if len(nums) < 2:
            return nums
        
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
        return nums

class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    # extra array approach:
                # initialize an empty array 
                # initialize a zero counter at 0
                # iterate on the input array
                    # append any non-zero value to the empty array
                    # when a number is 0, increment the zero counter
                # iterate zero counter many times:
                    # append 0 to the empty array
                # return empty array
        res = []
        zero_counter = 0

        for n in nums:
            if n != 0:
                res.append(n)
            else:
                zero_counter += 1

        for i in range(zero_counter):
            res.append(0)

        return res
        
        
        

solution = Solution3()
start_time = time.time()
print(solution.moveZeroes([1,0]))
print("--- %s seconds ---" % (time.time() - start_time))