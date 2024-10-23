import math, time
from collections import defaultdict, deque, Counter
from typing import List, Dict, DefaultDict, Set

# Leetcode 1657:
class Solution4:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 4th try:
        # array hashing from start
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        word1_count, word2_count = [0] * 26, [0] * 26
        for i in range(len(word1)):
            word1_count[ord(word1[i]) - ord('a')] += 1
            word2_count[ord(word2[i]) - ord('a')] += 1

        word1_count.sort()
        word2_count.sort()
        
        return word1_count == word2_count
    
class Solution3:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 3rd try:
        # Use of Counter method
        # TC: O(n + m log n) / SC: O(m) where m = 26
        word1_freq = sorted(Counter(word1).values())
        word2_freq = sorted(Counter(word2).values())

        return word1_freq == word2_freq and set(word1) == set(word2)
    
class Solution2:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 2nd try:
        # How can I compare the two words frequencies without the use of array hashing?
            # sorting the values of the word1_count and word2_count will give the frequencies in order
        # TC: O(n + m log n) / SC: O(n) where m = 26 (26 characters in an alphabet)
        word1_set, word2_set = set(word1), set(word2)
        if len(word1) != len(word2) or word1_set != word2_set:
            return False
        
        word1_count, word2_count = defaultdict(int), defaultdict(int)
        for i in range(len(word1)):
            word1_count[word1[i]] += 1
            word2_count[word2[i]] += 1
        
        word1_freq, word2_freq = sorted(word1_count.values()), sorted(word2_count.values())

        return word1_freq == word2_freq

    
class Solution1:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # input:
            # word1: str
            # word2: str
            # word1 and word2 only consists of lowercase english letters
        # goal:
            # Return the boolean
                # True if 
                    # word1 is close to word2
                # else False
        # Idea of being "close":
            # word is "close" if it can attain one word from another using 2 possible operations:
                # 1. swap any 2 existing characters
                # 2. transform every occurrences of one existing character into another existing character
            # Conclusion:
                # word1 is close if it has identical unique set of characters in word2
                    # however, the count of unique letters don't necessarily have to be identical
                        # as operation 2 allows the transformation of existing char to another existing character
                # ***IMPORTANT***:
                    # It is crucial that the frequency pattern of word1 must match that of word2
                        # ex) word1 = "abbzzca", word2 = "babzzcz"
                            # these two won't be close words because:
                                #                            a  b  c  z
                                # word1 frequency pattern is 2, 2, 1, 2
                                # word2 frequency pattern is 1, 2, 1, 3
        # Initial Try:
            # storing the count of the characters in hash map (word1_count and word2_count):
                # key: str
                    # the letter
                # value: int
                    # the count of characters
            # store the count of charcters in an array:
                # initialize an array with 0 as a default value
                # iterate on the word1_count and word2_count:
                    # increment the counter at word1_count[count]
                    # increment the counter at word2_count[count]
        # Variables:
            # word1_hash: Dict[int, List[str]]
            # word2_hash: Dict[int, List[str]]
            # count_array1: List[int]
            # count_array2: List[int]
        # Pseudocode:
            # if the length of word1 is not equal to length of word2:
                # return False
            # initialize an empty word1_count and word2_count
                # initialize with defaultdict with type int
            # iterate the length of word1 many times (i = index)
                # increment word1[i] by 1
                # increment word2[i] by 1
            # initialize a count_array with length of word1:
                # initialize each index with 0 as default value
            # iterate word1_count (char = key, count = value)
                # increment the counter at count_array1[count]
            # iterate word2_count (char = key, count = value)
                # increment the counter at count_array2[count]
            # return count_array1 == count_array2

        # TC: O(n) / SC: O(n)
        word1_set, word2_set = set(word1), set(word2)
        if len(word1) != len(word2) or word1_set != word2_set:
            return False
        
        word1_count, word2_count = defaultdict(int), defaultdict(int)
        for i in range(len(word1)):
            word1_count[word1[i]] += 1
            word2_count[word2[i]] += 1
        
        count_array1, count_array2 = [0] * (len(word1) + 1), [0] * (len(word2) + 1)
        for count in word1_count.values():
            count_array1[count] += 1

        for count in word2_count.values():
            count_array2[count] += 1

        return count_array1 == count_array2 and word1_set == word2_set

solution = Solution3()
start_time = time.time()
print(solution.closeStrings([1,0,0,0,0,1], 2))
print("--- %s seconds ---" % (time.time() - start_time))