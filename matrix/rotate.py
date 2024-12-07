from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 48:
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Input:
            # matrix: List[List[int]]
        # Output:
            # output: None
        # Goal:
            # Given a 2d array, rotate the matrix IN-PLACE
        # Edge-cases:
            # len(matrix) == 1:
                # no rotation
        # Note:
            # 1. To rotate the image 90 degrees, cells need to shift n - 1 times
            # 2. value of the cell being replaced needs to be remembered for it to be shifted to another cell
            # 3. Rotation needs to occur layer by layer
                # For each layer, the cells need to shift n - 1 time where n is the square layer being rotated
        # Idea:
            # Bruteforce:
                # create another n x n matrix and fill in the cell value from the original matrix:
                    # ex) Assuming 3 x 3 matrix...
                    #        new matrix    original
                    #          t, l          t, l
                    #         (0, 0)   ->   (3, 0)
                # However, this requires new memory, therefore not appropriate for the solution
            # Optimal Solution:
                # rotate the cell in place by replacing the value:
                    # (0,0) -> (0, n)
                    # (0,n) -> (n, n)
                    # (n,n) -> (n, 0)
                    # (n,0) -> (0, 0)
                # the scope of the matrix will be maintained using L/R and T/B for x-axis and y-axis for the scope of the layer roating
                # in each iteration within the rotation, cells will need to shift to next cell to "rotate"
                    # ex) Assuming 3x3 matrix
                        # 1st shift:
                            # (0,0) -> (0, 3)
                            # (0,3) -> (3, 3)
                            # (3,3) -> (3, 0)
                            # (3,0) -> (0, 0)
                        # 2nd shift:
                            # (0,1) -> (1, 3)
                            # (1,3) -> (3, 2)
                            # (3,2) -> (2, 0)
                            # (2,0) -> (0, 1)
                        # n-1 shift:
        # variables:
            # l: int
                # left
            # r: int
                # right
            # t: int
                # top
            # b: int
                # bottom
            # temp: int
                # for storage of temporary value
        # Pseudocode:
            # initialize l and r boundary:
                # l, r = 0, len(matrix) - 1
            # iterate while l < r:
                # initialize t and b to value of l and r
                    # t, b = l, r
                # iterate r-l times:
                    # *** Note ***
                        # each cell needs to shift either left, right, bottom, or top between each iteration
                            # ex)
                                # top-left cell should shift to right between each iteration
                                # top-right cell should shift to bottom between each iteration
                                # bottom-right cell should shift to the left between each iteration
                                # bottom-left cell should shift up betwee each iteration
                    # store matrix[t][l] to temp:
                        # temp = matrix[t][l + i]
                    # replace top-left of the matrix with value of bottom-left
                        # matrix[t][l + i] = matrix[b - i][l]
                    # replace bottom-left of the matrix with value of bottom-right
                        # matrix[b - i][l] = matrix[b][r - i]
                    # replace bottom-right of the matrix with value of top-right
                        # matrix[b][r - i] = matrix[t + i][r]
                    # replace top-right of the matrix with value of top-left (temp)
                        # matrix[t + i][r] = temp
                # l += 1
                # r -= 1
        
        l, r = 0, len(matrix) - 1

        while l < r:
            t, b = l, r
            
            for i in range(r - l):
                temp = matrix[t][l + i]

                matrix[t][l + i] = matrix[b - i][l]
                matrix[b-i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = temp
            
            l += 1
            r -= 1
        





solution = Solution()
start_time = time.time()
print(solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
print("--- %s seconds ---" % (time.time() - start_time))