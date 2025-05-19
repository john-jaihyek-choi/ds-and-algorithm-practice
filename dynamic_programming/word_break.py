from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Note:
            - return True if s could be segmented in one or more dictionary words
            - word can be used mulitple times in the segmentation
        Intuition:
            - compare each word in wordDict with s[x:x+len(wordDict[i])] backwards
                - initialize an array with default value of False with length of s (output)
                - iterate wordDict (word = wordDict[i]) backwards
                    - if s[i:i+len(word)] is within bound AND s[i:i+len(word)] == word
                        - mark output[i] to True if:
                            - output[i + len(word)] is also true
                                - Note: this is because I need to ensure that after the end of the current word match, the words that come after should also match
                    - if output[i]:
                        - break
                - return output[0]
        """

        output = [False] * (len(s) + 1)
        output[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                wlength = len(word)
                if i + wlength <= len(s) and s[i : i + wlength] == word:
                    output[i] = output[i + wlength]
                if output[i]:
                    break

        return output[0]


start_time = time.time()
solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))
print("--- %s seconds ---" % (time.time() - start_time))
