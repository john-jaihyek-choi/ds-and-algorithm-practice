import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 1207:
class Solution2:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Note:
            # input:
                # arr: List[int]
            # output:
                # output: bool
            # goal:
                # given an array of integers, arr, return boolean
                    # True, if the number of occurances of each number in the array is UNIQUE
                    # False, if the number of occurances of each number in the array is NOT UNIQUE
        # Edgecase:
            # empty arr
                # 1 <= arr.length <= 1000
            # all same numbers
            # non digit char in arr
            # negative number in the arr
                # treat the negative as a unique number
                    # ex) 3 and -3 are two unique numbers
        # Idea:
            # count hashmap and occurances set (TC: O(n) / SC: O(n)):
                # iterate on the arr
                    # update the count of unique numbers to a hash map
                # iterate on the count hash map's value
                    # check if occurance in the iteration is an existing occurance
                        # if in occruance already, return False
                    # add the current occurance to occurance set
        
        # count hashmap and occurances set
        # Pseudocode:
            # initialize a count hash map
            # initialize a occurances set
            # iterate on arr and store unique count and its number in count hashmap
            # iterate on hash map's values
                # if occruance in count hash
                    # return False
                # add current occurance to occurance set
        
        # TC: O(n) / SC: O(n)
        count, occurances = {}, set()

        for n in arr:
            count[n] = count.get(n, 0) + 1

        for occurance in count.values():
            if occurance in occurances:
                return False
            occurances.add(occurance)
        
        return True

        # Opportunity for optimzation:
            # Do I need both hashmap and set?
                # might be able to eliminate hashmap for count?
                    # what about using array indexing?
                        # len(arr) is the max possible occurance of numbers
                    # The performance would still be same
            # Do I need to get the count ahead of time?
                # Yes, I wouldn't be able to get number of occurances until I iterate and get the count ahead of time
            # Given the above assessment, there's only an opportunity for time complexity
                # How can I make less operation?
                    # Use counter for count?
                        # might be more quick and efficient

        # Slightly optimal
        count, occurances = Counter(arr), set()

        for occurance in count.values():
            if occurance in occurances:
                return False
            occurances.add(occurance)
        
        return True

        # More concise and potentially readable solution
        count = Counter(arr)
        occurances = set(count.values())

        return len(count) == len(occurances)

class Solution1:
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


solution = Solution2()
start_time = time.time()
print(solution.uniqueOccurrences([1,2,2,1,1,3]))
print("--- %s seconds ---" % (time.time() - start_time))