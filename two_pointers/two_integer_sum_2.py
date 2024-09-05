from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

def twoSum(numbers: List[int], target: int) -> List[int]:
    # Note:
        # numbers are sorted in a non-decreasing order
        # function should return [ index1, index2 ]
            # index1 < index2
            # index1 cannot equal to index2 (forbidden use of same elements)
        # there will be exactly ONE VALID SOLUTION

    # Pseudocode:
        # initialize l and r pointer, l starting at 0 and r starting from the end of the numbers list
        # iterate the numbers array while l and r doesn't cross (l <= r)
            # if sum of numbers[l] and numbers[r] is greater than the target
                # decrement r by 1
            # if sum of numbers[l] and numbers[r] is less than the target
                # increment l by 1
            # if sum of numbers[l] and numbers[r] is equal to target AND numbers[l] < numbers[r]
                # return [numbers[l], numbers[r]]

    l, r = 0, len(numbers) - 1

    # Solution 1:
    # while l <= r:
    #     if numbers[l] + numbers[r] > target:
    #         r -= 1
    #     elif numbers[l] + numbers[r] < target:
    #         l += 1
    #     else:
    #         if numbers[l] < numbers[r]: # this is not necessary as there is exactly 1 valid solution
    #             return [l + 1, r + 1]
    #         l += 1 # this is not necessary as there is exactly 1 valid solution

    # Solution 2 (Cleaner version):
    while l < r:
        sum = numbers[l] + numbers[r]

        if sum > target:
            r -= 1
        elif sum < target:
            l += 1
        else:
            return [l + 1, r + 1]
    

start_time = time.time()
print(twoSum([1,4,4,4,5,6,], 8))
print("--- %s seconds ---" % (time.time() - start_time))