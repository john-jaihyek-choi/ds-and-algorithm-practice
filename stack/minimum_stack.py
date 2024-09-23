from collections import deque
from typing import List, Dict, DefaultDict, Set

# Solution #2 Another way to approach the problem:
class MinStack:
    def __init__(self):
        self.stack: List[tuple[int, int]] = []

    def push(self, val: int) -> None:
        min_val = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append([val, min_val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Solution #1:
    # Note:
        # all operations must be completed within O(1) time

    # Pseudocode:
        # initialize an empty list for stack and main_stack in the constructor:
            # stack will store the value of each items in stack
            # min_stack will store the value of the minimum value at each point in time (index)
        # push:
            # append the val to the stack array
            # set min_val which stores minimum value of val or the value at the top of the min_stack
                # if min_stack is empty, use val
            # append the min_val to the min_stack array
        # pop:
            # pop the stack
            # pop the min_stack
        # top:
            # return the item at the top of the stack
        # getMin:
            # return the item at the top of the min_stack

# class MinStack:

#     def __init__(self):
#         self.stack = []
#         self.min_stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#         min_val = min(val, self.min_stack[-1] if self.min_stack else val)
#         self.min_stack.append(min_val)

#     def pop(self) -> None:
#         self.stack.pop()
#         self.min_stack.pop()

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.min_stack[-1]

minStack = MinStack()

print(minStack.push(1),
minStack.push(2),
minStack.push(0),
minStack.getMin(),
minStack.pop(),
minStack.top(),
minStack.getMin())