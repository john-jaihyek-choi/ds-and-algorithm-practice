from collections import defaultdict
from typing import List
import time

# Leetcode #2506:
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # Input:
            # words: List[str]
        # Output:
            # output: int
        # Goal:
            # given list of strings, words, return an integer, pairs (i, j), such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j] are similar
        # Notes:
            # similarity condition:
                # if s1 and s2 has same set of characters
        # Idea:
            # Bruteforce - set comparisons:
                # iterate words (i = index, w1 = words[i])
                    # make w1 to set (w1_set)
                    # iterate words from i + 1 (j = index, w2 = words[j]):
                        # make w2 to set (w2_set)
                        # if w1 == w2:
                            # counter += 1
            # Optimal solution - hashtable w/ set:
                # iterate the words and store the count of unique set and its count
                # iterate the hashtable and sum up the counts

        # Bruteforce:
        # TC: O(n^2) / SC: O(n)
        # pairs = 0

        # for i, w1 in enumerate(words):
        #     w1_set = set(w1)

        #     for j in range(i + 1, len(words)):
        #         w2_set = set(words[j])
        #         if w1_set == w2_set:
        #             pairs += 1

        # return pairs

        # Optimal solution:
        # TC: O(n * klogk) / SC: O(n * k)
        # TC: O(n * k) can be reduced to k since the input will only be lowercase english letter
        word_set_ct = {}
        pairs = 0
        for w in words:
            w_set = "".join(sorted(set(w)))
            word_set_ct[w_set] = word_set_ct.get(w_set, 0) + 1

        for ct in word_set_ct.values():
            pairs += ct * (ct - 1) // 2 # Combinatorics
        
        return pairs


start_time = time.time()
solution = Solution()
print(solution.similarPairs(["aba","aabb","abcd","bac","aabc"]))
print("--- %s seconds ---" % (time.time() - start_time))