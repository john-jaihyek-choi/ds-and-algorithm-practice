from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 2390:
# retried 1/13/2025
class Solution2:
    def removeStars(self, s: str) -> str:
        # input:
            # s: str
                # s consists of english lowercase letters and a *
        # output:
            # output: str
        # goal: 
            # given string, s, return the string after all stars have been removed
        # star removal rules:
            # choose a star and remove itself and the non-star character to its left
                # if 2 stars in a row, remove 2 stars and 1 non-star char to the left of it
        # ideas:    
            # intuitions: stack approach
                # initialize an empty stack (last in first out)
                # iterate the string s (i = index)
                    # check if s[i] is a star
                        # if true,
                            # remove the character at the top of the stack
                        # if false,
                            # add the character to the top of the stack
        
        # Pseudocode:
            # initialize an empty stack (output)
            # iterate on s (c = s[i]) 
                # if c == "*":
                    # if output:
                        # output.pop()
                    # continue
                # output.append(c)
            # return "".join(output)

        # TC: O(n) / SC: O(n)
        output = []
        for c in s:
            if c == "*":
                if output:
                    output.pop()
                continue
            output.append(c)

        return "".join(output)
    
                    

class Solution1:
    def removeStars(self, s: str) -> str:
        # input:
            # s: str
                # lowercase english letter or star (*)
        # goal: return an output, string, that contains the removed star and the character to immediately left it
        # Brainstorm:
            # stack approach:
                # create an empty stackt store the char in a string as iterating the s
                # on each iteration, check if the current char is a star
                    # if star,
                        # remove the prev char (top of the stack)
                        # then, move to the next char
                    # if not a start,
                        # store the char at the top of the stack
                # join the remaining items in the stack then return as a string
        # Variable:
            # stack: List[str]
        # Pseudocode:
            # initialize an empty stack to store the individual char (stack)
            # iterate on the input string (c = s[i])
                # if stack and c == "*"
                    # stack.pop() 
                    # continue
                # stack.append(c)
            # return a string that joins the characters in the stack array
        
        # TC: O(n) / SC: O(n)
        stack = [] # O(1)
        for c in s: # O(n)
            if stack and c == "*": # O(1)
                stack.pop() # O(1)
                continue 
            stack.append(c) # O(1)
        
        return ''.join(stack) # O(n)


solution = Solution2()
start_time = time.time()
# Example:
    # Input: target = 10, position = [1,4], speed = [3,2]
    # Output: 1
print(solution.removeStars(10, [4,1,0,7], [2,2,1,1]))
print("--- %s seconds ---" % (time.time() - start_time))