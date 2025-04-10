from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 58:


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        goal:
            - given string s, consisting of words + spaces, return length of the last word in a string
        ideas:
            - bruteforce:
                - use split, then return length of the last element
                - TC: O(n) / SC: O(n)
            - optimization:
                - do it in place
                    - intuition:
                        - initialize a boolean var that tracks first_letter_found
                        - initialize length = 0
                        - iterate s from the end of the word:
                            - if first_letter_found and not s[i].isalpha():
                                - continue
                            - if s[i].isalpha():
                                - length += 1
                                - first_letter_found = True
        """
        # TC: O(n) / SC: O(1)
        first_letter_found = False
        length = 0
        for i in range(len(s) - 1, -1, -1):
            if first_letter_found and not s[i].isalpha():
                return length

            if s[i].isalpha():
                length += 1
                first_letter_found = True

        return length

        # TC: O(n) / SC: O(n)
        return len(s.split()[-1])


solution = Solution()
start_time = time.time()
print(solution.lengthOfLastWord("Hello World"))
print("--- %s seconds ---" % (time.time() - start_time))
