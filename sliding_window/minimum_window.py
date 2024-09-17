from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

def minWindow(s: str, t: str) -> str:
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
        # can input t have duplicating charactes?
            # will assume t can have duplicate, but substring of s doesn't necessarily have to return the same number of characters that appear in input t

    # Brainstorm:
        # check string s and find first instance of any characters in string t
        # move the pointer with respect to the index where the first instance of the matching char with t to the right
            # repeat until we exhaust the count of the unique letters in t
        # Once the count is exhausted, return the string between left and the right pointer
        # 
        # need a way to standardize the lowercase and uppercase comparison

    # Solution 1 (Bruteforce - TC: O(m * n^2) == O(n^2) SC: O(m); where n = len(s) and m = len(t)):
        # Pseudocode:
            # initialize length variable for shortest substring (shortest_substring_len)
            # initialize a tuple to store the left and the right pointers (index) of the shortest substring length (shortest_substring_window)
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

    def contains_all_chars(substring_map): # O(m) where m = length of t - the duplicates
        for char, count in t_map.items():
            if substring_map.get(char, 0) < count:
                return False
        return True
    
    # Outer loop for the left index of the window
    for l in range(len(s)): # O(n)
        substring_map = dict()

        # Only process if s[l] is part of t
        if s[l] in t: # O(1)
            substring_map[s[l]] = substring_map.get(s[r], 0) + 1  # Initialize with the first character

        # Check if a single character matches the entire t
        if contains_all_chars(substring_map): # O(m)
            return s[l:l + 1]  # If it's a single character that satisfies t / O(1)

        # Inner loop for the right index of the window
        for r in range(l + 1, len(s)): # O(n)
            if s[r] in t: # O(1)
                substring_map[s[r]] = substring_map.get(s[r], 0) + 1

            # Check if current substring contains all chars of t
            if contains_all_chars(substring_map): # O(m)
                # Update the shortest substring if a smaller one is found
                if (r - l + 1) < shortest_substring_len: # O(1)
                    shortest_substring_len = r - l + 1
                    shortest_substring = s[l:r + 1]

                # Break early since we found a valid substring
                break

    return shortest_substring


start_time = time.time()
print(minWindow("OUZODYXAZV", "XYZ"))
print("--- %s seconds ---" % (time.time() - start_time))
