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
    # Pseudocode:
        # 

class Solution:
    def __init__(self) -> None:
        self.result = []
        
    def generateParenthesis(self, n: int) -> List[str]:


        return self.result
    

solution = Solution()
start_time = time.time()
print(solution.generateParenthesis(3))
print("--- %s seconds ---" % (time.time() - start_time))