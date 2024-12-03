import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 2352:
class Solution2:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Input:
            # grid: List[List[int]]
        # Output:
            # pairs: int
                # where pair = the number of pairs such that (r_i, c_j) are equal
        # Goal:
            # given a n x n grid, find the total number of row-column pair that are equal
                # considered equal if...
                    # row and column value are equal and the order in which it appears is equal
        # Edgecase:
            # if
                # row = [3, 1, 2]
                # column = [2, 1, 3]
                # pairs = 0
                # explanation: values are identical, the order is not
            # not n x n
                # constraint garantees row length and column length is identical
            # big n
                # 1 <= n <= 200
            # big integer in each array
                # 1 <= grid[i][j] <= 10^5
            # Odd number pairs?
                # example:
                    # row = [3, 2, 1]
                    # column = 2 * [3, 2, 1]
                    # pairs = 3
        # Ideas:
            # Brute-force ():
                # use a 3 nested loop to iterate on every possibility of the pair
            # Optimal solution (TC: O(n^2) / SC: O(n))
                # store every possible row variation in a form of array to dictionary (row_dict)
                    # where:
                        # key = row
                        # value = count
                # iterate each column to see if column exists in the dictionary
                    # if exists, pairs *= row_dict[column]
                # return the pairs
        # Variables:
            # row_dict: Dict[List[int], int]
                # key = row
                # val = int
            # pairs: int
                # starts at 0
        # Pseudocode:
            # initialize varaibles:
                # row_dict = {}
                # pairs = 0
            # iterate the grid, grid's length many times
                # row = grid[i]
                # row_dict[row] = row_dict.get(row, 0) + 1
            # iterate on grid (i = index)
                # set an empty array to temporarily store columns (column)
                # iterate on row (j = index)
                    # append column
                # if column in row_dict:
                    # pairs += row_dict[column] * 1
            # return pairs

        # # TC: O(n^2) / SC: O(n^2)
        row_dict = {}
        pairs = 0
        n = len(grid)

        for row in grid:
            row_dict[tuple(row)] = row_dict.get(tuple(row), 0) + 1
        
        for i in range(n): 
            column = []
            for j in range(n):
                column.append(grid[j][i])

            if tuple(column) in row_dict:
                pairs += row_dict[tuple(column)] * 1
        
        return pairs

        # cleaned and optimized:
        row_dict = Counter(tuple(row) for row in grid)
        pairs, n = 0, len(grid)

        for i in range(n):
            column = [grid[j][i] for j in range(n)]
            pairs += row_dict[tuple(column)]

        return pairs
                


class Solution1:
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



solution = Solution2()
start_time = time.time()
print(solution.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print("--- %s seconds ---" % (time.time() - start_time))