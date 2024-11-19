import math
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 1431:

class Solution2:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Note:
            # input:
                # candies: List[int]
                # extraCandies: int
            # output:
                # output: List[bool]
            # goal:
                # given candies list and an integer extraCandies, return a List of booleans that indicates the i'th kid's possibility of having the greatest number of candies
        # general approach:
            # compute max candies a kid in the list has
                # any number of candies greater than this num essentially has potential to have greatest num of candies
            # iterate on candies
                # check if sum of extraCandies and candies[i] exceeds the max
                    # if true, true for ith kid
                    # else, false
        # Psuedocode:
            # max_candies = max(candies)
            # output = []
            # for n in candies:
                # if extraCandies + candies[i] >= max_candies:
                    # output.append(True)
                    # continue
                # output.append(False)
            # return output

        # TC: O(n) / SC: O(n)
        max_candies = max(candies) # O(n)
        output = []
        for n in candies: # O(n)
            if extraCandies + n >= max_candies: # O(1)
                output.append(True)
                continue
            output.append(False) 
        return output # O(1)
        

class Solution1:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # input:
            # candies: List[int]
                # candies[i] represents the number of candies a kid at i has currently
            # extraCandies: int
                # number candies I have that I can give to a single kid at candies[i]
        # goal: return an boolean array "result" of length n
            # result[i] = true if candies[i] + extraCandies is the max among the candies list
            # result[i] = false if candies[i] + extraCandies is NOT the max among the candies list
        # Brainstorm:
            # need to find out the current max (without extra candies) of the candies
            # iterate the candies list and compute the total amount candies a kid has after the extraCandies were given
                # if the total is bigger than OR EQUAL to the max, then true
                # if the total is less than to the max, then false
        # Variables to track:
            # result: List[bool]
            # max_b4_extra: int
        # Pseudocode:
            # initialize an empty array to store output (result)
            # initialize max_b4_extra and set it to the max value of the candies array (max_b4_extra)
            # iterate the candies (c = candies[i])
                # if c + extraCandies >= max_b4_extra:
                    # append True to output array
                # else:
                    # append False
            # return the output array

        # TC: O(n) / SC: O(n)
        result = []
        max_b4_extra = max(candies)

        for c in candies:
            if c + extraCandies >= max_b4_extra:
                result.append(True)
            else:
                result.append(False)

        return result


            
                

