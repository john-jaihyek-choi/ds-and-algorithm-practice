import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 1679:
class Solution3:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Note:
            # input:
                # nums: List[int]
                # k: int
            # output:
                # output: int
            # goal:
                # given list of int, nums, and an integer, k, return the count of sum pairs that can be removed where the sum of the two pairs == k
        # Potential edge-cases:
            # empty array:
                # contrainst guarantees atleast 1 item in nums
            # len(nums) < 2:
                # return 0
            # Can use the same element twice?
                # Will assume that it cannot
        # Idea:
            # brute-force:
                # 2 nested loops (i and j as indicies)
                    # i starts from 0
                    # j = i + 1
            # Two-pointer approach:
                # Assumes use of sort is allowed
                # sort the nums array
                # use l and r to traverse the element in nums
                    # if nums[l] + nums[r] == k:
                        # increment counter
                        # increment l
                        # decrement r
                    # elif nums[l] + nums[r] > k:
                        # decrement r
                    # else: (nums[l] + nums[r] < k)
                        # increment l
            # Two-pointer approach:
                # Assumes use of sort is NOT allowed
                # num_count hash map to store the count of each unique num
                # iterate on nums
                    # compute the complement
                    # if complement in num_count and num_count[i] > 0 and num_count[complement] > 0:
                        # output += 1
                        # num_count[i] -= 1
                        # num_count[complement] -= 1

        # Brute-force (TC: O(n^2) / SC: O(n)):
        output = 0
        indicies_used = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == k and i not in indicies_used and j not in indicies_used:
                    output += 1
                    indicies_used.add(i)
                    indicies_used.add(j)
        
        return output
        
        # Pseudocode:
            # nums.sort()
            # output = 0
            # l, r = 0, len(nums) - 1
            # while l < r:
                # sum = nums[l] + nums[r]
                # if sum == k:
                    # output += 1
                    # l += 1
                    # r -= 1
                # elif sum > k:
                    # r -= 1
                # else:
                    # l += 1
            # return output
        
        # TC: O(n log n) including sort, O(n) excluding sort / SC: O(1)
        nums.sort()
        output = 0
        l, r = 0, len(nums) - 1
        while l < r:
            k_sum = nums[l] + nums[r]
            if k_sum == k:
                output += 1
                l += 1
                r -= 1
            elif k_sum > k:
                r -= 1
            else:
                l += 1
        return output

        # TC: O(n) / SC: O(n)
        count_map = {}
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1

        output = 0
        for n in count_map:
            complement = k - n
            
            if complement in count_map:
                if n == complement:
                    output += count_map[n] // 2
                else:
                    output += min(count_map[n], count_map[complement])
                    count_map[n] = 0
                    count_map[complement] = 0

        return output

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