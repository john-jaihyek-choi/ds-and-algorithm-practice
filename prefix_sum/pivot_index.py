import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 724:
class Solution4:
    def pivotIndex(self, nums: List[int]) -> int:
        # input:
            # nums: List[int]
        # output:
            # output: int
        # goal:
            # given a list of integers, nums, return a pivot index
                # pivot index:
                    # index where left prefix sum == right prefix sum
        # notes:
            # return -1 if no pivot index is found
        # ideas:
            # initial intuition: compute and store prefix sum from left then go backwards
                # initialize an array to store left prefix sum
                # iterate nums from the end of the list
                    # keep right prefix sum
                    # if right prefix sum == left prefix sum, return the index
                # return -1
            # better solution: take a sum of nums ahead of time
                # initialize a sum of nums (right_sum)
                # initialize a left_sum at 0
                # iterate the nums from left
                    # if right_sum - nums[i] == left_sum:
                        # return i
                    # else:
                        # left_sum += nums[i]
                # return -1
        
        # pseudocode:
            # initialize right_sum
                # right_sum = sum(nums)
            # initialize left_sum = 0
            # iterate nums (i = index)
                # if right_sum - nums[i] == left_sum:
                    # return i
                # else:
                    # left_sum += nums[i]
            # return -1
        
        # TC: O(n) / SC: O(1)
        left_sum, right_sum = 0, sum(nums)
        for i in range(len(nums)):
            if right_sum - nums[i] == left_sum:
                return i
            else:
                right_sum -= nums[i]
                left_sum += nums[i]
        return -1
    
        # Less code:
        l_sum, total_sum = 0, sum(nums)
        for i, n in enumerate(nums):
            if total_sum - l_sum - n == l_sum:
                return i
            else:
                l_sum += n
        return -1
            

class Solution3:
    def pivotIndex(self, nums: List[int]) -> int:
        # Note:
            # input:
                # nums: List[int]
            # output:
                # output: int
            # goal:
                # given a list of integers, nums, return the pivot index
                    # must return the index of the leftmost pivot index (first appearing pivot when going from left)
                    # return - 1 if pivot index does not exist
                    # left sum of nums[0] = 0
                    # right sum of nums[len(nums)-1] = 0
        # Edgecases:
            # empty array:
                # 1 <= nums.length <= 104
            # no pivot:
                # return -1
            # single item in array:
                # return 0
            # multiple pivots:
                # return first appearing pivot (from left)
        # Ideas:
            # initial thought:
                # 2-pass solution:
                    # iterate nums from left, then store the sum to the left of the index in a separate array (left_sum_arr)
                        # ex)
                        #    [1,7,3,6,5,6]
                        #    [0,1,8,11,17,22,28] 
                    # then iterate the nums from the end of the list while maintaining the right sum
                        # if right sum == left_sum_arr[i]:
                            # set pivot = i
        
        # 2-pass solution:
        # Pseudocode:
            # initialize an empty arr, left_sum_arr = []
            # initialize output = -1
            # initialize l_sum = 0
            # iterate the nums array (i = index)
                # left_sum_arr.append(l_sum)
                # l_sum += nums[i]
            # r_sum = 0
            # iterate the nums array from the end of the list (i = index)
                # if r_sum == left_sum_arr[i]:
                    # output = i
                # r_sum += nums[i]
            # return output

        # TC: O(n) / SC: O(n)
        left_sum_arr = []
        output = -1
        l_sum = r_sum = 0
        for n in nums:
            left_sum_arr.append(l_sum)
            l_sum += n
        
        for i in range(len(nums) - 1, -1, -1):
            if r_sum == left_sum_arr[i]:
                output = i
            r_sum += nums[i]
        
        return output

        # Possibility for optimization:
            # any way to do this without n space?
                # is it possible to know the left and right sum without a memory?
                    # Yes, if I have total sum calculated in advance, I can compute right sum with left sum
        
        # idea:
            # calculate the total sum of nums (O(n))
            # keep a variable for l_sum
            # iterate the nums array (i = index, n = nums[i])
                # if (total_sum - nums[i]) / 2 == l_sum:
                    # return i
            # return -1
        
        # TC: O(n) / SC: O(1)
        total_sum, l_sum = sum(nums), 0
        for i, n in enumerate(nums):
            if (total_sum - n) / 2 == l_sum:
                return i
            l_sum += n
        
        return -1

        # no division solution:
        total_sum, l_sum = sum(nums), 0
        for i, n in enumerate(nums):
            if (total_sum - l_sum - n) == l_sum:
                return i
            l_sum += n
        
        return -1


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