import math, time, os, random, sys, re
from collections import defaultdict, OrderedDict
from typing import List

# Leetcode 3042:


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        Notes:
            - isPrefixAndSuffix:
                - inputs:
                    1. words[i]
                    2. words[j]
                - output:
                    - boolean True / False
                - Rule:
            - countPrefixSuffixPairs:
                - inputs:
                    - words: List[str]
                - output:
                    - output: int
                        - number denotes number of pairs (i, j)
            - Rules:
                - i < j
                    - ex) ["abab","ab"]
                        - ab is both suffix and prefix, but i > j (1 > 0)
                        - Therefore, false
            - Disecting a problem:
                - compare words[i] with words[j]
                    - where x = len(words[i])
                    - where y = len(words[j])
                    - check prefix:
                        - check if words[j][0:x] == words[i]
                    - check suffix:
                        - check if words[j][y-x:y] == words[i]
                    - return number of valid pairs
        Intuition:
            - Bruteforce:
                - implement isPrefixAndSuffix(word1, word2):
                    - if word1 > word2:
                        - return false
                    - x = len(word1)
                    - y = len(word2)
                    - if word1 == word2[0:x] and word1 == word2[y-x:y]:
                        return True
                    - else:
                        return False
                - use 2 nested loops:
                    - first loop going from 0 to len(words) where i is the index
                    - second loop groing from i + 1 to len(words)
        """

        # TC: O(n^2 * k) / O(k)
        count = 0

        for i, word1 in enumerate(words):
            for j in range(i + 1, len(words)):
                word2 = words[j]
                if self.isPrefixAndSuffix(word1, word2):
                    count += 1

        return count

    # TC: O(k) where k1 is length of substrings / SC: O(k)
    def isPrefixAndSuffix(self, word1: str, word2: str):
        if word1 > word2:
            return False

        if word2.startswith(word1) and word2.endswith(word1):
            return True

        return False


solution = Solution()
start_time = time.time()
print(
    solution.countPrefixSuffixPairs(
        ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"
    )
)
print("--- %s seconds ---" % (time.time() - start_time))
