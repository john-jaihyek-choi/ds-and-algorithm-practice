from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # input:
            # s: str
                # 1 <= s.length <= 100,000
                # s consists of only lowercase english letters
            # k: int
                # 1 <= k <= s.length
        # goal: return the maximum number of vowels in a substring of s with size k
        # Note:
            # using sliding window approach
            # consider starting both l and r pointer at 0 and handle sliding logic with condition instead of using substring
                # to prevent big k input
        # Variable to track:
            # max_vowel_count: int
                # start at 0
            # vowels: set
                # initialize a set with lower case vowels
            # l: int
            # r: int
            # count: int
                # counts the current instances of vowels
        # Pseudocode:
            # initialize max_vowel_count at 0 (max_vowel_count)
            # initialize a set with lower case vowels (vowels)
            # initialize l pointer at 0
            # iterate the s string (r = index, c = s[r])
                # if c in vowels:
                    # count += 1
                    # max_vowel_count = max(max_vowel_count, count)
                # if r >= k - 1:
                    # if s[l] in vowels:
                        # count -= 1
                    # increment l
                # if max_vowel_count == k:
                    # return max_vowel_count
            # return max_vowel_count

        # TC: O(n) / SC: O(1)
        vowels = set({"a", "e", "i", "o", "u"}) # O(1)
        max_vowel_count, count, l = 0, 0, 0 # O(1)
        for r, c in enumerate(s): # O(n)
            if c in vowels: # O(1)
                count += 1
                max_vowel_count = max(max_vowel_count, count)

            if r >= k - 1: # O(1)
                if s[l] in vowels: # O(1)
                    count -= 1
                l += 1
            
            if max_vowel_count == k: # O(1)
                return max_vowel_count

        return max_vowel_count # O(1)


solution = Solution()
start_time = time.time()
print(solution.maxVowels("abciiidef", 3))
print("--- %s seconds ---" % (time.time() - start_time))
