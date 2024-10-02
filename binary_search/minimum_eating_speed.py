from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time
import math

# Note:
    # 1. piles.length <= h
    # 2. k = the number of banana to eat per hr
    # 3. max(piles): represents the maximum rate of banana per hr
    # Goal:
        # return the MINIMUM number of banana to eat per hour in a given time h

# Pseudocode:
    # initialize the left and the right pointer
        # l starting from 1
        # r starting from max(piles)
    # initialize the min_k = r
    # while l <= r
        # compute the mid point, (since 1-indexed, mid == k):
            # k = r + l // 2
            # compute the hrs needed to finish the pile (hrs_to_finish)
                # iterate the piles array from 0 to the length of the piles:
                    # add up the sum of the ceiling value of the piles[i] / k 
            # if hrs_to_finish > than h
                # set l to k + 1
            # else:
                # set min_k to k
                # set r to k - 1
    # return the min_k

# TC: O(log n * p) SC: O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # O(n)
        min_k = r # O(1)

        while l <= r: # O(log n) where n is the max value in piles
            k = (r + l) // 2 # O(1)
            
            hrs_to_finish = 0
            for pile in piles: # O(p) where p is length of piles
                hrs_to_finish += math.ceil(pile / k) # O(1)

            if hrs_to_finish > h: # O(1)
                l = k + 1 # O(1)
            else:
                min_k = k # O(1)
                r = k - 1 # O(1)
                

        return min_k # O(1)

solution = Solution()
start_time = time.time()
print(solution.minEatingSpeed([312884470], 968709470))
print("--- %s seconds ---" % (time.time() - start_time))