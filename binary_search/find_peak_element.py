from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time
    
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # input:
            # nums: List[int]
                # nums[-1] = nums[n] = -inf
                    # element is always considered to be strictly greater than the neighbor outside the array
                    # nums[i] != nums[i + 1] for all valid i
        # goal:
            # return the peak element, num[i], where nums[i - 1] <  nums[i] < nums[i + 1]
        # Brainstorm:
            # Bruteforce:
                # iterating the nums array and comparing the left and the right neighboring elements if it qualifies as a valid peak
            # Target time complexity of an algorithm, O(log n), signifies that the problem needs to be solved with binary search
            # Binary search:
                # Target: peak, nums[i] where nums[i - 1] <  nums[i] > nums[i + 1]
                    # Is it possible to find the neighboring elements of nums[i]?
                        # what if either of the neighboring element is out of boundary?
                            # based on the problem's constraint:
                                # nums[-1] = nums[n] = -inf
                # How do I know when to search left half and when to search right half?
                    # what hint can I get from the neighboring elements?
                        # Main constraints:
                            # 1. nums[-1] = nums[n] = -inf
                            # 2. nums[i] != nums[i + 1] for all valid i
                        # Due to the above constraints, it guarantees two things:
                            # 1. there are no flat slope in the graph
                            # 2. there will be at least 1 peak in the graph
                    # Conclusion:
                        # if nums[i] < nums[m + 1], there's an upward slope to the right:
                            # check the right half
                        # if nums[i] < nums[m - 1], there's an upward slope to the left:
                            # check the left half
        # Variable:
            # l: int
            # r: int
            # m: int
        # Pseudocode:
            # initialize a left and the right boundary
                # l = 0
                # r = len(nums) - 1
            # while l <= r:
                # find the mid point:
                    # m = (l + r) // 2
                # define cur, left neighbor, and right neighbor:
                    # cur = nums[m]
                    # left_neighbor = nums[m - 1] if m - 1 >= 0 else float('-inf')
                    # right_neighbor = nums[m + 1] if m + 1 < len(nums) else float('-inf')
                # if left_neighbor < cur < right_neighbor:
                    # return m
                # elif left_neighbor > cur:
                    # r = m - 1
                # else:
                    # l = m + 1

        # TC: O(log n) / SC: O(1)
        l, r = 0, len(nums) - 1 # O(1)
        while l <= r: # O(n)
            m = (l + r) // 2 # O(1)
            cur = nums[m] # O(1)
            left_neighbor = nums[m - 1] if m - 1 >= 0 else float('-inf') # O(1)
            right_neighbor = nums[m + 1] if m + 1 < len(nums) else float('-inf') # O(1)

            if left_neighbor < cur > right_neighbor: # O(1)
                return m
            elif left_neighbor > cur: # O(1)
                r = m - 1
            else: # O(1)
                l = m + 1



solution = Solution()
start_time = time.time()
print(solution.findPeakElement([3,4,3,2,1]))
print("--- %s seconds ---" % (time.time() - start_time))