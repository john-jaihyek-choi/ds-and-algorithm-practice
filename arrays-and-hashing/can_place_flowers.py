import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 605:
class Solution3:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Note:
            # input:
                # flowerbed: List[int]
                # n: int
            # output:
                # output: bool
            # goal:
                # given list flowerbed with integer n, return the boolean true/false whether n number of flowers can be planted adhering to the no-adjacent-flowers-rule
            # no-adjacent-flowers-rule:
                # flower can only be planted if the adjacent flowerbed is empty (0's)
        # General approach:
            # iterate the flowerbed
                # check if adjacent sides are both empty (0s)
                    # ** treat list index out of range with if else
                    # If plantable:
                        # update the flowerbed[i] with 1
                            # assumes input update is fine
                        # then decrement n
                            # assumes input update is fine
        
        # Pseudocode:
        # for i in flowerbed:
            # left_bed = flowerbed[i - 1] if i - 1 >= 0 else 0
            # right_bed = flowerbed[i + 1] if i + 1 < len(flowerbed) else 0
            # if left_bed == right_bed == 0:
                # flower_bed[i] = 1
                # n -= 1
            # if n <= 0:
                # return True
        
        # return False

        # TC: O(n) / SC: O(1)
        for i in range(len(flowerbed)):
            left_bed = flowerbed[i - 1] if i - 1 >= 0 else 0
            right_bed = flowerbed[i + 1] if i + 1 < len(flowerbed) else 0

            if flowerbed[i] == left_bed == right_bed == 0:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        
        return False


class Solution2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Solution without direct modification of flowerbed

        # TC O(n) / SC O(1) without input modification
        if len(flowerbed) < 3 and max(flowerbed) == 1:
            return n < max(flowerbed)
        
        remaining_flower = n
        i = 0
        while i < len(flowerbed):
            prev = flowerbed[i - 1] if i - 1 >= 0 else 0 
            cur = flowerbed[i]
            nxt = flowerbed[i + 1] if i + 1 < len(flowerbed) else 0

            if cur == 0 and prev == cur == nxt:
                remaining_flower -= 1
                i += 1
                if remaining_flower == 0:
                    break
            i += 1

        return remaining_flower <= 0

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # input:
            # flowerbed: List[int]
                # rule:
                    # flowerbed[i] can only be planted if adjacent plots are empty (0)
            # n: int
                # total number of flowers to plant  
            # ** no two adjacent flowers in flowerbed
                # means the input isn't provided as a non-valid input
        # Obvious solution:
            # Iterating with three pointers
                # track 3 pointers:
                    # prev
                    # cur
                    # next
                # iterate while next is available
                # edge case to handle:
                    # flowebed with len < 3
                    # if len(flowerbed) < 3
                        # it means there's only 2 valid plots
                            # if 1 of the plot is empty, then we can't plant
                            # if both of the plot is empty, we can plant 1
                        # so, I can get max of flowerbed
                            # if flowerbed max == 1
                                # can't plant
                            # if flowerbed max == 0
                                # can plant 1
        # Variables to track:
            # prev: int
            # cur: int
            # next: int
            # remaining_flowers: int
        # Pseudocode:
            # if len(flowerbed) < 3:
                # if max(flowerbed) == 1:
                    # return n < max(flowerbed)
            # initialize remaining_flower to n (remaining_flower)
            # initialize 3 pointers (prev, cur, next):
                # prev = 0
                # cur = 1
                # next = 2
            # while next < len(flowerbed):
                # if cur == 0 and prev == cur == next:
                    # decrement remaining_flowers by 1
                # increment prev, cur, and next pointers
            # return remaining_flower == 0

        # TC: O(n) / SC: O(1) - if direct modification to flowerbed is allowed
        # TC: O(n) / SC: O(n) - if direct modification not allowed
        if len(flowerbed) < 3 and max(flowerbed) == 1:
            return n < max(flowerbed)
        
        remaining_flower = n
        for i, plot in enumerate(flowerbed):
            prev = flowerbed[i - 1] if i - 1 >= 0 else 0 
            cur = plot
            nxt = flowerbed[i + 1] if i + 1 < len(flowerbed) else 0

            if cur == 0 and prev == cur == nxt:
                flowerbed[i] = 1
                remaining_flower -= 1
                if remaining_flower == 0:
                    break

        return remaining_flower <= 0

solution = Solution()
start_time = time.time()
print(solution.canPlaceFlowers([1,0,0,0,0,1], 2))
print("--- %s seconds ---" % (time.time() - start_time))