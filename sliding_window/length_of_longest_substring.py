from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

def lengthOfLongestSubstring(s: str) -> int:
    # Note:
        # given a string, find longest length of the substring WITHOUT Duplicate
        # 2 pointer problem

    # Brainstorm:
        # how do human interpret the longest sequence?
            # look through the string from left to right
            # locate a point where the previous text comes up again
            # start counting again when you find duplicating character
            # remember the longest length calculated
    
    # Psuedocode (Initial thought):
    # NOT A VALID SOLUTION:
        # 1. It doesn't cover edge cases like an empty string since empty string cannot be used as a dictionary key
        # 2. Even if some of the edge cases are handled, the time complexity

    # initialize a dictionary to store character at each iteration (repeat_map)
    # initialize the maximum length count of non-duplicate substring at 0 (max_length)
    # iterate the s string
        # check if character in the ith index exists in the repeat_map
            #  if true, set the new max_length and clear the repeat_map
        # add the c to the repeat_map dictionary
    # return max_length

    # Initial Thought (NOT A VALID SOLUTION)
    # repeat_map = dict()
    # max_length = 0

    # for i, c in enumerate(s):
    #     if c in repeat_map:
    #         max_length = max(max_length, i - repeat_map[c])
    #         repeat_map.clear()

    #     repeat_map[c] = i
    
    # return max_length


    # Psuedocode:
    # initialize the 2 pointers:
        # l starting 0
        # r starting 1
    # initialize max length count (max_length_count)
    # iterate the string while r less than the length of the string:
        

    # Solution 1:
    l, r = 0, 1
    max_length_count = 0
    repeat_map = set()

    while r < len(s):
        cur_sub_string = s[l:r]
        if s[r] in repeat_map:
            duplicate_index = s[l:r].index(s[r])
            l = duplicate_index + 1

        max_length_count = max(max_length_count, r - l)
        repeat_map.add(s[r])
        r += 1

        
    return max_length_count


start_time = time.time()
print(lengthOfLongestSubstring("zxyzxyz"))
print("--- %s seconds ---" % (time.time() - start_time))