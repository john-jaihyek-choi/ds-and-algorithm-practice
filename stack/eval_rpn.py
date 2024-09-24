from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time


# Solution 1:
    # Pseudocode:
        # initialize an empty array to store the arithmetic value
        # if length of token == 1, return the first time in tokens array
        # iterate the tokens list
            # if stack is valid and token (token[current_index]) is a valid operand
                # retrieve the last 2 items for:
                    # left operand
                    # right operand
                # if token == +
                    # left operand + right operand
                # if token == -
                    # left operand - right operand
                # if token == *
                    # left operand * right operand
                # if token == /
                    # left operand * right operand
            # pop top 2 items from stack
            # append the arithmetic expression value of left and right to the stack
        # otherwise
            # append token to stack
        # return the last item from the stack

class Solution:
    def __init__(self) -> None:
        pass

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid_operands = ["+", "-", "/", "*"]

        if len(tokens) == 1:
            return tokens[0]

        for token in tokens:
            if stack and token in valid_operands:
                left, right = int(stack[-2]), int(stack[-1])

                if token == "+":
                    left += right
                elif token == "-":
                    left -= right
                elif token == "*":
                    left *= right
                elif token == "/":
                    left /= right

                stack.pop()
                stack.pop()
                stack.append(left)
            else:
                stack.append(token)
        
        return stack[-1]
    

solution = Solution()
start_time = time.time()
print(solution.evalRPN(["4","13","5","/","+"]))
print("--- %s seconds ---" % (time.time() - start_time))
