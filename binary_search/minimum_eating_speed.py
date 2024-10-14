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

# Retry:
        # Note:
            # The max number of bananas in pile represents the max amount of k it takes to finish within h
            # piles[i] = pile of bananas that could be eaten in a given hour
            # 

        # get max value of the piles (pile_max)
        # initialize a l and r pointer:
            # l = 1, r = pile_max
        # initialize a min_k = float('inf')
        # iterate the piles array while l <= r
            # ex)
                #     k
                # [1, 2, 3, 4]
            # set middle point, k, equal to (l + r) // 2 (k)
            # initialize an hour_to_finish = 0
            # iterate the piles array from 0
                # ex)
                    # k = 2
                    # [1, 4, 3, 2]
                # compute the hour to finish = math.ceil(piles[i] / k) and add to itself
            # if hour_to_finish <= h:
                # set min_k equal to the minimum value of it itself or k
                # set r = k - 1
            # otherwise:
                # set l = k + 1
        # return min_k
class Solution2:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        pile_max = max(piles)
        l, r = 1, pile_max
        min_k = pile_max

        while l <= r:
            k = (l + r) // 2
            hours_to_finish = 0

            for pile in piles:
                hours_to_finish += math.ceil(pile / k)

            if hours_to_finish <= h:
                min_k = min(min_k, k)
                r = k - 1
            else:
                l = k + 1

        
        return min_k

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