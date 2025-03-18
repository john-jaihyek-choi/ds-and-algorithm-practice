import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set


# Leetcode 2559:
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        """ "
        # objective:
            # given array of strings, words, and an array of integers, queries, return an array ans of size queries.length where ans[i] is the answer to ith query
        # keywords:
            # queries:
                # queries[i] = [l, r]
                    # where l and r is the indicies range of words array (l and r inclusive)
            # start and ends with vowel
                # vowel == a, e, i, o , u
        # Brainstorm:
            # Bruteforce Solution:
                # TC: O(q * k) / SC: O(q + k)
                # iterate on queries (query = queries[i]) O(q)
                    # check subarray of words array where words[query[0]:query[1]] O(k)
                    # iterate on the subarray O(k)
                        # count the total that starts and ends with a vowel
            # Optimized Solution:
                # how can I not iterate on subarray?
                    #  can I iterate on words and preprocess on words that start and ends with vowel?
                        # nope, it won't help
                    #  what if I use prefix sum of words that start and ends with vowel?
                        # ex) i = 0     1     2     3   4
                        #      ["aba","bcb","ece","aa","e"]
                        #         0     1     1     2   3
                        # Then, use the the indicies of the queries to compute total counts in range with O(1) lookup
            # general steps:
                # initialize an array for prefix_sum = []
                # initialize a query_fufilled_ct = 0
                # iterate on words: (word = words[i])
                    # append query_fulfilled_ct to prefix_sum
                    #  if word[0] is vowel and word[-1] is vowel:
                        # increment query_fulfilled_ct by 1
                # iniitalize ans array to return as an output
                # iterate on queries: (query = queries[i])
                    # start, end = query[0], query[1]
                    # range_ct = prefixsum[end] - prefixsum[start]
                    # if words[end] is vowel:
                        # range_ct += 1
                    # append the range_ct to ans array
                # return ans array"
        """

        # TC: O(n + q) / SC: O(n + q) if memory allocated for q counts as memory used
        # n = length of words
        # q = length of queries
        prefix_sum = []  # SC O(n)
        query_fulfilled_ct = 0
        for word in words:  # TC O(n)
            prefix_sum.append(query_fulfilled_ct)
            if self.startsAndEndsWithVowel(word):
                query_fulfilled_ct += 1

        ans = []  # SC O(q)
        for query in queries:  # TC O(q)
            start, end = query[0], query[1]
            range_ct = prefix_sum[end] - prefix_sum[start]
            if self.startsAndEndsWithVowel(words[end]):
                range_ct += 1

            ans.append(range_ct)

        return ans

        # Less code / Slightly more efficient
        prefix_sum = [0] * (len(words) + 1)  # SC O(n)
        for i in range(len(words)):  # TC O(n)
            prefix_sum[i + 1] = prefix_sum[i]
            if self.startsAndEndsWithVowel(words[i]):
                prefix_sum[i + 1] += 1

        ans = []  # SC O(q)
        for query in queries:  # TC O(q)
            ans.append(prefix_sum[query[1] + 1] - prefix_sum[query[0]])

        return ans

    def startsAndEndsWithVowel(self, string: str) -> bool:
        vowels = {"a", "e", "i", "o", "u"}

        if string[0] in vowels and string[-1] in vowels:
            return True

        return False


solution = Solution()
start_time = time.time()
print(solution.vowelStrings([[0, 2], [1, 4], [1, 1]]))
print("--- %s seconds ---" % (time.time() - start_time))
