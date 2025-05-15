from collections import defaultdict, Counter
from typing import List, Dict, DefaultDict, Set
import time


# Leetcode #88


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        Note:
            - nums1 and nums2 are both sorted
            - return nums1 which contains sorted and merged result
        Intuition:
            - Bruteforce:
                - TC: O(n log n) / SC: O(1)
                - iterate nums1 with a pointer on nums2
                    - if 0, switch nums[i] with nums[p]
                    - sort at the end
            - Two pointer iterate backwards:
                - initialize p1 and p2 at the end of nums1 and nums2
                - iterate nums1 from backwards
                    - if p1 < 0 or p2 < 0:
                        break out of loop
                    - if nums1[p1] <= nums2[p2]:
                        - set nums1[i] to nums2[p2]
                    - else:
                        - set nums1[i] to nums1[p1]

        """

        # TC: O(m + n) / SC: O(1)
        p1, p2 = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            if p2 < 0 or p1 < 0:
                break
            if nums1[p1] <= nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1

        while p2 >= 0:
            nums1[i] = nums2[p2]
            i, p2 = i - 1, p2 - 1

        return nums1

        # TC: O(n log n) / SC: O(1)
        p = 0
        for i in range(m, m + n):
            nums1[i], nums2[p] = nums2[p], nums1[i]
            p += 1
        nums1.sort()
        return nums1


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
