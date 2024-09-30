from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

def characterReplacement(s: str, k: int) -> int:
    # Note:
        # input string will always be uppercase english characters (A-Z, 26 characters)
        # characters at s can be replaced up to k many times
        # function returns the maximum length of the contiguous substring after up to kth many replacements to the s

    # Pseudocode:
        # initialize a dictionary where each character's occurances in input s (char_count)
        # initialize a variable to store the maximum possible length of contiguous substring in input s (max_length)
        # initialize the left pointer (l)
        # iterate the input s
            # iterate the current subarray
                # find most frequent character count
            # if length of the substring - most frequent character > k
                # if s[l] in char_count *** NOTE: This MUST come before the l incrementor since we need to decrease the count of char_count[s[l]] before l shifts to the next value
                    # decrement char_count[s[l]] by 1
                # increment l pointer by 1
            # else
                # if s[r] in char_count
                    # increment char_count[s[r]] by 1
                # else
                    # add s[l] to char_count initializing at 1
                # set max_length = maximum between itself and r - l + 1 (because 0 indexed)

        # return max_length
            
    # Solution 1 (TC: O(26 * N) / SC: O(N) First Version):
    # char_count = dict()
    # max_length, l = 0, 0

    # for r in range(len(s)):
    #     char_count[s[r]] = char_count.get(s[r], 0) + 1
        
    #     most_freq_c_count = 0
    #     for count in char_count.values():
    #         most_freq_c_count = max(most_freq_c_count, count)

    #     if (len(s[l:r+1])) - most_freq_c_count > k:
    #         char_count[s[l]] -= 1
    #         l += 1

    #     max_length = max(max_length, r - l + 1)

    # return max_length

    # Solution 2 (TC: O(26 * N) / SC: O(N) Cleaner version):
    # char_count = dict()
    # max_length, l = 0, 0

    # for r in range(len(s)):
    #     char_count[s[r]] = char_count.get(s[r], 0) + 1

    #     if (len(s[l:r+1])) - max(char_count.values()) > k:
    #         char_count[s[l]] -= 1
    #         l += 1

    #     max_length = max(max_length, r - l + 1)

    # return max_length

    # Solution 3 (TC: O(N) / SC: O(1) Optimal version):
    char_count = dict()
    max_length, l = 0, 0

    for r in range(len(s)):
        char_count[s[r]] = char_count.get(s[r], 0) + 1

        max_length = max(max_length, char_count[s[r]])

        if (r - l + 1) - max_length > k:
            char_count[s[l]] -= 1
            l += 1

    return r - l + 1

start_time = time.time()
print(characterReplacement("AAABABB", 1))
print("--- %s seconds ---" % (time.time() - start_time))