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

    # Solution 1:
        # Pseudocode:
            # initialize a matches_map for input t (t_count)
                # {
                #   X: 1
                #   Y: 1
                #   Z: 1
                # }
            # initialize a left pointer (l) to 0
            # iterate the input s string (i = index)
                # set the t[s[i]] equal to 0
            

    return ''


start_time = time.time()
print(minWindow("OUZODYXAZV", "XYZ"))
print("--- %s seconds ---" % (time.time() - start_time))
