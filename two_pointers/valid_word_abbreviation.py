from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        Objective:
            - given strings, word and abbr, return boolean true if abbr is a valid abbreviation of word else if not
        Note:
            - 1 <= word.length <= 20
            - word is lowercase english letters
            - 1 <= len(abbr) < 10
            - abbr consists of lowercase english letters and digits
        Intuition:
            - two-pointer:
                - p1 iterates word
                - p2 iterates abbr
                - while p1 < len(word) or p2 < len(abbr):
                    - if word[p1] == abbr[p2]:
                        - p1 += 1
                        - p2 += 1
                    - else: (Not equal to each other)
                        - if type(word[p1]) == type(abbr[p2]):
                            - return False
                        - else:
                            - sub_len = ""
                            - while p2 < len(abbr) and type(abbr[p2]) == number:
                                - sub_len += abbr[p2]
                                - p2 += 1
                            - p1 += sub_len
                - return p1 < len(word) and p2 < len(abbr)
        """

        # TC: O(1) / SC: O(1)
        p1 = p2 = 0
        while p1 < len(word) and p2 < len(
            abbr
        ):  # TC: O(20 + 10) = O(1) since constraint -> 1 <= abbr.length <= 10 and 1 <= word.length <= 20
            if word[p1] == abbr[p2]:
                p1 += 1
                p2 += 1
            else:
                if not abbr[p2].isdigit() or abbr[p2].startswith("0"):
                    return False
                else:
                    sub_len = ""  # SC: O(1) since constraint -> 1 <= abbr.length <= 10

                    while (
                        p2 < len(abbr) and abbr[p2].isdigit()
                    ):  # TC: O(1) since constraint -> 1 <= abbr.length <= 10
                        sub_len += abbr[p2]
                        p2 += 1

                    p1 += int(sub_len)

                    if p1 > len(word):
                        return False

        return p1 >= len(word) and p2 >= len(abbr)


start_time = time.time()
solution = Solution()
print(solution.validWordAbbreviation("internationalization", "i12iz4n"))
print("--- %s seconds ---" % (time.time() - start_time))
