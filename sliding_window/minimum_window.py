from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

class Solution6:
    def minWindow(self, s: str, t: str) -> str:
        # input:
            # s: str
            # t: str
        # goal: find the shortest substring of s in t
            # includes dupliates
            # if no substring, return empty string
            # always unique output
        # Note:
            # since we need to find substring of s that includes all letters in t
                # len(s) cannot be less than t
                    # if len(s) < t, return ""
            # only uppercase and lowercase english characters
        # Sliding window approach:
            # l and r pointers
                # when does r move?
                    # as long as we r - l doesn't have every letter in t
                # when does l move?
                    # once r - l has every letter in t
            # How to know if window contains the letters?
                # we can keep track of the counts of characters in t
                    # no need to keep count of characters outside of t
                # array hashing vs dictionary:
                    # array hashing:
                        # we'll need to consider 2 casing
                            # we can change the lower to upper or vice versa
                    # dictionary:
                        # no need for casing concerns
                        # defaultdict for easy int counting
                        # O(1) access
            # iterate together or separate?
                # separate:
                    # iterate t initially for the count of each characters
                        # once t's characters are counted, we know the total number of UNIQUE characters needed
                    # first (len(t)) part of the s char could also be tracked along with t
                        # we can use this to immediately return the substring if they are exact match
                            # we are finding min substring, so if s's t_len portion matches, it's a match
                    # iterate the remainder of s starting from where we left off
            # Knowing the need count, how can we count the "have"?
                # As long as the s[r] count in s_count is == count in t_count:
                    # we can increment have
                        # if greater, we still qualify, so we won't count
            # Does the window need to contract?
                # yes, the window should get smaller while have == need
            # Return value?
                # should return a substring
                    # do we need to keep track of the substring?
                        # yes, since window size will change dynamically throughout the iteration
        # Variables to track:
            # t_count: dict
            # s_count: dict
            # need: int
            # have: int
            # min_len: int
                # we can use float("-inf") as an initial value
            # substring_pair: List[int] -> [l, r + 1]

        # Pseudocode:
            # initialize min_len to float("-inf")
            # initialize substring_pair to [-1, -1]
            # initialize t_count and s_count dictionaries
                # use defaultdict int for easy increment
            # iterate the t string (i = index, c = t[i])
                # store the count of each string to t_count
            # set need to len(t_count)
            # set have to 0
            # initialize l pointer:
                # l = 0
            # iterate the s string (r = index, c = s[i])
                # increment s_count[c] by 1
                # if c in t_count and  s_count[c] == t_count[c]:
                    # increment the "have" by 1
                # while have == need:
                    # if min_len > window size (r - l + 1):
                        # set min_len to smaller of itself or r - l + 1
                        # substring_pair = [l, r + 1]
                    # decrement s[l] in s_count by 1
                    # if s_count[s[l]] < t_count[s[l]]:
                        # decrement have by 1
                    # increment l by 1
            # l, r = substring_pair
            # return s[l, r]

        min_len = float('inf')
        substring_pair = [-1, -1]
        t_count, s_count = defaultdict(int), defaultdict(int)
        
        for c in t:
            t_count[c] += 1

        have, need = 0, len(t_count)
        l = 0
        for r, c in enumerate(s):
            s_count[c] += 1
            
            if c in t_count and s_count[c] == t_count[c]:
                have += 1

            while have == need:
                if min_len > (r - l + 1):
                    min_len = min(min_len, r - l + 1)
                    substring_pair = [l, r + 1]

                s_count[s[l]] -= 1

                if s_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        l, r = substring_pair


        return s[l:r]

