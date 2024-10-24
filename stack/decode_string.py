from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 394:
class Solution2:
    def decodeString(self, s: str) -> str:
        # 2nd Try (Cleaner Code):
        # Build output dynamically as iterating to ensure the complete output is ready for return by the end of the loop
        stack = [] # O(1)
        integer, res = "", "" # O(1)
        for c in s: # O(n)
            if c.isalpha(): # O(1)
                res += c
            elif c.isdigit(): # O(1)
                integer = integer + c
            elif c == "[": # O(1)
                stack.append(int(integer))
                stack.append(res)
                integer, res = "", ""
            elif c == "]": # O(1)
                substring = stack.pop()
                multiplier = stack.pop()
                res = substring + (multiplier * res)
        
        return res

class Solution1:
    def decodeString(self, s: str) -> str:
        # input:
            # s: str
                # always a valid input
                # lowercase english letters, digits, and []
                # integers in s is between 1 and 300
        # goal: return a decoded string based on the decoding rule
        # Brainstorm:
            # Main conditions:
                # s[i] == "a-z":
                    # store the sequence of letters until s[i] is not a letter
                        # when to start tracking the letter?
                            # if s[i] == "["
                        # when to stop tracking the letter? (when to push the sequence to the stack)
                            # if s[i] is an integer
                            # OR
                            # if s[i] == "]"
                # s[i] == int:
                    # store the sequence of numbers until s[i] is not an integer
                        # when to start tracking the integer digits
                            # if s[i] is an integer
                        # when to stop trackign the integer digits
                            # if s[i] == "["
                # s[i] == "[" or "]"
                    # "[" indicates the start of letter sequence
                    # "]" indicates the end of the letter sequence
            # General Idea:
                # push s[i] to the stack as long as it is a letter and an integer
                    # push the individual letters to the stack
                # pop until the integer digits are found at the top of the stack (Handling multi-layer encoded string)
                    # pop the digit from the stack, compute the sequence by multiplying the letter sequence
            # Pseudocode:
                # stack approach:
                    # use stack to store each decoding portion of the string
                        # stack: List[int || str]
                    # initialize the integer and sequence string to track
                        # integer = ""
                        # sequence = ""
                    # as iterating the input s:
                        # if s[i] is an int:
                            # integer = integer + s[i]
                        # if s[i] is alphabet:
                            # sequence = sequnce + s[i]
                        # if s[i] is "[":
                            # push sequence to stack if integer is non-empty
                            # push int(integer) to stack if integer is non-empty
                            # reset the integer and sequence to ""
                        # if s[i] is "]":
                            # while stack and stack[-1] is str:
                                # sequence = stack.pop() + sequence
                            # sequence = stack.pop() * sequence
                            # reset the sequence to ""
                    # initialize output to ""
                    # while stack is non-empty:
                        # if stack[-1] is str:
                            # output = stack.pop() + output
                        # if stack[-1] is int:
                            # output = stack.pop() * output
                    # return output string

        # TC: O(n) / SC: O(n)
        stack = [] # O(1)
        integer, sequence = "", "" # O(1)
        for c in s: # O(n)
            if c.isdigit(): # O(1)
                integer = integer + c
            elif c.isalpha(): # O(1)
                sequence = sequence + c
            elif c == "[": # O(1)
                stack.append(sequence)
                stack.append(int(integer))
                sequence, integer = "", ""
            elif c == "]": # O(1)
                while stack and type(stack[-1]) == str: # O(1) per amortized analysis, elements will only ever be pushed once and popped once at most
                    sequence = stack.pop() + sequence
                sequence = stack.pop() * sequence
                stack.append(sequence)
                sequence = ""

        stack.append(sequence) # O(1)

        output = "" # O(1)
        while stack: # O(n)
            if type(stack[-1]) == str: # O(1)
                output = stack.pop() + output
            else: # O(1)
                output = stack.pop() * output
        
        return output


solution = Solution2()
start_time = time.time()
print(solution.decodeString("3[a2[c]]"))
print("--- %s seconds ---" % (time.time() - start_time))