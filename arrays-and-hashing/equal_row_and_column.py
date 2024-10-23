import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 2352:
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # ex)
        # [[3,2,1],
        #  [1,7,6],
        #  [2,7,7]]
        # input:
            # grid: List[List[int]]
        # goal: return the total count of matching pairs
            # r, c pair is matching if ri and ci has a matching numbers in order
        # Brainstorm:
            # create and store the row and col in a hash_map
                # register row items to the row map
                    # keep the total count of the unique row
                        # key: Tuple[int]
                        # value: int
                # register col items to the col map
                        # key: Tuple[int]
                        # value: int
            # iterate on row set:
                # if row exists in col hash_map
                    # set matches to the sum of itself and product of the the row_map[row] and col_map[row]
        # Variables:
            # row_map: Set[Tuple[int]]
            # col_map: Set[Tuple[int]]
            # matches: int
                # begins at 0
        # Pseudocode:
            # initialize a hash map for row and col with default value as int
                # row_map
                # col_map
            # initialize a matches counter (matches) at 0
            # register row to the row_map
                # iterate the grid (i = index)
                    # set row, grid[i], to tuple
                    # increment row_map[row] by 1

                    # register col to the col_map:
                        # initialize an empty array to store col
                        # iterate the grid (i = index)
                            # append grid[r][c] to col_map
                        # set col array to col_map as Tuple 
                        # increment col_map[col] by 1
            # iterate on row_map (row = row_map[i]) 
                # if row is in col_map:
                    # set matches to sum of itself and the product of row_map[row] and col_map[row]
            # return matches

        # TC: O(n^2) / SC: O(n)
        row_map, col_map = defaultdict(int), defaultdict(int) # TC O(n) / SC O(n)
        matches = 0 # O(1)
        for r in range(len(grid)): # O(n)
            row_map[tuple(grid[r])] += 1 # O(1)

            col = [] # SC O(n)
            for c in range(len(grid)): # TC O(n)
                col.append(grid[c][r]) # O(1)

            col_map[tuple(col)] += 1 # O(1)
            
        for row in row_map: # O(n)
            if row in col_map: # O(1)
                matches += (col_map[row] * row_map[row]) # O(1)
        
        return matches # O(1)



solution = Solution()
start_time = time.time()
print(solution.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print("--- %s seconds ---" % (time.time() - start_time))