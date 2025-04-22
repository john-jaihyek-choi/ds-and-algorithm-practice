from collections import defaultdict, Counter
from typing import List, Dict, DefaultDict, Set
import time


# Leetcode #88
class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        Goal: given 2 arrays, nums1 and nums2, return a merged array sorted in nums1 instead of new array
        Note:
            - Can I use m or n in a meaninful way?
                - 
        Idea:
            1. merge the values, then sort (bruteforce):
                - put all elements in nums2 to the filler 0s in nums1
                - sort the nums1 array
            2. use read/write pointers iterate from the back (three pointers):
                - r1 (read pointer for nums1) starts m - 1
                - r2 (read pointer for nums2) starts n - 1
                - w (write pointer for nums1) starts m + n - 1
                - iterating from m + n - 1 to -1: (w = index)
                    - if r2 < 0:
                        - break
                    - if r1>= 0 and nums1[r1] > nums2[r2]:
                        - nums1[w] = nums1[r1]
                        - r1 -= 1
                    - else:
                        - nums1[w] = nums1[r1]
                        - r1 -= 1
        """

        # bruteforce:
        # TC: O(n log n) / SC: O(1)
        for i in range(m, m + n):
            nums1[i] = nums2[i - n]

        nums1.sort()

        # three-pointer from back of the array:
        # TC: O(m + n) / SC: O(1)
        r1, r2 = m - 1, n - 1
        for w in range(m + n - 1, -1, -1):
            if r2 < 0:
                break
            if r1 >= 0 and nums1[r1] > nums2[r2]:
                nums1[w] = nums1[r1]
                r1 -= 1
            else:
                nums1[w] = nums2[r2]
                r2 -= 1


start_time = time.time()
solution = Solution1()
print(solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print("--- %s seconds ---" % (time.time() - start_time))
