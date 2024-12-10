import math
from typing import List
import time

# Leetcode: 3190
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Input:
            # nums: List[int]
        # Output:
            # output: List[int]
        # Goal:
            # given a list of integers, nums, return the minimum number of operations to make all elements of nums divisble by 3
        # Note:
            # target: nums[i] being divisible by 3
                # nums[i] % 3 == 0
                    # if nums[i] % 3 == 1:
                        # I can decrement 1 (1 operation) to get 0 which makes it divisible by 3
                    # if nums[i] % 3 == 2:
                        # I can increment 1 (1 operation) to get to 3 which makes it divisible by 3
                # Above shows that if nums[i] % 3 != 0, the minimum operation required to make the number divisible by 3 is 1
        # Ideas:
            # iterate on nums:
                # compute the nums[i] modulo 3:
                # if nums[i] % 3 is not 0, increment the moves counter
        # Pseudocode:
            # initialize a counter:
                # moves = 0
            # iterate on the nums array (i = index):
                # if nums[i] % 3 != 0:
                    # moves += 1
            # return moves

        # TC: O(n) / SC: O(1)
        moves = 0

        for i in range(len(nums)):
            if nums[i] % 3 != 0:
                moves += 1

        return moves
                

solution = Solution()
start_time = time.time()
answer = solution.minimumOperations([1,2,3])
print(answer)
print("--- %s seconds ---" % (time.time() - start_time))
