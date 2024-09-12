from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

def checkInclusion1(s1: str, s2: str) -> bool:
    # Note:
        # 2 strings, s1 and s2
        # if s2 has permutation of s1, return true, otherwise false.
        # permutation - arrangement or ordering of elements of a set into specific sequence or order

    # Solutions:
        # 1. sort s1, then take each sorted s2 substring to compare (TC: O(n * m log(m)) / SC: O(m))
        # 2 - 3. create a frequency array to store the frequency for s1 and s2, then compare (TC: O(n * m) / SC: O(1))
        # 4. create s1 count map and s2 substring count map, and compare s1 map with s2 substring map

    # Solution 4 ( TC: O(26 * m) == O(m) / SC: O(26) == O(1) ):
        # Pseudocode:
            # if length of s1 > length of s2, return true
            # initialize s1 count map (s1_count)
            # initialize s2 substring count map (s2_substring_count)
            # iterate 26 times to initialize the keys of s1 and s2 count from a-z with default value 0
            # iterate the s1 string and store the letter count and store the initial window for s2
            # if s1_count == s2_substring_count
                # return True
            # initialize l pointer (l)
            # iterate s2 starting from length of s1 and ending at length of s2 (r = index)
                # if s1_count matches s2_substring_count
                    # return True
                # Otherwise,
                    # increment the s2[r] to s2_substring_count by 1
                    # decrement the s2[l] to s2_substring_count by 1
                    # increment the left pointer by 1 to move the window

    s1_len, s2_len = len(s1), len(s2)

    if s1_len > s2_len: # O(1)
        return False

    s1_count = dict()
    s2_substring_count = dict()

    for i in range(ord('a'), ord('z') + 1): # O(26)
        s1_count[chr(i)] = 0
        s2_substring_count[chr(i)] = 0

    for i in range(len(s1)): # O(n)
        s1_count[s1[i]] += 1
        s2_substring_count[s2[i]] += 1
        
    if s1_count == s2_substring_count: # O(1)
        return True

    l = 0
    for r in range(s1_len, s2_len): # O(m - n)
        if s1_count == s2_substring_count: # O(26)
            return True

        s2_substring_count[s2[r]] += 1
        s2_substring_count[s2[l]] -= 1
        l += 1

    if s1_count == s2_substring_count:
        return True

    return False


    # Solution 3 (variation of Solution 2):
    # Lengths of the strings
    m, n = len(s1), len(s2)
    
    # If s1 is longer than s2, return False
    if m > n:
        return False
    
    # Frequency arrays for s1 and for the current window in s2
    s1_count = [0] * 26  # Frequency array for s1
    s2_count = [0] * 26  # Frequency array for the sliding window in s2
    
    # Fill the frequency array for s1
    for char in s1:
        s1_count[ord(char) - ord('a')] += 1
    
    # Initialize the first window in s2
    for i in range(m):
        s2_count[ord(s2[i]) - ord('a')] += 1
    
    # Compare the first window
    if s1_count == s2_count:
        return True
    
    # Start sliding the window
    for i in range(m, n):
        # Add the new character to the window
        s2_count[ord(s2[i]) - ord('a')] += 1
        # Remove the old character from the window
        s2_count[ord(s2[i - m]) - ord('a')] -= 1
        
        # Compare frequency arrays
        if s1_count == s2_count:
            return True
    
    # If no permutation found
    return False

    # Solution 2:
    if len(s1) > len(s2): # O(1)
        return False
    
    s1_freq = [0] * 26 # O(26) = O(1)

    for c in s1: # O(n), n = len(s1)
        s1_freq[ord(c) % 97] += 1

    for i, c in enumerate(s2): # O(m), m = len(s2)
        substring_freq = [0] * 26 # O(1) 

        for l in s2[i:i + len(s1)]: # O(m) + O(m)
            substring_freq[ord(l) % 97] += 1 # O(1)
        
        if substring_freq == s1_freq: # O(1)
            return True

    return False

    # Solution 1 (TC: O(n * m log(m)) / SC: O(m))
    if len(s1) > len(s2): # O(1)
        return False
    sorted_s1 = "".join(sorted(s1)) # O(n log m) + O(m)

    if len(s1) > len(s2): # O(1)
        return False

    for i in range(0, len(s2)): # O(m)
        sorted_substring = "".join(sorted(s2[i:(i + len(s1))]))  # O(m) + O(m log m)
        if sorted_substring == sorted_s1: # O(m)
            return True

    return False


start_time = time.time()
print(checkInclusion1("adc", "dcda"))
print("--- %s seconds ---" % (time.time() - start_time))
