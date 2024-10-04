from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time
import math

class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if not total:
            return -1

        if B < A:
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            m1 = (r + l) // 2
            m2 = half - m1 - 2

            A_lp_last = A[m1] if m1 >= 0 else float('-inf')
            A_rp_first = A[m1 + 1] if m1 + 1 < len(A) else float('inf')  
            B_lp_last = B[m2] if m2 >= 0 else float('-inf')
            B_rp_first = B[m2 + 1] if m2 + 1 < len(B) else float('inf')

            if A_lp_last <= B_rp_first and B_lp_last <= A_rp_first:
                if total % 2:
                    return min(A_rp_first, B_rp_first)
                else:
                    return (max(A_lp_last, B_lp_last) + min(A_rp_first, B_rp_first)) / 2
            elif A_lp_last > B_rp_first:
                r = m1 - 1
            else:
                l = m1 + 1

# Note:
    # each array is sorted in an ascending order
    # median:
        # m + n is odd:
            # middle item
        # m + n is even:
            # middle 2 items / 2
    # solution must be be O(log(m + n))
    # Information available to use:
        # m: length of nums1
        # n: length of nums2

# Brainstorm:
    # partioning method:
        # mimicing the idea of combined sorted array by forming left partition to each arrays which takes half the number of elements of the total list (m + n)
        # Visualization:
            # Given:
                # nums1 = [1, 2], nums2 [3]
                # total = 3 
                # half = 3 / 2 = 1.5 = 1
            # Locating left partition:
                #   m1  <- partition point for nums1 (mid value of current l and r in nums1)
                # [ 1,  2 ]
                #  m2 <- partition point for nums2 (half - (m1 + 1) <- +1 because m1 is 0-indexed))
                # -inf  [ 3 ]  +inf
                #   ^- -inf when out of bounds to guarantee lowest value when comparing
                # Check1:
                    #  is num1[m1] <= num2[m2 + 1] = True
                # Check2:
                    #  is num2[m2] <= nums1[m1 + 1] = True
                # (If check1 and check2 doesn't pass):
                    # shift the l of the nums1 array to m1 + 1 and recalculate the new m1 point
                        # l = m + 1
                        # new left partition for nums1 = m1 - nums1[0]
            # Computing median:
                # stored variables available:
                    # m1 left partition point for nums1
                    # m2 left partition point for nums2
                # if m + n % 2 == 0 (even):
                    # (min(nums1[m1], nums2[m2]) + max(nums1[m1 + 1], nums2[m2 + 1])) / 2
                # else (odd):
                    # nums1[m1+1]

# Pseudocode:
    # initialize a variable to store the total length of the nums1 and nums2 (total)
    # initialize a starting half point of the total (half)
    # store nums1 and nums2 for length comparison
        # A and B
    # if B < A:
        # A is the new B and vice versa
    # initialize a left and the right pointer (l, r)
        # l starting from 0
        # r starting from the length of the A array
    # while True:
        # set the mid point (m1) to (r + l) // 2
        # compute m2 to half - (m1 + 1)

        # n1_lp_last = float('-inf') if m1 < 0 else nums1[m1]
        # n1_rp_start = float('inf') if m1 + 1 >= len(nums1) else nums1[m1 + 1]
        # n2_lp_last = float('-inf') if m2 < 0 else nums2[m2]
        # n2_rp_start = float('inf') if m2 + 1 >= len(nums2) else nums2[m2 + 1] 

        # if n1_lp_last <= n2_rp_start and n2_lp_last <= n1_rp_start:
            # if true,
                # if m + n % 2 == 0:
                    # return max(nums1[m1], nums2[m2]) + min(nums1[m1 + 1], nums2[m2 + 1] ) / 2
                # else:
                    # return nums2[m2 + 1] if m1 + 1 >= len(nums1) else nums1[m1 + 1]
            # elif n1_lp_last > n2_rp_start:
                # set r = m1 - 1
            # else:
                # set l = m1 + 1

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B  = nums1, nums2
        
        if B < A:
            A, B = B, A

        l, r = 0, len(A) - 1
        while l <= r:
            m1 = (l + r) // 2
            m2 = half - m1 - 2

            n1_lp_last = A[m1] if m1 >= 0 else float('-inf')
            n1_rp_start = A[m1 + 1] if m1 + 1 < len(A) else float('inf')
            n2_lp_last = B[m2] if m2 >= 0 else float('-inf') 
            n2_rp_start = B[m2 + 1] if m2 + 1 < len(B) else float('inf')

            if n1_lp_last <= n2_rp_start  and n2_lp_last <= n1_rp_start:
                if total % 2:
                    return min(n1_rp_start, n2_rp_start)
                return (max(n1_lp_last, n2_lp_last) + min(n1_rp_start, n2_rp_start)) / 2
            elif n1_lp_last > n2_rp_start:
                r = m1 - 1
            else:
                l = m1 + 1

        return float(-1)

    
solution = Solution1()
start_time = time.time()
print(solution.findMedianSortedArrays([1,2], [3]))
print("--- %s seconds ---" % (time.time() - start_time))