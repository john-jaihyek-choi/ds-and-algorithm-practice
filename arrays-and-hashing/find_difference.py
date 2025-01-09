import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 2215:
# 1/8/2025 retried
class Solution4:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # input:
            # nums1: List[int]
            # nums2: List[int]
        # output:
            # otuput: List[List[int]]
        # goal: 
            # given a 2 lists of integers, nums1 and nums2, return a list of list of integers with size 2 where
                # output[0] == list of distinct numbers in nums1 that's not present in nums2
                # output[1] == list of distinct numbers in nums2 that's not present in nums1
        # ideas:
            # intuition: 2 sets for nums1 and nums2
                # initialize 2 sets - each for nums1 and nums2
                # initialize output array with 2 empty arrays
                # iterate nums1 (n = nums[i])
                    # if n not in nums2:
                        # output[0].append(n)
                # iterate nums2 (n = nums[i])
                    # if n not in nums1:
                        # output[1].append(n)
                # return output
            # pythonic solution: 2 sets then set difference
                # initialize 2 sets - each for nums1 and nums2
                # return [for n in (set1 - set2)], [for n in (set2 - set1)]]
        
        # TC: O(n + m) / SC: O(n + m)
        set1, set2 = set(nums1), set(nums2)
        return [n for n in (set1 - set2)], [n for n in (set2 - set1)]

        # better readability:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]


class Solution3:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Note:
            # input:
                # nums1: List[int]
                # nums2: List[int]
            # output:
                # answer: List[List[int]]
            # goal:
                # given 2 lists of integers, nums1 and nums2, return answer with size 2 where:
                    # answer[0] contains list of all distinct integer in nums1
                    # answer[1] contains list of all distinct integer in nums2
        # Edgecase:
            # nums1 and nums2 empty:
                # 1 <= nums1.length, nums2.length <= 1000
            # nums1 or nums2 empty:
                # 1 <= nums1.length, nums2.length <= 1000
        # Ideas:
            # initial thought:
                # 2-pass (n + m) and 2 sets solution:
                    # initialize n1_set, n2_set = {}, {}
                    # iterate on nums1 and add nums1[i] to set
                    # iterate on nums2 and add nums2[i] to set
                    # iterate on nums1:
                        # if nums1[i] not in n2_set:
                            # answer[0].append(nums1[i])
                    # iterate on nums2:
                        # if nums2[i] not in n1_set:
                            # answer[1].append(nums2[i])
            # bruteforce:
                # 2 nested loops:
                    # nest loops and check each possibility
                        # and also need to check for duplicates within output


        # Pseudocoe:
            # n1_set, n2_set = set([n for n in nums1]), {[n for n in nums2]}
            # for n in n1_set:
                # if n not in n2_set:
                    # answer[0].append(n)
            # for n in n2_set:
                # if n not in n1_set:
                    # answer[1].append(n)
        
        # TC: O(n + m) / SC: O(n + m)
        n1_set, n2_set = set(nums1), set(nums2)
        answer = [[],[]]
        for n in n1_set:
            if n not in n2_set:
                answer[0].append(n)
        for n in n2_set:
            if n not in n1_set:
                answer[1].append(n)

        return answer
            
        # Python native set comparison:
        n1_set, n2_set = set(nums1), set(nums2)
        n1_unique = list(n1_set - n2_set)
        n2_unique = list(n2_set - n1_set)
        
        return [n1_unique, n2_unique]

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