class Solution5:
    def minWindow(s: str, t: str) -> str:
        # sliding window problem
        # the window of string s will ATLEAST be length of t
        # characters in s doesn't necessarily have to be in the order that the characters appear in t

        # Questions:
            # are the input s and t ever going to be in different casing?
                # ex) s = "ABC" t = "abc"
            
        # Assuming the answer to the question above is Yes,
            # I'll have to add a standardization when comparing the two substrings

        # variables to store:
            # l and r
                # l will be the left pointer
                # r will be the right pointer
            # the l and r pointer index of the shortest substring
            # count of the each letters in t
            # count of the each letters in s that are in t

        # high-level:
            # iterate r as until all matching characters in t had been found
            # increment l until matching characters are found
            # in every iteration keep the record of the valid shortest substring
            # return the substring of the shortest l,r pair

        if len(s) < len(t):
            return ""

        s_map = defaultdict(int)
        t_map = defaultdict(int)

        shortest_substring_index = [-1, -1]

        for i in range(len(t)):
            t_map[t[i]] += 1

        window_match_count, t_count = 0, len(t_map)

        l, shortest_substring = 0, float('inf')
        for r in range(len(s)):
            s_map[s[r]] += 1

            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                window_match_count += 1

            while window_match_count == t_count:
                if shortest_substring > r - l + 1:
                    shortest_substring = r - l + 1
                    shortest_substring_index = [l, r]
                s_map[s[l]] -= 1

                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    window_match_count -= 1

                l += 1
                

        l, r = shortest_substring_index
        return s[l:r + 1]

    # Note:
        # given string s and t
            # return shortest substring of s such that every character in t is present
            # includes duplicates
        # input s and t will be consisted of lowercase and uppercase english letters
        # correct output is always unique
        # if s is shorter than t, then the output would be an empty string
    
    # Question:
        # can s and t have mix of lowercase and uppercase letter?
            # will assume s and t will have unique casing
        # can input t have duplicating characters?
            # will assume t can have duplicate, and the substring of s needs to return the same number of characters that appear in input t

class Solution4:
    def minWindow(self, s: str, t: str) -> str:
        # Solution 4 (Optimal Solution / TC: O(n) SC: O(m))
        if len(s) < len(t): # O(1)
            return ""
        
        substring_char_map, t_char_map = dict(), dict()

        for c in t: # O(n)
            t_char_map[c] = t_char_map.get(c, 0) + 1

        window_match_count, t_count = 0, len(t_char_map)
        res, shortest_substring_len = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)): # O(n)
            substring_char_map[s[r]] = substring_char_map.get(s[r], 0) + 1 # O(1)
            
            if s[r] in t_char_map and substring_char_map[s[r]] == t_char_map[s[r]]: # O(1)
                window_match_count += 1 # O(1)

            while window_match_count == t_count: # O(1)
                if r - l + 1 < shortest_substring_len:
                    shortest_substring_len = r - l + 1 # O(1)
                    res = [l, r] # O(1)
                    output = s[l: r + 1]
                
                substring_char_map[s[l]] -= 1
                if s[l] in t_char_map and substring_char_map[s[l]] < t_char_map[s[l]]: # O(1)
                    window_match_count -= 1 # O(1)
                
                l += 1 # O(1)

        l, r = res
        return s[l: r + 1] if shortest_substring_len != float("infinity") else '' # O(k) where k is the size of the window but is bounded by n (k <= n)


# Solution 3 (Variation of Solution 2 / TC: O(n * m))
class Solution3:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): # O(1)
            return ""
        
        substring_char_map, t_char_map = dict(), dict()
        window_match_count, t_count = 0, len(t)
        res, shortest_substring_len = [-1, -1], float("infinity")

        for c in t: # O(n)
            t_char_map[c] = t_char_map.get(c, 0) + 1
            substring_char_map[c] = 0

        l = 0
        for r in range(len(s)): # O(n)
            if s[r] in t_char_map: # O(1)
                substring_char_map[s[r]] += 1 # O(1)
                window_match_count += 1 # O(1)

            while window_match_count >= t_count and matching_characters(t_char_map, substring_char_map): # O(m)
                shortest_substring_len = min(shortest_substring_len, r - l + 1) # O(1)
                res = [l, r] # O(1)
                
                if s[l] in t_char_map: # O(1)
                    substring_char_map[s[l]] -= 1 # O(1)
                    window_match_count -= 1 # O(1)

                l += 1 # O(1)

        l, r = res
        return s[l: r + 1] if shortest_substring_len != float("infinity") else '' # O(k) where k is the size of the window but is bounded by n (k <= n)


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        #Solution 2 (TC: O(n * m) where m is len(t) - duplicate character):
            # Brainstorm:
                # Constrains:
                    # if len(s) < len(t), return an empty output
                # Variables I need to track:
                    # map of the current matching letter count in the current window
                    # map of the matching letter count needed to qualify as a valid substring
                    # total amount of unique characters in the current window
                    # total amount of unique characters needed to qualify as a valid substring
                    # shortest substring length
                # Pseudocode:
                    # initialize an empty output string (output)
                    # if len of s is less than len t, return the output string
                    # initialize an empty map to track matching letter count in a substring (substring_char_map)
                    # initialize an empty map to store matching letter counts needed to qualify as a valid substring (t_char_map)
                    # initialize a variable to track shortest substring len (shortest_substring_len)
                    # initialize a variable for total amount of unique characters in the current window at 0 (window_match_count)
                    # initialize a variable for total amount of unique characters in string t including duplicates (t_count)
                    # iterate the t string to count occurances of each letter and increment the t_count
                    # initialize a left pointer at 0 (l)
                    # iterate the s string beginning from 0 (r = index)
                        # if s[r] is in t_char_map
                            # increment substring_char_map[s[r]] by 1
                            # increment window_match_count by 1
                        # while window_match_count is greater than or equal to t_count and t_char_map is equal to substring_char_map
                            # set shortest_substring_len to minimum value of itself and r - l + 1 
                            # set output string to s[l:r+1]
                            # if s[l] is in t_char_map
                                # decrement substring_char_map[s[l]] by 1
                            # increment the l pointer by 1
                    # return output

        output = ''
        if len(s) < len(t): # O(1)
            return output
        
        substring_char_map, t_char_map = dict(), dict()
        shortest_substring_len = len(s)
        window_match_count, t_count = 0, len(t)

        for c in t: # O(n)
            t_char_map[c] = t_char_map.get(c, 0) + 1
            substring_char_map[c] = 0

        l = 0
        for r in range(len(s)): # O(n)
            if s[r] in t_char_map: # O(1)
                substring_char_map[s[r]] += 1 # O(1)
                window_match_count += 1 # O(1)

            while window_match_count >= t_count and matching_characters(t_char_map, substring_char_map): # O(1) + # O(m)
                shortest_substring_len = min(shortest_substring_len, r - l + 1) # O(1)
                output = s[l:l + shortest_substring_len] # O(k) where k is the size of the window, but is bounded by n (k <= n)
                
                if s[l] in t_char_map: # O(1)
                    substring_char_map[s[l]] -= 1 # O(1)
                    window_match_count -= 1 # O(1)

                l += 1 # O(1)

        return output

