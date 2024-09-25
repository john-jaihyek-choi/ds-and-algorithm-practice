from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
from operator import add, sub, mul, truediv
import time

# Note:
    # n = number of cars traveling to a destination in ONE-LANE highway
        # Car CANNOT pass another car ahead of it, it can only catch up to another car, then drive at the same speed as the car ahead of it
    # position = position of the ith car (in MI)
    # speed = speed of the ith car (in MI/hr)
    # len(position) == len(speed) == n
    # destination is == target (in MI)
    # car fleet are non-empty set of cars driving at the same position and same speed; Single car is also considered a car fleet
        # ex) { 1, 2, 3 }
        # ex2) { 1 }
    # if car catches up to a car fleet the moment the fleet reaches the destination, then the car IS PART of the fleet
    # Return the number of different car fleets that will arrive at the destination
    

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        return 0
    

solution = Solution()
start_time = time.time()
# Example:
    # Input: target = 10, position = [1,4], speed = [3,2]
    # Output: 1
print(solution.carFleet(10, [1, 4], [3, 2]))
print("--- %s seconds ---" % (time.time() - start_time))