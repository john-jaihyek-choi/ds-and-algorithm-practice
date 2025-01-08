from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 1456:
class Solution3:
    def maxVowels(self, s: str, k: int) -> int:
        # input:
            # s: str
            # k: str
        # output:
            # output: int
        # goal:
            # given string s and integer k, return the maximum number of vowel letters in any substring of s with length k
        # notes:
            # k is guaranteed to be <= len(s)
            # since k is the window, output would never exceed k
        # ideas:
            # intuition: set for vowels, sliding window to increase or decrease vowel count
                # create set for vowels
                # initialize vowel_count
                # count the vowels in the first k substring of s
                # iterate s beginning k and add and remove vowel_count as sliding window shifts
        # pseudocode:
            # vowels = {'a','e','i','o','u'}
            # output = 0
            # for c in s[:k]:
            #     if c in vowels:
            #         output += 1
            # for i in range(k, len(s)):
                # prev = 1 if s[i - k] in vowel else 0
                # nxt = 1 if s[i] in vowel else 0
                # output += prev - nxt
            # return output

        # TC: O(n) / SC: O(1)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for c in s[:k]:
            if c in vowels:
                count += 1

        output = count
        for i in range(k, len(s)):
            prev = 1 if s[i - k] in vowels else 0
            nxt = 1 if s[i] in vowels else 0
            count += nxt - prev
            output = max(output, count)
        return output

        # cleaner/less code:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = output = sum(1 for c in s[:k] if c in vowels)

        for i in range(k, len(s)):
            prev = 1 if s[i - k] in vowels else 0
            nxt = 1 if s[i] in vowels else 0
            count += nxt - prev
            output = max(output, count)
        return output

class Solution2:
    def maxVowels(self, s: str, k: int) -> int:
        # Note:
            # input:
                # s: str
                # k: int
            # output:
                # output: int
            # goal:
                # given str and int, s and k, return the maximum number of vowel letters in any substring of s with length k
        # Edgecases?
            # empty s:
                # s will have atleast 1 character and up to 100,000
            # k > len(s)
                # k is guaranteed to be greater than 1 and less than len(s)
            # no vowel in s:
                # return 0 since no vowels found
            # non alpha char in s:
                # s will consist only lowercase english letters
        # Ideas:
            # Brute-force:
                # 2 nested loops (i and j)
                    # i starts at 0 and ends at len(s) - k + 1
                    # j starts at i and ends at i + k
                    # in each iteration, increment count if s[j] is vowel
            # Sliding window:
                # use 2 pointers l and r for window
                # r advances each loop
                    # if s[r] is vowel, increment count
                    # when r >= k - 1:
                        # increment l by 1
                            # before incrementing, decrement the count if s[l] is vowel
        
        # Brute-force (TC: O(n^2) / SC: O(1)):
        # max_vowel_count = 0
        # vowels = set({'a', 'e', 'i', 'o', 'u'})

        for i in range(0, len(s) - k + 1):
            count = 0
            for j in range(k):
                if s[i + j] in vowels:
                    count += 1
            max_vowel_count = max(max_vowel_count, count)

        return max_vowel_count

        # sliding window:
        # l = count = max_count = 0
        # vowels = set({'a', 'e', 'i', 'o', 'u'})
        # for r in range(len(s)):
            # if s[r] in vowels:
                # count += 1
            # compute max_count
            # if r >= k - 1:
            #     if s[l] in vowels:
            #         count -= 1
            #     l += 1
        # return 0

        l = count = max_count = 0
        vowels = set({'a', 'e', 'i', 'o', 'u'})
        for r in range(len(s)):
            if s[r] in vowels:
                count += 1

            max_count = max(max_count, count)

            if r >= k - 1:
                if s[l] in vowels:
                    count -= 1
                l += 1

        return max_count

        # Cleaner code w/ better readability:
        vowels = set({'a', 'e', 'i', 'o', 'u'})
        count = max_count = sum(s[i] in vowels for i in range(k))
        
        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i-k] in vowels)
            max_count = max(max_count, count)

        return max_count


class Solution1:
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
