import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 1207:
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # input:
            # arr: List[int]
        # goal: return a boolean:
            # True if:
                # arr[i]'s occurances are unique
            # False if:
                # arr[i]'s occurances aren't unique
        # Note:
            # what we care about is the occurances of each num in arr
            # using set to store the unique occurances of a number
                # can't use set, since we will need to iterate on arr and count each occurances 1 by 1
            # using hash map to store the number as key and occurance as val
        # Brainstorm:
            # start with an empty occurances map
            # iterate the arr and store the count of unique numbers
            # create an empty set to store the occurances
            # iterate on the values add value to occurances if it doesn't already exist
                # if it exists, return false
        # Variables:
            # occurances_map: dict(int)
            # occurances_set: set(int)
        # Pseudocode:
            # initialize an empty dictionary occurances_map
                # use defaultdict with int
            # initialize an empty dictionary occurances_set
            # iterate on the arr (i = index, n = arr[i])
                # increment occurances_map[n] by 1
            # iterate the occurances_map values (n = count)
                # if n in occurances_set:
                    # return false
                # add n to occurances_set
            # return true

        # TC: O(n) / SC: O(n)
        occurances_map, occurances_set = defaultdict(int), set()
        for i, n in enumerate(arr):
            occurances_map[n] += 1
        
        for n in occurances_map.values():
            if n in occurances_set:
                return False
            occurances_set.add(n)

        return True


solution = Solution()
start_time = time.time()
print(solution.uniqueOccurrences([1,2,2,1,1,3]))
print("--- %s seconds ---" % (time.time() - start_time))