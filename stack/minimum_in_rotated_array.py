from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time
import math

# Note:
    # 1. len(nums) = n
    # 2. nums[i] are all unique
    # 3. array is in a ascending order (but rotated by x times)

# TC: O(log n) / SC: O(1) Same logic, but with float('inf')
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 # O(1)
        min_val = float('inf') # O(1)

        while l <= r: # O(log n)
            mid = (r+l) // 2 # O(1)
            if nums[mid] > nums[r]: # O(1)
                l = mid + 1 # O(1)
            else:
                min_val = min(min_val, nums[mid]) # O(1)
                r = mid - 1 # O(1)
        
        return min_val # O(1)

# Solution 1:
    # Pseudocode:
        # initialize a left and right pointer:
            # l to start from 0
            # r to start from the length of the nums array - 1
        # initialize the min_val at value at nums[0]
        # while l less than or equal to r:
            # set mid pointer to (r + l) // 2
            # if nums[mid] is greater than nums[r]:
                #  set l to mid + 1
            # else:
                # set min_val minimum between itself and nums[mid]
                # then set r to mid - 1
        # return the min_val

# TC: O(log n) / SC: O(1)
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 # O(1)
        min_val = nums[0] # O(1)

        while l <= r: # O(log n)
            mid = (r+l) // 2 # O(1)
            if nums[mid] > nums[r]: # O(1)
                l = mid + 1 # O(1)
            else:
                min_val = min(min_val, nums[mid]) # O(1)
                r = mid - 1 # O(1)
        
        return min_val # O(1)
    
solution = Solution2()
start_time = time.time()
print(solution.findMin([3,4,5,6,1,2]))
print("--- %s seconds ---" % (time.time() - start_time))