from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 2696:
class Solution:
    def minLength(self, s: str) -> int:
        # Input:
            # s: str
        # Output:
            # output: int
        # Goal:
            # given string, s, return the minimum possible length of the resulting string that I can object after removing instances of "AB" and "CD" from s
        # Rule:
            # in single operation I can...
                # remove "AB"
                # or
                # remove "CD"
            # if no operation can be made on the string, length of the string remains the same
        # Ideas:
            # Intuition - stack approach:
                # iterate on string s (c = s[i])
                    # if stack and stack[-1] == "A" and c == "B" or stack[-1] == "C" and c == "D":
                        # stack.pop
                        # continue
                    # store c in stack
                # return len(stack)
            # Bruteforce:
                # while True:
                    # replace instance of "AB" and "CD" from string s
                    # if length of current s == length of previous s, return the value
        
        # TC: O(n) / SC: O(n)
        stack = []
        for c in s:
            if stack and (stack[-1] == "A" and c == "B" or stack[-1] == "C" and c == "D"):
                stack.pop()
                continue
            stack.append(c)
        
        return len(stack)

        # Cleaner/Readable Solution:
        stack = []
        combos = set(["AB", "CD"])
        for c in s:
            if stack and stack[-1] + c in combos:
                stack.pop()
                continue
            stack.append(c)
        
        return len(stack)

        # Bruteforce:
        # TC: O(n * k) where k number of AB's and CD's are removed from s where in worst case will be n / SC: O(n)
        while True:
            s_len = len(s)

            s = s.replace("AB", "", 1)
            s = s.replace("CD", "", 1)

            if s_len == len(s):
                return s_len
    
    
solution = Solution()
start_time = time.time()
print(solution.minLength([-2,-1,1,-2]))
print("--- %s seconds ---" % (time.time() - start_time))