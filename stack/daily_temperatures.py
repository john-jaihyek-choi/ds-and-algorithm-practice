from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
from operator import add, sub, mul, truediv
import time

# Retried 10/24/2024: Leetcode 739
class Solution3:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # input:
            # temperatures: List[int]
                # temperatures[i] = temperature on i'th day
        # goal:
            # return an array, answer, where answer[i] is the number of days needed to wait until the weather gets warmer
                # ex)  [32, 31, 30, 38]
                # then [ 3,  2,  1,  0]
        # Brainstorm:
            # Bruteforce:
                # iterate the temperatures array where i = index
                    # iterates teperatures array where j = i + j
                        # if temperature[j] > temperatures[i], then j - i = days
            # Optimal Solution:
                # Monotonic Decreasing stack:
                    # ex) stack = [ 73, ]
                        # instead of storing the temperature directly, store the index to the temperature
                            # ex) stack = [ 0, ]
                            # In order for us to use the index and store the ith day, I'll have concept similar to array hashing
                                # initialize a stack with an empty 0 where the length, n, is equal to the length of the temperatures
        # Variable:
            # answer: List[int]
                # answer[i] = number of days
            # temp_stack: List[int]
                # temp_stack[i] = temperatures's index
        # Pseudocode:
            # initialize an empty stack
                # initialize with a default value of 0 and extend the array to the length of the temperatures array
                    # ex) n = 3; [ 0, 0, 0 ]
            # for i, temp in enumerate(temperatures):
                # while temp_stack and temperatures[stack[-1]] < temp:
                    # compute days between temperature at stack[-1] index:
                        # previous_day = stack.pop()
                        # days = i - previous_day
                        # answer[previous_day] = days
                # answer.append(i)
            # return stack

        # Overall TC: O(n) / SC: O(n)
        answer = [0] * len(temperatures)
        temp_stack = []

        for i, temp in enumerate(temperatures): # O(n)

            while temp_stack and temperatures[temp_stack[-1]] < temp: # O(1)
                previous_day = temp_stack.pop()
                days = i - previous_day
                answer[previous_day] = days

            temp_stack.append(i) # O(1)

        return answer

class Solution2: # TC: O(n) SC: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp_index = []

        for i in range(len(temperatures)): # O(n)
            while temp_index and temperatures[temp_index[-1]] < temperatures[i]: # O(1)
                days = i - temp_index[-1] # O(1)
                res[temp_index[-1]] = days # O(1)
                temp_index.pop() # O(1)
            
            temp_index.append(i) # O(1)

        return res
    
# Initial try (INVALID SOLUTION):
    # partially working solution.
        # invalid due to the way that the counters are adding/subtracting conflicting with the while loop
        # ALSO:
            # it is unnecessary to pop and go back to the first (bottom most) item in the stack
    # Brainstorm:
        # using indicies of the temperatures array instead of the value could help:
            # compute the days easier (past_i - current_i)
class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp = []

        i = 0
        while i < len(temperatures):

            if temp and temperatures[temp[0]] < temperatures[i]:
                res[temp[0]] = i - temp[0]

                while temp:
                    i = temp.pop() + 1

            temp.append(i)
            i += 1

        return res

solution = Solution1()
start_time = time.time()
print(solution.dailyTemperatures([30,38,30,36,35,40,28]))
print("--- %s seconds ---" % (time.time() - start_time))