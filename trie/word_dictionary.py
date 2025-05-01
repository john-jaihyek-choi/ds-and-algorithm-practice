import math, time, os, random, sys, re
from collections import defaultdict, OrderedDict
from typing import List

# Leetcode 211:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary1:
    """
    Bruteforce approach:
        - intialize an array that stores words
        - addword:
            - adds a word to an array
        - search:
            - iterate on dictionary array (dict_word = dictionary[i])
                - if len(dict_word) != len(word):
                    continue
                - if dict_word == word:
                    - return True
                - iterate on word (char = word[i])
                    - if char == "." or char == dict_word[i]:
                        continue
                    - else:
                        return False
    """

    def __init__(self):
        self.dictionary = []  # SC: O(d) where d is all unique words stored

    def addWord(self, word: str) -> None:
        # TC: O(1)
        self.dictionary.append(word)

    def search(self, word: str) -> bool:
        # TC: O(w * c)

        for dict_word in self.dictionary:  # O(w) where w = len(dictionary)
            if len(dict_word) != len(word):
                continue

            if dict_word == word:
                return True

            if "." in word:  # O(k) where k = len(word) -> O(25) -> O(1)
                i = 0
                while i < len(
                    dict_word
                ):  # O(c) where c = length of characters of all words with "."
                    if dict_word[i] != word[i] and word[i] != ".":
                        break
                    i += 1

                if i == len(dict_word):
                    return True

        return False


class WordDictionary:
    """
    1. intialize WordDictionary
        - intializes an object to store word in a dictionary
    2. addWord
        - adds a given to the WordDictionary
    3. search
        - if a given string is found in dictionary:
            - return True
        - else:
            - return False
        - Q: What's considered a match?
            - exact math? partial match? etc
                - A: exact match
        - 2 main conditions:
            1. char == "."
                - process as wild card recursively for all possibilities
            2. char != "."
                - process as normal character
    Contstraints:
        - 1 <= word.length <= 25
        - word in addWord are LOWERCASE ENGLISH LETTERS
        - word in search are "." or LOWERCASE ENGLISH LETTERS
        - AT MOST 2 dots in word for search query
    """

    def __init__(self):
        self.root = TrieNode()  # SC: O(t) where t is number of unique nodes

    def addWord(self, word: str) -> None:
        # TC: O(w) where w is len(word)
        head = self.root

        for char in word:
            if char not in head.children:
                head.children[char] = TrieNode()

            head = head.children[char]

        head.end = True

    def search(self, word: str) -> bool:
        # TC: O(w) where w is len(word) / SC: O(w) for call stack used for dfs recursion

        def dfs(strt_idx: int, root: TrieNode):
            head = root

            for i in range(strt_idx, len(word)):  # O(25) -> O(1)
                char = word[i]

                if char == ".":  # O(2) -> O(1)
                    for node in head.children.values():  # O(26) -> O(1)
                        if dfs(i + 1, node):
                            return True
                    return False

                else:
                    if char not in head.children:
                        return False
                    head = head.children[char]

            return head.end

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
