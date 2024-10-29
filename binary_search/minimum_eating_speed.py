from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time
import math

# Retried 10/28/2024: Leetcode 875
class Solution3:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # input:
            # piles: List[int]
                # piles[i] = number of banas in given pile (index)
            # h: int
                # hours until the guard comes back to take the food away
        # goal:
            # return the minimum banana-per-hour eating rate needed to finish all the bananas in the pile within h hours
        # Brainstorm:
            # Bruteforce:
                # Check every possibilities from 1 to n where n = max(piles)
                # O(n^2) time solution due to checking possibility
            # Area of optimization:
                # max(piles) is available in O(n) time operation, so we can't get much better
                # However, I can optimize the search part of the logic by binary search approach
                    # max(piles) represents the maximum number of bananas koko could finish in an hour to eat at a least amount of h
                        # when koko eats at k = max(piles), then the amount it takes for koko to fininsh will be n where n = len(piles)
            # Optimal approach (Binary Search):
                # iterate as much as max(piles) from 1 to max(piles)
                    # in each iteration, use binary search to find the minimum k where k = minimum banana to finish bananas in piles array
                        # update k to min_bananas as long as it's less than or equal to h
                    # if m banana eating rate to finish the entire pile is > h, search left half of the max(piles) range
                    # if m banana eating rate to finish the entire pile is < h, search the right half of the max(piles) range
        # Variable:
            # l: int
                # left boundary of the max(piles) range
            # r: int
                # right boundary of the max(piles) range
            # k: int
                # number of bananas to compute the minimum integer k
            # min_bananas: int
                # contains the min k banana eating rate value
        # Psuedocode:
            # initialize min_bananas at max(piles)
            # initialize a left and right boundary
                # l = 1
                # r = min_bananas
            # while l <= r:
                # find the mid point of the boundary:
                    # k = (l + r) // 2
                # keep track of the time to finish the entire pile
                    # time_to_finish = 0
                # iterate on piles array (bananas = piles[i]):
                    # compute the total hours it takes to finish piles eating at k rate
                        # time_to_finish += math.ceil(bananas / m)
                # if time_to_finish <= h:
                    # update min_bananas to min(min_bananas, time_to_finish)
                    # r = k - 1
                # if time_to_finish > h:
                    # l = k + 1
            # return the min_bananas

        # TC: O(n * log m) / SC: O(1)
        min_bananas = max(piles) # O(n)
        l, r = 1, min_bananas
        while l <= r: # O(log m) where m = maximum value in the piles array
            k = (l + r) // 2
            time_to_finish = 0
            for bananas in piles: # O(n)
                time_to_finish += math.ceil(bananas / k)
            
            if time_to_finish <= h:
                min_bananas = min(min_bananas, k)
                r = k - 1
            else:
                l = k + 1
        
        return min_bananas


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