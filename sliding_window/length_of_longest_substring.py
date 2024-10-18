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


    # Solution 1 Psuedocode:
    # initialize the 2 pointers:
        # l starting 0
        # r starting 0
    # initialize max length count (max_length_count)
    # initialize a set to store the unique characters (repeat_map)
    # iterate the string while r less than the length of the string:
        # while s[r] is in repeat_map
            # remove s[l] (left most of the current substring) from the repeat_map set
            # then increment the l pointer by 1
        # set the max_length_count to max of itself and r - l + 1 (+1 because 0 indexed)
        # increment the r pointer by 1
    # return the max_length_count

    # Solution 1 (TC: O(n) / SC: O(n)):
    # l, r = 0, 0
    # max_length_count = 0
    # repeat_map = set()

    # while r < len(s):
    #     while s[r] in repeat_map:
    #         repeat_map.remove(s[l])
    #         l += 1
    #     max_length_count = max(max_length_count, r - l + 1)
    #     repeat_map.add(s[r])
    #     r += 1
        
    # return max_length_count

    # Solution 2 (TC: O(n) / SC: O(n) Cleaner/More Readable):
    l, max_length_count = 0, 0
    repeat_map = set()

    for r, c in enumerate(s):
        while c in repeat_map:
            repeat_map.remove(s[l])
            l += 1
        repeat_map.add(c)
        max_length_count = max(max_length_count, r - l + 1)

    return max_length_count

    # Solution Retry (10/17/2024)
    # s = string
    # goal: find substring WITHOUT duplicate characters
    # Brainstorm:
        # how to go about keeping count of the char
            # use set
        # two pointers - left and right
            # when does left move?
                # moves when encounters s[i] that's already in the set
            # when does right move?
                # moves as long as it doesn't encounter s[i] that's in the set
        # Does the window have to contract?
            # Yes, the window must contract until s[l] finds the duplicate letter
                # what does this mean?
                    # WHILE s[r] exists in char_set, l moves and removes the letters in char_set
        # What's being returned?
            # the length of the longest substring
            # do I need to initialize and keep it updated?
                # yes, I'll have to keep updated for edge cases such as repeating duplicate characters
    # Pseudocode:
        # initialize a set to store the characters iterating (char_set)
        # initialize max substring (max_substring)
        # initialize l pointer:
            # l starting from 0 (l)
        # loop len(s) - 1 many times (r = index)
            # set char for easy access:
            # while char in char_set:
                # remove s[l] from the char_set
                # l += 1
            # add the s[r] to char_set
        # return 

    char_set = set()
    l = 0
    max_substring = 0
    for r, c in enumerate(s):
        while c in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(c)
        max_substring = max(max_substring, r - l + 1)
    
    return max_substring





start_time = time.time()
print(lengthOfLongestSubstring("pwwkew"))
print("--- %s seconds ---" % (time.time() - start_time))