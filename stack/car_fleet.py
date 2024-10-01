from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
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

# Solution 2: using stack append/pop TC: O(n log n) / SC: O(n)
class Solution2:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

# Solution 1:
    # brainstorm:
        # to calculate the time that the first (last in the position array) reaches the destination:
            # miles remaining / speed of the vehicle:
                # miles remaining = target - position[i]
                # speed of the vehicle = speed[i]
        # how to group the fleet?
            # when does group of cars become fleet?
                # when car behind it reaches the car ahead of it
                    # if:
                        # times remaining of the car behind is less than the times remaining of the car in front
        # where should I iterate the car from?
            # from the 1st car to the last possible car (based on the position)
                # in order to iterate based on rank, the items will need to be sorted in reverse order (O(n log n) operation), lowest to highest position
                    # ex: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
                    #                               2  1  0  3
                    # reverse sorted by position = [0, 1, 4, 7]
        # what variables and items needed to compute time remaining?
            # position, position[i], is needed
            # speed, speed[i], is needed
            # target is needed
            # distance_remaining = target - position[i]
            # time_remaining = distance_remaining / speed[i]
        #  Ways to make the access to speed and position easy and quick?
            # use zip() to couple position[i] and speed[i] in iterable tuple format
                # ex: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
                # unsorted: [ (4, 2), (1, 2), (0, 1), (7, 1) ]
                # reverse sorted: [ (0,1), (1,2), (4,2), (7,1) ]
        # Grouping the fleets together:
            # starting from the top of the stack:
                # start iterating and checking
                    # if the time remaining is less than or equal to current remaining time group
                        # if true, then pop the item from stack
                        # if false, then re-calculate the remaining time group again
        
    # Pseudocode:
        # initialize an empty stack to store the car fleet (car_fleet)
        # zip the position and speed, position being the main item (road)
        # sort the road list
        # start itererating the road from the end of the array (index = i)
            # car = road[i]
            # compute time_remaining
                # time_remaining = (target - car[0]) / car[1]
            # check if car_fleet has an item and the value at the top of the stack is greater than or equal to the time_remaining of the car at i
                # if true
                    # continue the loop
                # else
                    # append the time_remaining to the car_fleet
        # return the length of the car_fleet

# TC: O(n log n) / SC: O(n)
class Solution1:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = [] # O(1)
        road = list(zip(position, speed)) # O(n)
        road.sort() # O(n log n)

        for i in range(len(road) - 1, -1, -1): # O(n)
            car = road[i] # O(1)
            time_remaining = (target - car[0]) / car[1] # O(1)

            if car_fleet and car_fleet[-1] >= time_remaining: # O(1)
                continue
            car_fleet.append(time_remaining) # O(1)

        return len(car_fleet) # O(1)
    

solution = Solution1()
start_time = time.time()
# Example:
    # Input: target = 10, position = [1,4], speed = [3,2]
    # Output: 1
print(solution.carFleet(10, [4,1,0,7], [2,2,1,1]))
print("--- %s seconds ---" % (time.time() - start_time))