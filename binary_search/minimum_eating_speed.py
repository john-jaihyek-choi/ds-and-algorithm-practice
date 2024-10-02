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

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = r

        while l <= r:
            k = (r + l) // 2
            
            hrs_to_finish = 0
            for pile in piles:
                hrs_to_finish += math.ceil(pile / k)

            if hrs_to_finish > h:
                l = k + 1
            else:
                min_k = k
                r = k - 1
                

        return min_k

solution = Solution()
start_time = time.time()
print(solution.minEatingSpeed([312884470], 968709470))
print("--- %s seconds ---" % (time.time() - start_time))