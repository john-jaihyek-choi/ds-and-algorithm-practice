from collections import defaultdict, Counter
from typing import List, Dict, DefaultDict, Set
import time


# Leetcode #2231
class Solution:
    def largestInteger(self, num: int) -> int:
        """
        objective:
            given positive integer num, return the largest possible value of num after ANY number of swaps
        Keyword:
            input == positive integer num
            swap:
                allows to swap any two digit of nums with same PARITY
                    parity == both odd digits or both even digits
        Brainstorm:
            ex) 12345
             l, r
            [0, 1] -> 1 vs 2 not parity
            [0, 2] -> 1 vs 3 is parity AND 3 > 1
                swap: 32145
            [0, 3] -> 3 vs 4 not parity
            [0, 4] -> 3 vs 5 is parity AND 5 > 3
                swap: 52143
        Intuition:
            # bruteforce solution: try every iteration and numbers
                # use 2 nested loops, then compare each possible pairs of numbers
                # outer loop (i = index, left = num[i]):
                    # inner loop (j = i + 1, right = num[j])
                        # if isParity(left, right) and right > left:
                            # right, left = left, right
        """

        # TC: O(n^2) / SC: O(n)
        # nums_arr = list(str(num)) # TC O(n) / SC O(n)
        # for l in range(len(nums_arr)): # O(n)
        #     for r in range(l + 1, len(nums_arr)): # O(n)
        #         if self.isParity(int(nums_arr[l]), int(nums_arr[r])) and nums_arr[r] > nums_arr[l]:
        #             nums_arr[l], nums_arr[r] = nums_arr[r], nums_arr[l]
        # return int("".join(nums_arr))

        """
        Optimal Solution: keep separate sorted lists for even and odd numbers
            store 2 unique arrays, in sorted order, for even and odd numbers:
                ex) num = 12345
                    odds = [1,3,5]
                    evens = [2,4]
            iterate on num (i = index, n = num[i])
                if n is even:
                    evens.append(n)
                elif n is odd:
                    odds.append(n)
            sort odds and evens arrays (in-place)
                O(n log n) timer / O(n) space
            # initialize output at 0
            iterate on num string (n = num_arr[i]):
                if n is even
                    output = output*10 + evens.pop()
                else: 
                    output = output*10 + odds.pop()
            return int("".join(num_arr))
        """

        evens, odds = [], []
        num_arr = list(int(n) for n in str(num))

        for i, n in enumerate(num_arr):
            if not int(n) % 2:  # even
                evens.append(n)
            else:  # odd
                odds.append(n)

        evens.sort(), odds.sort()

        output = 0
        for n in num_arr:
            if n % 2 == 0:
                output = output * 10 + evens.pop()
            else:
                output = output * 10 + odds.pop()

        return output

    def isParity(self, val1: int, val2: int) -> bool:
        if (not val1 % 2 and not val2 % 2) or (val1 % 2 and val2 % 2):
            return True
        else:
            return False


start_time = time.time()
solution = Solution()
print(solution.largestInteger(12345))
print("--- %s seconds ---" % (time.time() - start_time))
