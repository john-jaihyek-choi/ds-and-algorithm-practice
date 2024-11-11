from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Main considerations:
    # goal:
        # to return the next greatest letter in an array that's lexicographically greater than the target
            # if such letter doesn't exist, return the first letter in the input array
    # 1. check if the target is within the boundary of the input array
        # if not, return the first letter in the array
    # 2. do a binary search on the array
        # if letters[m] <= target:
            # check right half (eliminate left half from search)
        # else:
            # check left half (eliminate right half from search)
    # When the search is complete, the value at l should contain the next greater letter in the array


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1

        if target < letters[l] or target >= letters[r]:
            return letters[l]

        while l <= r:
            m = (l + r) // 2

            if target >= letters[m]:
                l = m + 1
            else:
                r = m - 1

        return letters[l]

solution = Solution()
start_time = time.time()
print(solution.nextGreatestLetter(["c","f","j"], "c"))
print("--- %s seconds ---" % (time.time() - start_time))