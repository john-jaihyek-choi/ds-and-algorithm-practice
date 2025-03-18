from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # objective:
        # given array of positive integers and an integer k, return the kth positive integer that is missing from the array
        # keywords:
        # arr
        # list of positive integers
        # not including 0
        # sorted in strictly increasing order
        # k
        # integer
        # return kth positive integer missing from array
        # observation:
        # arr can't have 0
        # arr is a range of positive integer starting from 1
        # brainstorm:
        # initial thought solution:
        # TC: O(n + m) where m has 1 <= m <= 1000 so O(n) / SC: O(n)
        # get max of the arr (TC O(n))
        # intialize an array with size of max + 1 with default value of 0 (num_pos) (TC O(m) / SC O(m))
        # iterate on arr: (n = arr[i]) (TC O(n))
        # set num_pos[n] += 1
        # iterate range(1, max + 1): (TC O(m))
        # if k == 0:
        # return i
        # if num_pos[i] == 0:
        # k -= 1

        # TC: O(n + m) where m has 1 <= m <= 1000, so O(n) / SC: O(n)
        mx = max(arr) + k
        num_pos = [0] * (mx + 1)
        for n in arr:
            num_pos[n] += 1

        for n in range(1, mx + 1):
            if not num_pos[n]:
                k -= 1
            if k == 0:
                return n

        # return None

        # less code / more efficient
        # TC: O(n) / SC: O(1)
        for n in arr:
            if n <= k:
                k += 1
            elif n > k:
                break
        return k

        # Binary Search solution:
        # note:
        # using index, it's possible to find out how many missing elements there are in array between range i and j
        # ex) [2, 3, 4, 7, 11]
        # at index 2 (value 4)
        # index = 2
        # array[index] = 4
        # total missing integers between array[0:2] = array[index] - index - 1
        # missing integers = 4 - 2 - 1 = 1
        # since the array comes pre-sorted:
        # I can find out whether I have kth missing integer on the left or the right side of the given index
        # general steps:
        # intialize left and right boundary
        # l, r = 0, len(arr) - 1
        # use binary search while l and r meets:
        # while l <= r:
        # find mid point:
        # m = (r + l) // 2
        # find left missing elements
        # arr[m] - m - 1
        # if arr[m] - m - 1 < k:
        # kth missing element is to the right of the middle point in the current array
        # l = m + 1
        # else (left missin elements >= k:
        # kth missing element is to the left of the middle point in the current array
        # r = m - 1
        # return l + k
        # how checking for missing_element < k guarantees to find the first position where at least k missing numbers exist
        # when binary search is complete, l represents the number of elements in arr before the k-th missing number
        # since l is the number of non-missing elements before k, l + k would represent the k-th missing element

        # TC: O(log n) / SC: O(1)
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (r + l) // 2
            missing_elements = arr[m] - m - 1
            if missing_elements < k:
                l = m + 1
            else:
                r = m - 1
        return l + k


solution = Solution()
start_time = time.time()
print(solution.findKthPositive([2, 3, 4, 7, 11]))
print("--- %s seconds ---" % (time.time() - start_time))
