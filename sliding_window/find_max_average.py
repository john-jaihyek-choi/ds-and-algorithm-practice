from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 643:
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # input:
            # nums: List[int]
            # k: int
                # k can only be as big as n where n = len(nums)
        # goal: find the contiguous subarray where len of the subarry == k, and return the maximum average value
        # Note:
            # k == window of the subarray
            # window will slide once the size of the window reaches k
            # round the avaerage to 10^-5 
        # Variable to track:
            # max_average: int
                # starts at 0
            # l: int
            # r: int
            # sum: int
                # starts at 0
        # Pseudocode:
            # if length of nums == 1, return the first item in the array
            # initialize max_average variable to store the max average at negative inf (max_average)
            # initialize a variable to keep a current sum up to r
            # initialize a left pointer at 0 (l)
            # iterate on nums array (r = index, n = nums[r])
                # sum += n
                # if r >= k - 1:
                    # compute the average:
                        # sum / k
                    # set the new max_average
                        # max_average = max(max_average, average)
                    # sum -= nums[l]
                    # increment l += 1
            # return max_average

        # TC: O(n) / SC: O(1)
        if len(nums) == 1:
            return nums[0]

        max_average, sum_val = float('-inf'), 0
        l = 0
        for r, n in enumerate(nums):
            sum_val += n
            if r >= k - 1:
                average = round(sum_val / k, 5)
                max_average = max(max_average, average)
                sum_val -= nums[l]
                l += 1

        return max_average

        # Alternative way to solve using substring:
        # TC: O(n) / SC: O(k)
        sum_val = sum(nums[:k])
        max_average = round(sum_val / k, 5)

        for r in range(k, len(nums)):
            sum_val += nums[r] - nums[r - k]
            max_average = max(max_average, sum_val / k)

        return max_average




solution = Solution()
start_time = time.time()
print(solution.findMaxAverage([1,3,1,2,0,5], 3))
print("--- %s seconds ---" % (time.time() - start_time))
