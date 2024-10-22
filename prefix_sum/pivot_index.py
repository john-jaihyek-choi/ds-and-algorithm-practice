import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 724:
class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        # Getting the right sum at the beginning and updating the right sum as iterating the array
        # TC: O(n) / SC: O(1)
        l_sum, r_sum = 0, sum(nums) # TC O(n) / SC O(1)

        for i, n in enumerate(nums): # O(n)
            r_sum -= n # O(1)
            
            if r_sum == l_sum: # O(1)
                return i # O(1)

            l_sum += n # O(1)

        return -1 # O(1)
    
class Solution1:
    def pivotIndex(self, nums: List[int]) -> int:
        # input:
            # nums: List[int]
        # goal: return the INDEX of the array that's pivot index
            # pivot index = left_sum == right_sum
            # MUST return the LEFT MOST PIVOT INDEX
        # Note:
            # first find the left_sum of the array
            # then find the right_sum of the array
            # iterate the array and return pivot index if any
                # otherwise return -1
        # Variable:
            # l_sum: int
                # starts at 0
            # r_sum: int
                # starts at 0
            # r_sum_array: List[int]
                # r_sum_array[i] is the r_sum at i
        # Pseudocode:
            # initialize l_sum = 0
            # initialize r_sum = 0
            # iniitalize an array with default value of 0, length of nums many times (r_sum_array)
            # iterate the nums from the end of the nums (i = index, n = nums[i])
                # set r_sum_array[i] to r_sum
                # add value n to r_sum
            # iterate the r_sum_arry starting from 0 (i = index, sum_r = r_sum_array[i])
                # if l_sum == sum_r:
                    # return i
                # add nums[i] to l_sum
            # return -1

        # TC: O(n) / SC: O(n)
        l_sum, r_sum = 0, 0 # O(1)
        r_sum_array = [0] * len(nums) # TC O(1) / SC O(n)
        for i in range(len(nums) - 1, -1, -1): # O(n)
            r_sum_array[i] = r_sum # O(1)
            r_sum += nums[i] # O(1)

        for i, n in enumerate(r_sum_array): # O(n)
            if l_sum == r_sum_array[i]: # O(1)
                return i 
            l_sum += nums[i] # O(1)
        
        return -1 # O(1)


solution = Solution1()
start_time = time.time()
print(solution.pivotIndex([1,7,3,6,5,6]))
print("--- %s seconds ---" % (time.time() - start_time))