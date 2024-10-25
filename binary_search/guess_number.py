from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
pick =  10

class Solution:
    def guess(self, n: int) -> int:
        global pick
        if n > pick:
            return -1
        elif n < pick:
            return 1
        else:
            return 0

        
    def guessNumber(self, n: int) -> int:
        # input:
            # n: int
                # pool of the total number to guess the number from
            # pick: int
                # the number the another person picked
        # goal:
            # return the number that the other person picked
        # Brainstorm:
            # I know that there is going to be n numbers to choose from
            # if I guess wrong, I get a response telling me whether the "picked" number is lower or greater
                # guess API is available
                    # param:
                        # num: int
                            # the number I'm guessing
            # Since every guess, I get back a response, I can strategize by going lower or upper based on the response of the guess API
        # Bruteforce:
            # guess from 1 all the way to n
            # O(n), but inefficient since I'm not optimally using the benefit of the guess API
        # Binary Search approach:
            # Guess the middle number to start with:
                # if guess API response = -1, I need to check the left half
                # if guess API response = 1, I need to check the right half
                # if guess API response = 0, I guessed correctly
            # repeat this every guess, then I'll eventually get to an answer
        # Pseudocode:
            # l = 1
            # r = n
            # while l <= r:
                # m = (l + r) // 2
                # if guess(m) == 0:
                    # return m
                # elif guess(m) == 1:
                    # l = m + 1
                # elif guess(m) == -1:
                    # r = m - 1
            # return 0
        l, r = 1, n
        while l <= r:
            my_guess = (l + r) // 2
            if self.guess(my_guess) == 0:
                return my_guess
            elif self.guess(my_guess) == 1:
                l = my_guess + 1
            elif self.guess(my_guess) == -1:
                r = my_guess - 1
        return 0


        # quicker runtime with use of binary shift and walrus operator
        l, r = 1, n
        # >> (bitwise shift) shifts the binary by factor of 2 which mimics the behavior of division
            # note: >> can only be used to when dividing by even. It can't be used to divide by odd number since each shift by factor of 2
        my_guess = (l + r) >> 1
        # := (walrus operation) allows assignment of variable within expression
        while (res := self.guess(my_guess)) != 0:
            if res == 1:
                l = my_guess + 1
            else:
                r = my_guess - 1
            my_guess = (l + r) >> 1
        return my_guess
    

solution = Solution()
start_time = time.time()
print(solution.guessNumber(10))
print("--- %s seconds ---" % (time.time() - start_time))