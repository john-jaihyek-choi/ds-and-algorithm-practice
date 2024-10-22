import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 2215:
class Solution2:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Concise way using native set comparisons
        # TC: O(n + m - x), SC: O(n + m - x) where n = len(nums1), m = len(nums2), x = duplicates in nums1 and nums2
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]
    
class Solution1:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # input:
            # nums1: List[int]
            # nums2: List[int]
            # nums1 and nums2 can be of a different length
        # goal:
            # return output "answer" of size 2 where:
                # answer[0] contains list of integers in nums1 NOT IN nums2
                # answer[1] contains list of integers in nums2 NOT IN nums1
            # Note:
                # integer in the list may be returned in any order
        # Brainstorm:
            # Using sets to store the values in nums1 and nums2
            # iterate nums1 and nums2 separately and check the existence of the num at i
                # if doesn't exist, append to an output array
        # Variable:
            # output: List[ List[int] ]
                # length is fixed to 2
            # set1: set
            # set2: set
        # Pseudocode:
            # initialize set1 and set2 with nums1 and nums2
            # initialize output array with size 2 and with array as a default
            # iterate set1 (i = index, n = set1[i])
                # if n exists in set2:
                    # append n to output[0]
            # iterate set2 (i = index, n = set2[i])
                # if n exists in set1:
                    # append n to output[1]
            # return the output

        # TC: O(n + m - x), SC: O(n + m - x) where n = len(nums1), m = len(nums2), x = duplicates in nums1 and nums2
        set1, set2 = set(nums1), set(nums2)
        output = [[] for _ in range(2)]
        
        for i, n in enumerate(set1):
            if n not in set2:
                output[0].append(n)
        
        for i, n in enumerate(set2):
            if n not in set1:
                output[1].append(n)

        return output


solution = Solution1()
start_time = time.time()
print(solution.findDifference([1,0,0,0,0,1], 2))
print("--- %s seconds ---" % (time.time() - start_time))