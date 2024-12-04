from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 735:
class Solution3:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Input:
            # asteroids: List[int]
                # asteroids[i] represents asteroid
                    # abs(asteroids[i]) = size of the asteroid
                    # positive/negative asteroids[i] = direction the asteroid is moving towards
        # Output:
            # output: List[int]
                # output[i] is remaining asteroids
        # Goal:
            # given a list of integers, asteroids, return the output array that contains the remaining asteroids AFTER all possible collisions
        # Collision Rule:
            # 1. Collision occurs when asteroid[i] is + and asteroid[j] is - (or vice versa)
            # 2. when collision occurs, bigger asteroid between abs(asteroid[i]) or abs(asteroid[j]) explodes
            # 3. when collision occurs and abs(asteroid[i]) == abs(asteroid[j]), then both asteroids explode
        # Ideas:
            # Intuition (stack approach):
                # use a stack to store the asteroid that survived the collision (or no collision) (remaining_asteroids)
                # iterate on asteroids array:
                    # incoming_asteroid = asteroids[i]
                    # while remaining_asteroids is non-empty
                        # AND remaining_asteroids[-1] is positive and incoming_asteroid is negative
                            # assuming:
                                # left = remaining_asteroid[-1]
                                # right = abs(incoming_asteroid)
                            # if left > right:
                                #  break out of the loop
                            # if left < right:
                                # remaining_asteroids.pop()
                            # if left == right:
                                # remaining_asteroids.pop()
                                # break

        # TC: O(n) / SC: O(n)
        remaining_asteroids = []
        for incoming_asteroid in asteroids:
            while remaining_asteroids and remaining_asteroids[-1] > 0 and incoming_asteroid < 0:
                left, right = remaining_asteroids[-1], abs(incoming_asteroid)
                if left > right:
                    break
                else:
                    remaining_asteroids.pop()
                    if left == right:
                        break
            else:
                remaining_asteroids.append(incoming_asteroid)
        
        return remaining_asteroids

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