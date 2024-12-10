from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 1910:
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Input:
            # s: str
            # part: str
        # Output:
            # output: str
        # Goal:
            # given string s and part, find and remove the leftmost occurrence of the substring part
                # return s after removing all occurrences of part
        # Note:
            # string manipulation in python is not possible, so turn string to arr
        # Ideas:
            # Intuition (stack):
                # use stack to store each char at s
                # iterate on string s (c = s[i])
                    # append c to the stack
                    # if stack[-1] == part[-1]:
                        # check if stack[-(len(s)):] == part
                            # if true:
                                # for _ in range(len(part)):
                                    # stack.pop()
                # return "".join(stack)
        
        # TC: O(n * k) / SC: O(n)
        stack = [] 
        for c in s: # O(n)
            stack.append(c)
            if stack[-1] == part[-1] and ''.join(stack[-(len(part)):]) == part: # O(k)
                for _ in range(len(part)): # O(k)
                    stack.pop()
        
        return ''.join(stack)

        # Optimized
        stack = []
        part_list = list(part)
        k = len(part)

        for c in s:
            stack.append(c)

            if stack[-1] == part[-1] and stack[-k:] == part_list:
                del stack[-k:]

        return ''.join(stack)
    
    
solution = Solution()
start_time = time.time()
print(solution.removeOccurrences([-2,-1,1,-2]))
print("--- %s seconds ---" % (time.time() - start_time))