import math, time, os, random, sys, re
from collections import defaultdict, OrderedDict
from typing import List

# Leetcode 3042:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.wordCount = 0


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()  # SC: O(t) where t is unique trie nodes

    # TC: O(w) where w = len(word) / SC: O(1)
    def add_word(self, word: str) -> None:
        head = self.root

        for char in word:
            if char not in head.children:
                head.children[char] = TrieNode()
            head = head.children[char]
            head.wordCount += 1

        head.end = True

    # TC: O(p) where p is len(pref)
    def count(self, pref: str) -> int:
        head = self.root

        for char in pref:
            if char not in head.children:
                return 0
            head = head.children[char]

        return head.wordCount


class Solution2:
    def __init__(self):
        self.root = TrieNode()

    # TC: O(W * w + p) / SC: O(W * w)
    def prefixCount(self, words: List[str], pref: str) -> int:
        tree = PrefixTree()  # SC: O(t)

        for word in words:  # TC: O(W) where W is len(words)
            tree.add_word(word)  # TC: O(w) where w is len(word)

        return tree.count(pref)  # TC: O(p) where p is len(pref)


class Solution1:
    def prefixCount(self, words: List[str], pref: str) -> int:
        """
        Intuition:
            1. Bruteforce:
                - iterate on every word (word = words[i])
                    - if len(word) < len(pref):
                        - continue
                    - if word[:2] == pref:
                        - counter += 1
            2. Using trie:
                - implement trie structure
                    - add_word:
                        - add words to the prefix tree
                        - count number word_count for every revisited path
                    - count:
                        - iterates on pref and traverses prefix tree
                        - check the word_count at the end of the traversal
        """

        # Bruteforce:
        # TC: O(n * p) / SC: O(p)
        counter = 0
        for word in words:
            if len(word) < len(pref):
                continue
            if (
                word[: len(pref)] == pref
            ):  # TC: O(p) where p is len(pref), but pref.length <= 100, so O(100) -> O(1) / SC: O(p)
                counter += 1

        return counter
