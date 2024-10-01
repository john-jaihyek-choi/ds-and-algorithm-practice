from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Note:
    # a bar can can extend to the right if the height of bar in the right is greater than or equal to height of itself
    # bars to the left of itself can be popped until a bar with lower height is found
        # this allows to extend the area to the left of the current bar

# Solution 1:
    # Pseudocode:
        # initialize an empty stack to store the index and height pair (stack)
        # initialize a max area value to 0 (max_area)
        # iterate the heights array from the 0th index
            # set current index and height pair (index, height[i])
            # while there's an item in the stack AND 1th index of the item on the top of the stack is greater than the current height
                # if true:
                    # calculate the area of the item being popped
                        # width = current index - index of the item being deleted
                        # height = stack[-1][1]
                    # set the max_area between itself and the calculated area
                    # overwrite the index of the pair to the index of the pair deleting
                    # pop the top of the stack
            # append the current index and height pair (index, height[i]) to the stack
        # while stack is non-empty:
            # calculate the area
                # len(heights) - index of the pair * height of the pair
                # set the max_area between itself and the calculated area
                # pop the top of the stack
        # return max_area
        
# TC: O(n * m) where m is length of the stack / SC: O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # O(1)
        max_area = 0 # O(1)

        for i in range(len(heights)): # O(n)
            pair = [i, heights[i]] # O(1)

            while stack and stack[-1][1] >= heights[i]: # O(1) since bar (height[i]) is being popped at most 1 time. It never re-enters the stack
                area = (i - stack[-1][0]) * stack[-1][1] # O(1)
                max_area = max(max_area, area) # O(1)
                pair[0] = stack[-1][0] # O(1)
                stack.pop() # O(1)
            
            stack.append(pair) # O(1)

        while stack: # O(n)
            area = (len(heights) - stack[-1][0]) * stack[-1][1] # O(1)
            max_area = max(max_area, area) # O(1)
            stack.pop() # O(1)

        return max_area # O(1)
    

solution = Solution()
start_time = time.time()
print(solution.largestRectangleArea([2,1,5,6,2,3]))
print("--- %s seconds ---" % (time.time() - start_time))