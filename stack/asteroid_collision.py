from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 735:
class Solution2:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 2nd Try:
        # use of while/else for better readability and cleaner code
        state = []
        for cur in asteroids: # O(n)
            while state and cur < 0 and state[-1] > 0: # O(1)
                incoming = state[-1]
                if abs(incoming) < abs(cur): # O(1) per amotized analysis because asteroid element is pushed and popped AT MOST once during the entirety of the execution
                    state.pop()
                    continue
                if abs(incoming) == abs(cur): # O(1)
                    state.pop()
                break
            else:
                state.append(cur) # O(1)
        
        return state # O(1)
    
class Solution1:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Rules of collision:
            # value of asteroids[i] represents the size of the asteroid
            # sign of asteroids[i] (+/-) represents the direction of the asteroid moving towards
            # Assuming the asteroid is moving in a 2d space row with only possible direction of left and right
            # bigger sized asteroid dominates the smaller asteroid when colliding
            # Asteroids are moving in a same speed.
                # This guarantees that the asteroids moving to the same direction never collides
        # input:
            # asteroids: List[int]
        # goal: return the output, array, that contains the state after all collisions
        # Brainstorm:
            # stack approach:
                # store the state of the asteroids in each iteration
                # iterate on the asteroids array:
                    # in each iteration, check if the asteroids[i] is negative
                        # if negative and the previous asteroid (top of stack) is positive, it's collision
                            # take the bigger of the two and store leave it at the top of the stack
        # Variable:
            # state: List[int]
        # Pseudocode:
            # initialize an empty array to be used as a stack (state)
            # iterate on the asteroids (cur = asteroids[i])
                # if state AND cur < 0 (negative) AND state[-1] > 0 (positive): [COLLSION]
                    # while state is non-empty AND abs(state[-1]) < abs(cur): [size of cur is dominant over size of prev]
                        # state.pop()
                    # if state is non-empty AND state[-1] == abs(cur):
                        # state.pop()
                        # continue
                    # if state is non-empty AND state[-1] > abs(cur):
                        # continue
                # append cur to the state
            # return state
        
        # TC: O(n) / SC: O(n)
        state = []
        for cur in asteroids: # O(n)
            if state and cur < 0 and state[-1] > 0: # O(1)
                while state and state[-1] > 0 and abs(state[-1]) < abs(cur): # O(1) per amotized analysis because asteroid element is pushed and popped AT MOST once during the entirety of the execution
                    state.pop()

                if state and state[-1] == abs(cur): # O(1)
                    state.pop()
                    continue
                if state and state[-1] > abs(cur): # O(1)
                    continue

            state.append(cur) # O(1)
        
        return state # O(1)


solution = Solution2()
start_time = time.time()
print(solution.asteroidCollision([-2,-1,1,-2]))
print("--- %s seconds ---" % (time.time() - start_time))