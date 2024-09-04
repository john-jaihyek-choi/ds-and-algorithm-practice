from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

ROW_SIZE = 9
COLUMN_SIZE = 9


# Solution 1
# def isValidSudoku(board: List[List[str]]) -> bool:
    # Note:
    # There are 3 criteria that must be met for a valid sudoku board
        # 1. each row must have unique 1-9 digit without any duplicate
        # 2. each column must have unique 1-9 digit without any duplicate
        # 3. each 3x3 subgrid must have unique 1-9 digits without any duplicates

    # Pseudocode:
    # create a function that checks the given row to see if a row is a valid row (is_valid_row)
        # check if any duplicate is found in board[i] using dictionary
    # create a function that checks the given column to see if a column is a valid column (is_valid_column)
        # check if any duplicate is found in board[0][j] using a dictionary
    # create a function that checks the given subgrid to see if a subgrid is a valid subgrid (is_valid_subgrid)
        #  create a dictionary to store the revealed sudoku numbers from 0-8
            # {
            #   0: [1, 2, 4, 9, 8]
            #   1: [3, 5]
            #   ...
            # }
        # then iterate the values (lists) in the dictionary to check if each subgrid is valid

#     subgrid_map = defaultdict(list)

#     for r in range(COLUMN_SIZE):
#         if not is_valid_row(board, r):
#           return False
#         elif not is_valid_column(board, r):
#             return False
        
#         for c in range(ROW_SIZE):
#             cell = board[r][c]
#             grid_index = find_subgrid_index(r, c)
#             subgrid_map[grid_index].append(cell)

#     if not is_valid_subgrid(subgrid_map):
#         return False

#     return True

# def find_subgrid_index(row: str, column: str) -> int:
#     return ((row // 3) * 3) + (column // 3)

# def contains_duplicate(list: List[str]) -> bool:
#    duplicate = {}

#    for num in list:
#         if num != '.' and num in duplicate:
#             return True
#         duplicate[num] = True

#    return False

# def is_valid_row(board: List[List[str]], r_index: int) -> bool:
#     if contains_duplicate(board[r_index]):
#         return False

#     return True

# def is_valid_column(board: List[List[str]], r_index: int) -> bool:
#     column = ['.'] * COLUMN_SIZE

#     for c_index in range(COLUMN_SIZE):
#         column[c_index] = board[c_index][r_index]

#     if contains_duplicate(column):
#         return False
    
#     return True

# def is_valid_subgrid(subgrid: Dict[str, List[int]]) -> bool:
#     for subgrid_items in subgrid.values():
#         if contains_duplicate(subgrid_items):
#             return False
        
#     return True

# Solution 2
def isValidSudoku(board: List[List[str]]) -> bool:
    row_set = defaultdict(set)
    column_set = defaultdict(set)
    subgrid_set = defaultdict(set)

    for r in range(ROW_SIZE):
        for c in range(COLUMN_SIZE):
            cell = board[r][c]
            subgrid_index = ((r // 3) * 3) + (c // 3)

            if cell == ".":
                continue
            
            if (
                cell in row_set[r]
                or cell in column_set[c]
                or cell in subgrid_set[subgrid_index]
            ):
                return False
            
            row_set[r].add(cell)
            column_set[c].add(cell)
            subgrid_set[subgrid_index].add(cell)

    return True



start_time = time.time()
print(isValidSudoku([
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
 ]))
print("--- %s seconds ---" % (time.time() - start_time))