from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


# Leetcode 1249:
class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Note:
            - Valid parentheses:
                - empty string
                - contains only lower case english char
                - string A and B can be concatenated where A and B are valid strings
                - a valid string sits between ( and )
        Intuition:
            - Use stack to keep track of parenthesis and set to remember invalid position:
                - iterate on s
                    - if opening parenthesis, push to stack
                    - if closing parenthesis,
                        - if stack is non-empty:
                            - pop the top of the stack
                        - else:
                            add (c, i) pair to the invalid position set
                - while stack has remaining open parenthesis (to be removed)
                    - pop the stack and add the position of the invalid parenthesis to the invalid set
                - iterate from s again
                    - if i in invalid position (invalid character, so skip)
                        - continue
                    - else:
                        - add the string to the output array
                - return joined output array as string.
        """

        # TC: O(n) / SC: O(n)
        stack = []  # SC: O(n)
        invalid_pos = set()  # SC: O(n)
        # capture invalid positions and store any remaining parenthesis
        for i, c in enumerate(s):  # TC: O(n)
            if c == "(":
                stack.append(i)
            if c == ")":
                if stack:
                    stack.pop()
                else:
                    invalid_pos.add(i)

        # get the position of all remaining characters in invalid_pos
        invalid_pos = invalid_pos.union(set(stack))

        output = []
        for i, c in enumerate(s):  # TC: O(n)
            if i in invalid_pos:
                continue

            output.append(c)

        return "".join(output)


class Solution1:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Note:
            - Valid parentheses:
                - empty string
                - contains only lower case english char
                - string A and B can be concatenated where A and B are valid strings
                - a valid string sits between ( and )
        Intuition:
            - Use stack to keep track of parenthesis and set to remember invalid position:
                - iterate on s
                    - if opening parenthesis, push to stack
                    - if closing parenthesis,
                        - if stack is non-empty:
                            - pop the top of the stack
                        - else:
                            add (c, i) pair to the invalid position set
                - while stack has remaining open parenthesis (to be removed)
                    - pop the stack and add the position of the invalid parenthesis to the invalid set
                - iterate from s again
                    - if i in invalid position (invalid character, so skip)
                        - continue
                    - else:
                        - add the string to the output array
                - return joined output array as string.
        """

        # TC: O(n) / SC: O(n)
        stack = []  # SC: O(n)
        invalid_pos = set()  # SC: O(n)
        # capture invalid positions and store any remaining parenthesis
        for i, c in enumerate(s):  # TC: O(n)
            if c == "(":
                stack.append(i)
            if c == ")":
                if stack:
                    stack.pop()
                else:
                    invalid_pos.add(i)

        # get the position of all remaining characters in invalid_pos
        while stack:  # TC: O(n)
            pos = stack.pop()
            invalid_pos.add(pos)

        output = []
        for i, c in enumerate(s):  # TC: O(n)
            if i in invalid_pos:
                continue

            output.append(c)

        return "".join(output)


solution = Solution2()
start_time = time.time()
print(solution.minRemoveToMakeValid("lee(t(c)o)de)"))
print("--- %s seconds ---" % (time.time() - start_time))
