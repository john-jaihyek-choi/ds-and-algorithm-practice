import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 151:
class Solution:
    def reverseWords(self, s: str) -> str:
        # input:
            # s: str
                # atleast 1 word in s
                # upper and lower case, digits, and spaces
        # goal: return the string where the words are reversed
            # ex) "Hi Leetcode" -> "Leetcode Hi"
        # Brainstorm:
            # Using stack:
                # stack requires O(n) space
                # keep a stack and push the words to a stack as iterating the s when space is found
                    # considerations:
                        # keep a var that tracks the "word" traversing
                        # reset the "word" to "" when space is found
                        # if word == "", don't push to stack
        # Variables to track:
            # stack: List[str]
            # word: str
        # Pseudocode:
            # initalize an empty list to be used as a stack (stack)
            # initialize a word variable to store words (word)
                # starts empty ""
            # iterate the s string (c = s[i])
                # if c is a space " " and word is non-empty:
                    # append the word to the stack
                    # then reset the word
                # else:
                    # append c to word
            # intialize an empty string for output
            # while stack is non-empty:
                # pop the top of the stack
                # append each word to output
                # if stack is non-empty:
                    # break
                # add empty space to word
            # return output

        # Stack Solution
        # TC: O(n) / SC: O(n)
        stack = []
        word = ""
        for c in s:
            word += "" if not c or c == " " else c

            if c == " " and word != "":
                stack.append(word)
                word = ""
                continue
        
        output = word
        while stack:
            output += " " if len(output) > 0 else ""
            output += stack.pop()

        return output

        # Two Pointer Solution (uses built-in):
        # TC: O(n) / SC: O(n)
        # words = s.split()
        # l, r = 0, len(words) - 1
        # while l < r:
        #     temp = words[l]
        #     words[l], words[r] = words[r], temp
        #     l += 1
        #     r -= 1

        # return ' '.join(words) 

        # Built-in method solution:
        # O(n) / SC: O(n)
        # s_list = s.split()[::-1]
        # return ' '.join(s_list)

solution = Solution()
start_time = time.time()
print(solution.reverseWords("the sky is blue"))
print("--- %s seconds ---" % (time.time() - start_time))