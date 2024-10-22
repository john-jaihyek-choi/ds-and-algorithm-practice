import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 334:
class Solution:
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