from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
from operator import add, sub, mul, truediv
import time

# Solution 3 - using the return value of the pop operation (TC: O(n) SC: O(n)):
class Solution3:
    def __init__(self) -> None:
        pass

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid_operands = ["+", "-", "/", "*"]
        operations = {
            "+": add,
            "-": sub,
            "/": truediv,
            "*": mul
        }

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if stack and token in valid_operands:
                right_operand = stack.pop()
                left_operand = stack.pop()

                result = int(operations[token](left_operand, right_operand))

                stack.append(result)
                continue

            stack.append(int(token))
        
        return stack[-1]

# Solution 2 - operator library approach for less line of code (TC: O(n) SC: O(n)):
class Solution2:
    def __init__(self) -> None:
        pass

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid_operands = ["+", "-", "/", "*"]
        operations = {
            "+": add,
            "-": sub,
            "/": truediv,
            "*": mul
        }

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if stack and token in valid_operands:
                left_operand, right_operand = int(stack[-2]), int(stack[-1])
                result = int(operations[token](left_operand,right_operand))

                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[-1]

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

class Solution1: # (TC: O(n) / SC: O(n))
    def __init__(self) -> None:
        pass

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        valid_operands = ["+", "-", "/", "*"]

        if len(tokens) == 1: # O(1)
            return int(tokens[0])

        for token in tokens: # O(n)
            if stack and token in valid_operands:
                left, right = int(stack[-2]), int(stack[-1]) # O(1)

                if token == "+": # O(1)
                    left += right
                elif token == "-": # O(1)
                    left -= right 
                elif token == "*": # O(1)
                    left *= right
                elif token == "/": # O(1)
                    left /= right

                stack.pop() # O(1)
                stack.pop() # O(1)
                stack.append(left) # O(1)
            else:
                stack.append(int(token)) # O(1)
        
        return stack[-1]
    

solution1 = Solution1()
solution2 = Solution2()
solution3 = Solution3()
start_time = time.time()
print(solution3.evalRPN(["4","13","5","/","+"]))
print("--- %s seconds ---" % (time.time() - start_time))
