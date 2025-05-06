import math, time, os, random, sys, re
from collections import defaultdict, OrderedDict
from typing import List

# Leetcode 3045:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str) -> None:
        head = self.root

        for a, b in zip(word, word[::-1]):
            if (a, b) not in head.children:
                head.children[(a, b)] = TrieNode()
            head = head.children[(a, b)]
            head.count += 1

    def count(self, word: str) -> int:
        head = self.root

        for a, b in zip(word, word[::-1]):
            if (a, b) not in head.children:
                return 0
            head = head.children[(a, b)]

        return head.count


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        """
        Note:
            Objective - give str1 and str2..
                return true if str1 is prefix AND suffix of str2
                return false otherwise

        Intuition:
            1. use built-in startswith and endswith method and return bool value
                General idea:
                    - create a helper function that checks if str2 starts and ends with str1
                    - iterate on words array with nested loop
                        - i = index (outer index)
                        - j = i + 1 (inner index)
                        - if words[j] does start and end with words[i]:
                            - increment pairs count
            2. Optimal solution:
                Use prefix tree:
                    - General steps:
                        - implement prefix tree and trie node
                            - stores count variable
                            - stores pointer to children character pair
                        - instead of using single character as trie node, use pair of character
                            - pair[0] is character from words[i] starting from the left
                            - pair[1] is character from words[i] starting from the end of the string
                        - iterate the words array from the back of the array
                            - for each word, update keep track of the sum of count at each traversal
        """
        tree = PrefixTree()
        res = 0

        for word in reversed(words):
            res += tree.count(word)
            tree.add(word)

        return res


solution = Solution()
start_time = time.time()
print(solution.countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]))
print("--- %s seconds ---" % (time.time() - start_time))
