from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

class Solution2:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # O(n + m) solution:
        # Idea:
            # counting from the end of the column, cell-by-cell
            # due to the sorted nature of the array, I can traverse the matrix without visiting the rows individually
        output = 0
        i, j = len(grid) - 1, 0

        while i >= 0 and j < len(grid[0]):
            if grid[i][j] < 0:
                output += len(grid[0]) - j
                i -= 1
            else:
                j += 1
        
        return output
        
class Solution1:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Note:
            # grid is sorted in decreasing order both row and column
            # grid[i] is sorted in a decreasing order
        
        # General Idea:
            # Bruteforce:
                # two nested loop to iterate grid[i] and grid[i][j]
                # O(n^2)
            # Better solution:
                # iterate on the grid array
                    # check if the last item in the grid[i] is less than 0
                        # if true, do a binary search on grid[i] with target for 0
                            # if grid[i][j] <= 0:
                                # r = m - 1
                            # else:
                                # l = m + 1
                    # number of negative numbers in grid[i] = len(grid[i]) - r + 1
                        # sum the negative numbers in grid[i] to the output
        
        # Pseudocode:
            # initialize an output to store the total number of negative numbers
            # iterate on grid:
                # if grid[i][-1] < 0
                    # initialize a l and r pointer for binary search boundary 
                    # while l <= r:
                        # m = (l + r) // 2
                        # if grid[i][m] < 0:
                            # r = m - 1
                        # else:
                            # l = m + 1
                    # output += len(grid[i]) - r + 1
            # return output
        
        # TC: O(n log m) / SC: O(1)
        output = 0 # O(1)
        for row in grid: # O(n)
            if row[-1] < 0:
                l, r = 0, len(row) - 1

                while l <= r: # O(log m)
                    m = (l + r) // 2

                    if row[m] < 0:
                        r = m - 1
                    else:
                        l = m + 1
                
                output += len(row) - (r + 1)
            
        return output

solution = Solution1()
start_time = time.time()
print(solution.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print("--- %s seconds ---" % (time.time() - start_time))