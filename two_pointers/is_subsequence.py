import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 392:
# 1/6/2025 recap
class Solution4:
    def isSubsequence(self, s: str, t: str) -> bool:
        # input:
            # s: str
            # t: str
        # output:
            # output: bool
        # goal:
            # given strings, s and t
                # return true if s is a subsequence of t
                # false otherwise
        # note:
            # if len(s) > len(t):
                # immediately False
        # ideas:
            # intuition: two-pointer approach 
                # set a guard condition for len(s) > len(t)
                    # return False if true
                # initialize a pointer to track position at string s
                # iterate on t
                    # if s[x] == s[i]:
                        # increment x
                # return x >= len(s) - 1
        # Pseudocode:
            # if len(s) > len(t):
                # return False
            # if s == t:
                # return True
            # s = 0
            # for i in t:
                # if x >= len(s):
                    # break
                # if s[x] == s[i]:
                    # x += 1
            # return x >= len(s)
        
        # TC: O(n) / SC: O(1)
        if len(s) > len(t):
            return False
        if s == t:
            return True
        
        x = 0 
        for c in t:
            if x >= len(s):
                break
            if s[x] == c:
                x += 1

        return x >= len(s)



class Solution3:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Note:
            # input:
                # s: str
                # t: str
            # output:
                # output: bool
            # goal:
                # given string s and t, return boolean
                    # True if s is subsequence of t
                    # False otherwise
                # Checking if s is subsequence of t
                    # len(s) < t
        # potential scenarios:
            # len(s) > t:
                # return False
        # Idea:
            # Brute-force (TC: O(n^3) / SC: O(1)):
                # 3 nested loops (i, j, k)
                    # where i starts 0
                    # j = i + 1
                    # k = j + 1
            # Two-pointer approach:
                # iterate on t while tracking the "checked" index of s
                    # checked_idx will start 0
                    # if t[i] == s[checked_idx]:
                        # increment checked_idx

        # Two-pointer approach (TC: O(n) where n = len(t) / SC: O(1)):
        if len(s) > len(t):
            return False

        s_idx = 0

        for t_idx in range(len(t)):
            if s_idx >= len(s):
                return True

            if t[t_idx] == s[s_idx]:
                s_idx += 1

        return s_idx >= len(s)
    
        # Brute-force:
        if len(s) > len(t):
            return False

        for i in range(len(t)):
            for j in range(i + 1, len(t)):
                for k in range(j + 1, len(t)):
                    sequence = [t[i], t[j], t[k]]
                    if "".join(sequence) == s:
                        return True
        
        return False

class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Create a list to store the positions of each character in t
        positions = defaultdict(list)
        
        for i, c in enumerate(t):
            positions[c].append(i)
        
        current_position = -1  # Start before the first index
        
        for char in s:
            if char not in positions:  # If char from s is not in t, return False
                return False
            
            # Use the binary search to find the right position
            pos_list = positions[char]
            current_position = self.binary_search(pos_list, current_position)
            
            if current_position == len(pos_list):  # No valid position found
                return False
            
            # Update current_position to the index of the found position
            current_position = pos_list[current_position]

        return True
    
    def binary_search(self, pos_list, current_position):
        left, right = 0, len(pos_list)
        
        while left < right:
            mid = (left + right) // 2
            if pos_list[mid] <= current_position:
                left = mid + 1  # Move right to find the rightmost position
            else:
                right = mid  # Move left since mid is too high

        return left  # This is the insertion point (rightmost index + 1)
    
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