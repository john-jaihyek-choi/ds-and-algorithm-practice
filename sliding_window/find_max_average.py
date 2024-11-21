from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 643:
class Solution2:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Note:
            # input:
                # nums: List[int]
                # k: int
            # output:
                # output: float
            # goal:
                # given a list of integer and integer, nums and k, return the maximum average value of a contiguous subarray whose length is equal to k
                    # error less than 10^-5 is accepted
        # Edgecase:
            # k > len(nums):
                # constraint is in place for 1 <= k <= n <= 100,000
            # k == 0
                # 1 <= k <= n <= 10^5
        # Idea:
            # Brute-force:
                # 2 nested loops (i and j)
                    # i starts at 0 and loops the entire nums arr
                    # j starts at i + 1 and loops to i + k 
                # compute average for the elements within the size of the window
                # return the max average
            # sliding-window:
                # 2 pointers, l and r
                # iterate the nums while r < len(nums)
                    # r moves each iteration
                    # compute sum of number at each iteration
                    # if r >= k-1:
                        # calculate max average of the sum
                        # increment l
                            # before incrementing, subtract nums[l] from sum

        
        # Brute-force:
        max_avg = float('-inf')
        for i in range(0, len(nums) - k + 1):
            avg = nums[i]
            for j in range(i+1, i + k):
                avg += nums[j]
            max_avg = max(max_avg, round(avg / k, 5))
        
        return max_avg

        # sliding-window:
        # l = 0
        # max_avg = float('-inf')
        # sum = 0
        # for r in range(len(nums)):
            # compute sum of number at each iteration
                # sum += nums[r]
            # if r >= k - 1:
                # max_avg = max(max_avg, round(sum / k, 5))
                # sum -= nums[l]
                # l += 1

        # TC: O(n) / SC: O(1)
        l = sum_val = 0
        max_avg = float('-inf')

        for r in range(len(nums)):
            sum_val += nums[r]

            if r >= k - 1:
                max_avg = max(max_avg, round(sum_val / k, 5))
                sum_val -= nums[l]
                l += 1
        
        return max_avg

        # Optimized cleaner code (TC: O(n) / SC: O(1)):
        sum_val = max_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            sum_val += nums[i] - nums[i - k]

            max_sum = max(max_sum, sum_val)

        return max_sum / k
    

class Solution1:
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
