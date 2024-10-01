from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Note:
    # matrix is sorted in NON-DECREASING ORDER
    # first integer of every row is greater than the last integer of the previous row
    # function returns true if target exists, false otherwise

# Solution 1:
    # Pseudocode:
        # initialize an outer_l and outer_r pointer
            # l is equal to 0
            # r is equal to len(matrix) - 1
        # while outer_l is less than or equal outer_r:
            # set outer_mid pointer to outer_l + outer_r divided (floor division) by 2
            # if target is within matrix[outer_mid][0] and matrix[outer_mid][-1]:
                # initialize inner_l and inner_r:
                    # inner_l = 0
                    # inner_r = length of the matrix[outer_mid] - 1
                # while inner_l <= inner_r:
                    # set inner_mid pointer to inner_l + outer_r divided (floor division) by 2
                    # if matrix[outer_mid][inner_mid] is greater than the target:
                        # inner_r = inner_mid - 1
                    # elif matrix[outer_mid][inner_mid] is less than the target:
                        # l = inner_mid + 1
                    # else:
                        # return true
                # return false
            # if matrix[outer_mid][0] > target:
                # set r = outter_mid - 1
            # elif matrix[outer_mid][0] < target:
                # set l = outter_mid + 1
            # else:
                # return true
        # return false

# TC: O(log n + log m) effectively log(n * m) = log n + log m / SC: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer_l, outer_r = 0, len(matrix) - 1 # O(1)

        while outer_l <= outer_r: # O(log n) where n = length of the matrix array
            outer_mid = (outer_l + outer_r) // 2 # O(1)

            if matrix[outer_mid][0] <= target <= matrix[outer_mid][-1]: # O(1)
                inner_l, inner_r = 0, len(matrix[outer_mid]) - 1 # O(1)

                while inner_l <= inner_r: # O(log m) where m = length of the inner matrix array
                    inner_mid = (inner_l + inner_r) // 2 # O(1)

                    if matrix[outer_mid][inner_mid] > target: # O(1)
                        inner_r = inner_mid - 1 # O(1)
                    elif matrix[outer_mid][inner_mid] < target: # O(1)
                        inner_l = inner_mid + 1 # O(1)
                    else: # O(1)
                        return True # O(1)
                
                return False # O(1)

            elif matrix[outer_mid][0] > target: # O(1)
                outer_r = outer_mid - 1 # O(1)
            elif matrix[outer_mid][0] < target: # O(1)
                outer_l = outer_mid + 1 # O(1)
            else: # O(1)
                return True # O(1)
        
        return False # O(1)

solution = Solution()
start_time = time.time()
print(solution.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))
print("--- %s seconds ---" % (time.time() - start_time))