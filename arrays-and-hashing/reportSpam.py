from collections import defaultdict
from typing import List
import time


class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        # Input:
            # message: List[str]
            # bannedWords: List[str]
        # Output:
            # output: bool
                # True if the array message is spam
                # False otherwise
        # Goal:
            # given list of words in message, return whether the message is a spam or not
                # Spam if...
                    # message contains ATLEAST 2 exactly matching words from bannedWords array
                # Otherwise, not
        # Note:
            # Atleast 2 words match for message to be marked spam
        # Ideas:
            # Bruteforce (TC: O(n^2) / SC: O(1)):
                # iterate on message
                    # for each word, check if there is an exact matching word in banned Words array
                    # if there are 2 or more match, return True, otherwise false
            # Optimal method - use of set for bannedWords, then check each word in message:
                # create a set with bannedWords
                # iterate on message:
                    # check if message[i] in bannedWords_set
                    # if more than 2 word matches, return True and False otherwise
        
        # Pseudocode:
            # initialize banned_words_set = set(bannedWords)
            # banned_word_ct = 0
            # iterate on message (word = message[i])
                # if word in banned_word_set:
                    # banned_word_ct += 1
                    # if banned_word_ct >= 2:
                        # return True
            # return False

        # TC: O(n + m) / SC: O(n + m)
        banned_words_set = set(bannedWords) # TC: O(m) / SC: O(m)
        banned_word_ct = 0
        for word in message: # TC: O(n) 
            if word in banned_words_set:
                banned_word_ct += 1
                if banned_word_ct >= 2:
                    return True
        
        return False



start_time = time.time()
solution = Solution()
print(solution.reportSpam(["act","pots","tops","cat","stop","hat"]))
print("--- %s seconds ---" % (time.time() - start_time))