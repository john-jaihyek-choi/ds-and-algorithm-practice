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
        # initialize variables to store the count of open and close parenthesis being visited
        # check for base case:
            # open_count == close_count && open_count != 0
        # increment open_count by 1
        # append "(" to the permutation stack/list
        # check if:
            # close_count < open_count
            # AND
            # open_count < n
                # if true
                    # repeat
                # if false
                    # decrement open_count by 1
                    # pop the "(" from permutation stack/list
        # append ")" to the permutation stack/list
        # check if:
            # close_count < open_count
            # AND
            # open_count < n
                # if true
                    # repeat
                # if false
                    # decrement close_count by 1
                    # pop the ")" from permutation stack/list


class Solution:
    def __init__(self) -> None:
        self.result = []
        
    def generateParenthesis(self, n: int) -> List[str]:


        return self.result
    

solution = Solution()
start_time = time.time()
print(solution.generateParenthesis(3))
print("--- %s seconds ---" % (time.time() - start_time))