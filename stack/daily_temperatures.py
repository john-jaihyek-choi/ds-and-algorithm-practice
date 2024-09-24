from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
from operator import add, sub, mul, truediv
import time

# Valid Solution 1:
    # Brainstorm:
        # instead of popping all of the items in the temp:
            # I can pop the temp_index only as long as the top of the stack temperature is less than currently visiting temperature
                # This way, I can compute and eliminate the indicies that are smaller than the current value while retaining the values in the past that are great
                    # if there's item left over in the temp_index, it would indicate that those items never had future temperature greater than itself
    # Pseudocode:
        # initialize a res stack to store the results
            # initialize each index with a value of 0 expanding to length of the temperatures
                # for easy access to the specific index of the past and current temperature
        # initialize an empty temp_index stack to store the indicies of the temperatures
        # iterate the temperatures array
            # while temp_index has value AND the value off the last item in the temp_index stack is less than value of temperatures at i
                # calculate the difference of days by subtracting i (current day) by last item in the temp_index
                # set res at the value of last item in the temp_index to days
                # pop the item from the temp_index stack
            # append i to temp_index
        # return res stack


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