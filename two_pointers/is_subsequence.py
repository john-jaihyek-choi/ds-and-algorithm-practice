import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 392:
class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        # input:
            # s: str
            # t: str
            # s and t both consisted of engllish lower case letters
        # goal: return boolean True if s is subsequence of t, false otherwise
            # subsequence = new string that is formed from original string by deleting some (or none) WITHOUT disturbing the relative positions of the remaining characters
        # Immediate Solution:
            # set a pointer to iterate on s at 0
            # iterate t string
                # when a char at t[s_pointer] is found, increment s_pointer by 1
            # if s_pointer >= len(s) - 1
                # return true
            # otherwise
                # return false
        
        # TC: O(n) / SC: O(1)
        s_pointer = 0
        for c in t:
            if s_pointer < len(s) and s[s_pointer] == c:
                s_pointer += 1
        
        return s_pointer == len(s)

solution = Solution2()
start_time = time.time()
print(solution.isSubsequence("abc", "ahbgdc"))
print("--- %s seconds ---" % (time.time() - start_time))