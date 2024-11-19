import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 443:
class Solution:
    def compress(self, chars: List[str]) -> int:
        # Note:
            # input:
                # chars: List[str]
            # output:
                # output: int
            # goal:
                # given list of str, chars, return an integer output that represents the length of the array after compressing the characters based on the compression rule
                    # compression rule:
                        # for each group of consecutive repeating characters in chars
                            # if group's length == 1
                                # append char to s
                            # else:
                                # append characters followed by the group's length
                # Requirement: algorithm must use O(1) space
                # if group length > 10, split the value to multiple characters
            # Question about the input:
                # does the input come in a consecutive group already?
                    # the question implies that the chars array is a group of consecutive repeating characters
            # Approach:
                # Brute-foce:
                    # use hash map for count of individual char
                    # iterate hash_map.items() (key = key, count = val)
                        # append key to the s arr
                        # append [d for d in str(count)]
                    # return the length of the s arr
                # Space Optimal Solution (two-pointer with subarray replacement):
                    # use two-pointers - l and r
                        # l = r = 0
                    # while l < len(chars):
                        # if chars[r] != chars[l]:
                            # chars[l:r] = [chars[l]] + [d for d in str(r - l)]
                            # l = r
                        # else: (chars[r] == chars[l])
                            # r += 1
            
        # Brute-force:
        char_count = {}
        for c in chars:
            char_count[c] = char_count.get(c, 0) + 1

        s = []
        for key, count in char_count.items():
            s.append(key)
            s.extend([d for d in str(count)])

        return len(s)
            
        # Two-pointer with subarray replacement Approach:
        # Pseudocode:
            # l = r = 0
            # while l < len(chars):
            # if chars[r] != chars[l]:
                # chars[l:r] = [chars[l]] + [d for d in str(r - l)]
                # l = r
                # continue
            # r += 1
            
        l, r = 0, 0 
        while l < len(chars):
            char_r = chars[r] if r < len(chars) else ""
            if char_r != chars[l]:
                new_subarray = ([chars[l]] + [d for d in str(r - l)]) if r - l > 1 else [chars[l]]
                chars[l:r] = new_subarray
                r = r - (r - l - len(new_subarray))
                l = r
                continue
            r += 1

        return len(chars)

        # Two-pointer without subarray replacement (TC: O(n) / SC: O(1)):
        char_start, cur = 0, 0

        while cur < len(chars):
            letter = chars[cur]
            count = 0

            while cur < len(chars) and chars[cur] == letter:
                count += 1
                cur += 1
            
            chars[char_start] = letter
            char_start += 1
            if count > 1:
                for d in str(count):
                    chars[char_start] = d
                    char_start += 1
        
        return char_start
                


solution = Solution()
start_time = time.time()
print(solution.compress(["a","a","a","b","b","a","a"]))
print("--- %s seconds ---" % (time.time() - start_time))