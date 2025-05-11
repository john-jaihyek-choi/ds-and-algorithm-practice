from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Note:
            - s contains characters (), {}, [] brackets
            - determine if a given string is comprised of valid brackets
        Intuition:
            - Stack approach:
                - while opening brackets ( "(", "{", "[" ), add to stack
                - if closing bracket, ( ")", "}", "]" ), check against what's on stack
                    - if valid pair, pop
                    - else, return false
        """

        # TC: O(n) / SC: O(n)
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for c in s:
            if c not in pairs:
                stack.append(c)
                continue

            if stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                return False

        return not stack


# Solution 2 - same approach different idea (TC: O(n) / SC: O(n)):
def isValid(s: str) -> bool:
    stack = []
    braces_pair = {"}": "{", ")": "(", "]": "["}

    for c in s:  # O(n)
        if c not in braces_pair:  # check for opening braces
            stack.append(c)
            continue
        elif not stack or stack[-1] != braces_pair[c]:  # check for closing braces pair
            return False
        stack.pop()

    return not stack


# Solution 1 (TC: O(n) / SC: O(n)):
# Note:
# valid parenthesis are:
# Every open bracket is closed by the same type of close bracket.
# { closes with }
# [ closes with ]
# ( closes with )
# Open brackets are closed in the correct order.
# Valid: () [] {}
# Not Valid: ( [ ) ]
# Every close bracket has a corresponding open bracket of the same type.
# Valid: ( )
# Invalid: )

# Pseudocode:
# initialize an empty stack to store the opening braces
# initialize an pair of possible closing parenthesis types
# iterate the s str
# if the value in current iteration is an opening braces ( "{", "[", "(" )
# append the opening braces to the stack
# if stack has an item in the list AND if the item at the top of the stack is equals to the braces_pair[c]
# pop the item from the top of the stack
# else
# return false
# if length of the stack == 0, return true
# otherwise return false


def isValid(s: str) -> bool:
    stack = []
    braces_pair = {"}": "{", ")": "(", "]": "["}

    for c in s:  # O(n)
        if c == "{" or c == "(" or c == "[":  # check for opening braces
            stack.append(c)
        elif stack and stack[-1] == braces_pair[c]:  # check for closing braces pair
            stack.pop()
        else:  # if neither, return false
            return False

    return len(stack) == 0


start_time = time.time()
print(isValid("([{}])"))
print("--- %s seconds ---" % (time.time() - start_time))
