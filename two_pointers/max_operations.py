import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 1679:
class Solution2:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # TC: O(n) / SC: O(n)
        # Assuming sorting is not allowed:
        # Use of hash map for storing nums number count
        # Variable to track:
            # count: dict
            # operations: int
        count = {}
        operations = 0

        # Count occurrences of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Find pairs
        for num in list(count.keys()):
            complement = k - num
            if complement in count:
                if num == complement:
                    # If both numbers are the same
                    operations += count[num] // 2
                else:
                    # Minimum pairs we can form
                    pairs = min(count[num], count[complement])
                    operations += pairs
                    # Remove counted pairs
                    count[num] = 0
                    count[complement] = 0

        return operations

class Solution1:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # input:
            # nums: List[int]
                # Not sorted
            # k: int
                # target sum of nums[i] and nums[j]
        # goal: return the maximum number of operations I can perform on the nums array
        # Question:
            # Is input array sorted?
                # if not, is sorting the input array allowed?
                    # in-place sort allowed?
        # Assuming Sorting of the nums in-place is allowed using the built-in sort method:
            # sort the nums array
            # use two pointers, l and r
                # if sum of nums[l] and nums[r] is equal to k, add as 1 operation
                # when sum is less than the target, move the l pointer
                # when sum is greater than the target, move the r pointer
            # Variable to track:
                # l: int
                    # start at 0
                # r: int
                    # start at len(nums) - 1
                # operations: int
                    # start at 0
        # Pseudocode:
            # sort the nums array in-place
            # initialize operations at 0 (operations)
            # initialize l and r pointers:
                # l = 0
                # r = len(nums) - 1
            # while l is less than r:
                # compute sum:
                    # nums[l] + nums[r]
                # if sum < k:
                    # l += 1
                # if sum > k:
                    # r -= 1
                # else:
                    # operations += 1
                    # l += 1
                    # r -= 1
            # return operations
        
        # TC: O(n) + O(n log(n)) / SC: O(1) - if mutating input array is not allowed, the SC will be O(n)
        nums.sort() # O(n lon(n))
        operations = 0 # O(1)
        l, r = 0, len(nums) - 1 # O(1)
        while l < r: # O(n)
            sum_val = nums[l] + nums[r] # O(1)

            if sum_val < k: # O(1)
                l += 1
            elif sum_val > k: # O(1)
                r -= 1
            else: # O(1)
                operations += 1
                l += 1
                r -= 1
            
        return operations # O(1)

solution = Solution2()
start_time = time.time()
print(solution.maxOperations([3,1,3,4,3], 6))
print("--- %s seconds ---" % (time.time() - start_time))