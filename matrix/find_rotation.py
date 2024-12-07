from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 1886:
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # Input:
            # mat: List[List[int]]
            # target: List[List[int]]
        # Output:
            # output: bool
        # Goal:
            # given 2d matrix array, return True if mat, when rotated, could be euqal to target matrix and False otherwise
        # Edgecase:
            # len(mat) != len(target):
                # constraint guarantees the two matrix will equal
        # Idea:
            # Intuition:
                # rotate mat by 90 degrees increment:
                    # check between each rotation
                # 4 rotation == Full rotation
        # Pseudocode:
            # iterate 4 times (4 rotation == full rotation)
                # if mat == target:
                    # return True
                # intialize left and right boundary
                    # l, r = 0, len(mat) - 1
                # while l < r:
                    # initialize top and bottom boundary:
                        # t, b = l, r
                    # iterate r - l times:
                        # temp = mat[t][l + i]
                        # mat[t][l + i] = mat[b - i][l]
                        # mat[b - i][l] = mat[b][r - i]
                        # mat[b][r - i] = mat[t + i][r]
                        # mat[t + i][r] = temp
                    # l += 1
                    # r -= 1
            # return False
        
        # TC: O(n^2) / SC: O(1)
        for _ in range(4): # O(1)
            if self.matrix_match(mat, target):
                return True

            self.rotate(mat) # O(n^2)

        return False

    def rotate(self, mat: List[List[int]]) -> None:
        l, r = 0, len(mat) - 1
        while l < r:
            t, b = l, r

            for i in range(r-l):
                temp = mat[t][l + i]

                mat[t][l + i] = mat[b - i][l]
                mat[b - i][l] = mat[b][r - i]
                mat[b][r - i] = mat[t + i][r]
                mat[t + i][r] = temp

            l += 1
            r -= 1
    
    def matrix_match(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        return False




solution = Solution()
start_time = time.time()
print(solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
print("--- %s seconds ---" % (time.time() - start_time))