import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 151:
# 1/3/2025 recap
class Solution3:
    def reverseWords(self, s: str) -> str:
        # input:
            # s: str
        # output:
            # output: str
        # goal: 
            # given string, s, return the reversed string s as an output
        # note:
            # there could be leading and ending multi-spaces
            # there could be multi-spaces in between words
            # s contains uppercase and lowercase english letters, digits, and spaces
            # s contains atleast 1 word
        # ideas:
            # intuition (TC: O(n) / SC: O(n)):
                # split the string using built-in split method
                # use two pointers to reverse the words
                # repeat until l and the r pointer meets
        
        # Pseudocode:
            # initialize output array with s.split()
                # split should take care of the multi-spaces
            # initialize l and r pointer
                # l = 0
                # r = len(s) - 1
            # iterate until l and r meets
                # output[l], output[r] = output[r], output[l]
                # increment l
                # decrement r
            # join the output array and return the result
        
        # TC: O(n) / SC: O(n)
        output = s.split()
        l, r = 0, len(output) - 1
        while l < r:
            output[l], output[r] = output[r], output[l]
            l += 1
            r -= 1
        
        return ' '.join(output)

        # Stack (Assuming built-in split is not allowed)
        # TC: O(n * k) / SC: O(n)
        l, r = 0, len(s) - 1
        stack = []
        word = []
        for c in s:
            if c.isalnum():
                word.append(c)
            else:
                if word:
                    stack.append("".join(word))
                word.clear()
        stack.append("".join(word))

        output = []
        while stack:
            w = stack.pop()
            if w and w != "":
                output.append(w)

        return " ".join(output)

        
        

class Solution2:
    def reverseWords(self, s: str) -> str:
        # Note:
            # input:
                # s: str
            # output:
                # output: str
            # goal:
                # given string s, reverse the words in a string
        # edge-case scenarios:
            # multiple spaces between words
                # should ignore empty spaces
            # empty string s
                # s guaranteed to be longer than len 1
            # non alphabet in s?
                # digit allowed
                    # ignore digit
        # General approach:
            # 1. Assuming built-in reverse and split is allowed:
                # split s, then reverse
                # TC: O(n) / SC: O(n)
            # 2. Assuming built-in split is allowed but no reverse:
                # split s, iterate the splited s from the end of the list, append each word to output arr
                # TC: O(n) / SC: O(n)
            # 3. Assuming no built-in method is allowed:
                # stack-approach
                    # initialize a stack []
                    # initialize a word_arr []
                    # iterate the s 
                        # when s[i] == space and word_arr is non-empty
                            # append "".join(word_arr) to stack
                            # set word_arr back to empty arr
                            # continue
                        # append s[i] to word_arr
                    # while stack is non-empty:
                        # append stack[-1] to output

        # 1. split s, then reverse
        output = s.split()
        output.reverse()
        return " ".join(output)

        # 2. split s, iterate the splited s from the end of the list, append each word to output arr
        output = s.split()
        res = []
        for i in range(len(output) - 1, -1, -1):
            res.append(output[i])
        
        return " ".join(res)

        # 3. stack approach:
        stack = []
        word_arr = []
        for i, c in enumerate(s):
            if c == " " and word_arr:
                stack.append("".join(word_arr))
                word_arr = []
                continue
            else:
                if c != " ":
                    word_arr.append(c)

        output = ["".join(word_arr)] if word_arr else []
        while stack:
            word = stack.pop()
            if word and word != "":
                output.append(word)

        return " ".join(output)

        # 4. split s, use two-pointers:
        s_arr = s.split()
        l, r = 0, len(s_arr) - 1
        while l < r:
            s_arr[l], s_arr[r] = s_arr[r], s_arr[l]

            l += 1
            r -= 1
        
        return " ".join(s_arr)
                        

class Solution1:
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
        # TC: O(n^2) / SC: O(n)
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