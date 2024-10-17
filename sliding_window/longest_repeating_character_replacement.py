from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

# Third try:
class Solution3:
    def characterReplacement(self, s: str, k: int) -> int:
        # Note:
            # goal: return the length of the longest substring with one disttinct character after replacing up to k characters of the string
            # value to keep track of:
                # most frequent character count
                    # how: max value of new count value vs current max value
                # count map to store the letter counts

        # initialize a map to to store the letter counts (count_map)
        # initialize a frequent chracter count variable starting from 0 (max_freq)
        # initialize a variable to store the longest substing count starting from 0 (max_substring_count)
        # initialize left pointer starting from 0 (l)
        # iterate the s string from 0 (r = index, c = s[r])
            # increment count_map[c] by 1
            # set max_freq equal to max value between itself and count_map[c]
            # while length of the window (r - l - max_freq) IS NOT less than or equal to k:
                # decrement count_map[s[l]] by 1
                # increment l pointer by 1
            # set max_substring_count between r - l + 1 and itself
        # return max_substring_count

        count_map = defaultdict(int)
        max_substring_count = 0 # max_freq won't
        max_freq, l = 0, 0 

        for r, c in enumerate(s):
            count_map[c] += 1
            max_freq = max(max_freq, count_map[c])

            while not (r - l + 1 - max_freq) <= k: # because the goal is the find the longest substring, there's no need to shrink the window - therefore, "if" condition statement can be used
                count_map[s[l]] -= 1
                l += 1
            
            max_substring_count = max(max_substring_count, r - l + 1) # if "if" statement is used, then the longest window size will be retained throughout the iteration - therefore, this operation is redundant

        return max_substring_count # if "if" statement is used, I can compute the size of the window at the end of the loop
    
        
        count_map = defaultdict(int)
        max_freq, l = 0, 0

        for r, c in enumerate(s):
            count_map[c] += 1
            max_freq = max(max_freq, count_map[c])

            if not (r - l + 1 - max_freq) <= k:
                count_map[s[l]] -= 1
                l += 1

        return r - l + 1 - max_freq
            

# Second try
class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        # character at s can be replaced, at most, k many times
            # doesn't matter which of the characters are replaced as long as the overall string forms a string with identical characters
        # sliding window problem
            # window isn't necessarily k, since we can extend window larger than k
        # I want to keep the letter that appears most frequently
        # count dictionary keep count of individual character counts as I iterate
        # I'd keep max frequency count updated as going through iteration
            # since the goal is to form the longest substring, we'll want to replace something other than the chracters with max frequency count
        # if the length of the sliding window - the max frequency count <= k, then it's a valid substring

        # variables to store
            # count dictionary
            # max frquency count
            # 
        
        # when to move l and r pointers
            # r + 1 as long as the the length of the window - max frequency <= k
            # l + 1 otherwise
                # when l pointer moves, the max frequency will change
                    # since the goal of the problem is to search the max substring length, there's no need to recalculate the max frequency when decrementing
    
        count_dict = defaultdict(int)
        l, max_freq = 0, 0
        for r in range(len(s)):
            count_dict[s[r]] += 1

            max_freq = max(max_freq, count_dict[s[r]])

            if (r - l + 1) - max_freq > k:
                count_dict[s[l]] -= 1
                l += 1

        return r - l + 1
        
# Initial try
class Solution1:
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

solution = Solution3()
start_time = time.time()
print(solution.characterReplacement("AAABABB", 1))
print("--- %s seconds ---" % (time.time() - start_time))