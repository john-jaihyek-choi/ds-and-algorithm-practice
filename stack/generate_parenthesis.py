from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
from operator import add, sub, mul, truediv
import time


# Solution 1:
    # Note:
        # 1 <= n <= 7
        # well-formed parenthesis:
        # return the valid parenthesis permutations
    # Brainstorm:
        # backtracking required to search for every possible permutation
        # key considerations for backtracking:
            # 1. choices:
                # only 2 possible variation in each decision tree
                    # string += "("
                    # OR
                    # string += ")"
            # 2. constraints:
                # number of close parenthesis can't exceed that of open_count
                    # close_count < open_count
                # number of open_count can't exceed the value of n
                    # open_count < n
            # 3. goal:
                # open_count == close_count
                    # This will mean that that the permutation is a valid parenthesis
        # main challenges to solve:
            # how am I going to check 2 different variations per decision tree?
                # recurse the function by passing in ")" and "("
            # counting the open_count and close_count
                # initialize open_count at the beginning and pass the open_count to the recursing function
                # initialize close_count at the beginning and pass the close_count to the recursing function
            # where to check the constraints?
                # check close_count < open_count and open_count < n after the base case
            # where to check the goal case?
                # check open_count == close_count as a base case for the function

    # Pseudocode:
        # initialize an empty list/stack to store a valid list of permutations (result)
        # initialize an empty list/stack to store an individual permutation (permutation)
        # declare a function for backtracking recursion with 2 parameters:
            # Parameters:
                # open_count for total count of open brackets used
                # close_count for total count of close brackets used
            # check for base case:
                # open_count == close_count == n
                    # if true
                        # append the letters (joined) to the result stack
                        # then return
            # check if open_count < n:
                # append "(" to the permutation stack/list
                # backtrack with open_count + 1
                # pop the item from permutation
                    # this is intended to backtrack to previous permutation
            # check if close_count < open_count:
                # append ")" to the permutation stack/list
                # backtrack with close_count + 1
                # pop the item from permutation
                    # this is intended to backtrack to previous permutation
        # call the backtrack function and start with value of 0 for open_count and 0 for close_count
        # return the result stack


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        permutation = []

        def backtrack(open_count: int, close_count: int) -> None:
            if open_count == close_count == n:
                result.append(''.join(permutation))
                return

            if open_count < n:
                permutation.append("(")
                backtrack(open_count + 1, close_count)
                permutation.pop()
            if close_count < open_count:
                permutation.append(")")
                backtrack(open_count, close_count + 1)
                permutation.pop()
        
        backtrack(0, 0)

        return result
    

solution = Solution()
start_time = time.time()
print(solution.generateParenthesis(3))
print("--- %s seconds ---" % (time.time() - start_time))