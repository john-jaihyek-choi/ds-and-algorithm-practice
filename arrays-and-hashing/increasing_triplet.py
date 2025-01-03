import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 334:

# 1/3/2025 recap
class Solution3:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # input:
            # nums: List[int]
        # output:
            # output: bool
        # goal:
            # given an list of integers, nums, return true of nums have valid increasing triplet subsequence false otherwise
        # note:
            # increasing triplet subsequence:
                # indicies (i) must be in strictly increasing order
                # values (nums[i]) must be in strinctly increasing order
        # ideas:
            # brute-force (TC: O(n^3) / SC: O(1)):
                # use triple nested loop and compare all possibilities
            # optimized approach:
                # keep track of m1 and m2 min values
                # iterate on nums:
                    # condition:
                        # if nums[i] < m1:
                            # m1 = nums[i]
                        # elif nums[i] < m2:
                            # m2 = nums[i]
                        # else:
                            # return True
                # return False
        
        # brute-force:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False

        # optimal approach:
        m1 = m2 = float('inf')
        for i in range(len(nums)):
            if nums[i] <= m1:
                m1 = nums[i]
            elif nums[i] <= m2:
                m2 = nums[i]
            else:
                return True
        
        return False


class Solution2:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Note:
            # input:
                # nums: List[int]
            # output:
                # output: bool
            # goal:
                # given a list of integers, nums, return boolean true if nums contain triple of indicies such that i < j < k
        # Potential cases:
            # [1, 2, 3, 4, 5]
                # True
            # [5, 4, 3, 2, 1]
                # False
            # [2, 1, 5, 0, 4, 6]
                # n: 0 < 4 < 6
                # i: 3 < 4 < 5
        # Edge-case:
            # [5, 2, 2, 1, 6, 0, 8]
                # True
                # because:
                    # n: 1 < 6 < 8
                    # i: 3 < 4 < 6
        # Takeaway:
            # triplets don't necessarily have to be consecutive triplets both in terms of index or the value
        # Approach:
            # Brute-force (TC: O(n^3) / SC: O(1)):
                # 3 nested loops with indicies i, j, and k
                    # where i starts from 0
                    # where j = i + 1
                    # where k = j + 1
                    # all three indicies iterate til the end ofthe nums array
                # In each iteration, check if nums[i] < nums[j] < nums[k]
            # 1 pass if condition blocks (TC: O(n) / SC: O(1)):
                # min1
                # min2
                # else
                # min1 starts at inf
                # if nums[i] < min1:
                    # min1 = nums[i]
                # elif nums[i] < min2:
                    # min2 = nums[i]
                # else:
                    # return True
                # return False
            # track left min and track right max (TC: O(n) / SC: O(n)):
                # initialize left_min []
                # iterate on nums from 0
                    # append min n in nums up to ith index
                # initialized right_max []
                # iterate on nums from len(nums) - 1 to 0
                    # append max num in nums upto ith index
                # iterate on nums last time
                    # if left_min[i] < nums[i] < right_max[i]:
                        # return True
                # return False

        # Brute-force:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        
        return False

        # 1 pass if condition blocks:
            # Pseudcode:
                # min1 = min2 = float('inf')
                # for i in range(len(nums))
                    # if nums[i] <= min1:
                        # min1 = nums[i]
                    # elif nums[i] <= min2:
                        # min2 = nums[i]
                    # else:
                        # return True
                # return False
        
        min1 = min2 = float('inf')
        for i in range(len(nums)):
            if nums[i] <= min1:
                min1 = nums[i]
            elif nums[i] <= min2:
                min2 = nums[i]
            else:
                return True
        
        return False
        
        # track left min and track right max (TC: O(n) / SC: O(n)):
        left_mins = []
        l_min = float('inf')
        for i in range(len(nums)):
            prev = nums[i - 1] if i > 0 else float('inf')
            l_min = min(prev, l_min)

            left_mins.append(l_min)

        r_max = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            prev = nums[i + 1] if i < len(nums) - 1 else float('-inf')
            r_max = max(prev, r_max)

            if left_mins[i] < nums[i] < r_max:
                return True

        return False

class Solution1:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # input:
            # nums: List[int]
        # goal: return boolean True if indicies i < j < k and nums[i] < nums[j] < nums[k].
        # Brainstorm:
            # Monotonic increasing queue
                # create a stack that holds value in monotonically increasing
                # store each value in stack in strictly increasing order
                    # while nums[i] > than stack[-1], pop the stack
                        # when length of the stack >= 3, the nums array has increasing triplet subsequence
        # Brainstorm:
            # Keeping 2 min value approach:
                # have min1 and min2
                # as iterating:
                    # if nums[i] <= min1:
                        # set nums[i] to min1
                    # if nums[i] <= min2:
                        # set nums[i] to min2
                    # else:
                        # return True
            # return False
        
        min1 = min2 = float('inf')

        for n in nums:
            if n <= min1:
                min1 = n
            elif n <= min2:
                min2 = n
            else:
                return True
        
        return False
                

solution = Solution()
start_time = time.time()
print(solution.increasingTriplet([20,100,10,12,5,13]))
print("--- %s seconds ---" % (time.time() - start_time))