class Solution1:
    def minWindow(self, s: str, t: str) -> str:
    # Solution 1 (Bruteforce - TC: O(m * n^2) == O(n^2) SC: O(m); where n = len(s) and m = len(t)):
        # Pseudocode:
            # initialize length variable for shortest substring (shortest_substring_len)
            # initialize an empty to store the shortest substring (shortest_substring)
            # initialize a hash map of the character counts in t (t_map)
            # iterate string s beginning length of s many times (l = index)
                # initialize an hash map to store the characters and their total count of occurances in a given window (substring_map)
                # increment the character count at s[l] by 1 if s[l] is in t
                # iterate string s beginning from l + 1 (r = index)
                    # increment the character count of s[r] by 1 if s[r] is in t
                    # if substring_map == t_map AND shortest_substring_len < r - l + 1
                        # set shortest_substring_len to r - l + 1
                        # set shortest_substring_window to (l, r + 1)
            # return substring of s at shortest_substring_window

        if s == t:
            return s

        shortest_substring_len = len(s) + 1
        shortest_substring = ""

        # Create a frequency map for string t
        t_map = dict()
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        # Outer loop for the left index of the window
        for l in range(len(s)): # O(n)
            substring_map = dict()

            # Only process if s[l] is part of t
            if s[l] in t: # O(1)
                substring_map[s[l]] = substring_map.get(s[l], 0) + 1  # Initialize with the first character

            # Check if a single character matches the entire t
            if matching_characters(substring_map, t_map): # O(m)
                return s[l:l + 1]  # If it's a single character that satisfies t / O(1)

            # Inner loop for the right index of the window
            for r in range(l + 1, len(s)): # O(n)
                if s[r] in t: # O(1)
                    substring_map[s[r]] = substring_map.get(s[r], 0) + 1

                # Check if current substring contains all chars of t
                if matching_characters(substring_map, t_map): # O(m)
                    # Update the shortest substring if a smaller one is found
                    if (r - l + 1) < shortest_substring_len: # O(1)
                        shortest_substring_len = r - l + 1
                        shortest_substring = s[l:r + 1]

                    # Break early since we found a valid substring
                    break

        return shortest_substring

def matching_characters(self, t_char_map, substring_char_map):
    for c, count in t_char_map.items(): # O(m) where m = len(t) - duplicate character
        if substring_char_map.get(c, 0) < count:
            return False
        
    return True

solution = Solution6()
start_time = time.time()
print(solution.minWindow("ADOBECODEBANC", "ABC"))
print("--- %s seconds ---" % (time.time() - start_time))
