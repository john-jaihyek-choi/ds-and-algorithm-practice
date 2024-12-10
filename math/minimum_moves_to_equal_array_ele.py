import math
from typing import List
import time

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Input:
            # nums: List[int]
        # Output:
            # output: int
        # Goal:
            # given list of integers, nums, return the minimum number of moves required to make all array elements equal
                # condition:
                    # I can only increment n - 1 elements of the array by 1
        # Note:
            # Can I decrement the number?
                # No
            # How would I be able to find the mininmum required moves?
                # I need to first understand what numbers are in nums (O(n) at minimum)
        # [1, 2, 3]
        # [2, 3, 3]
        # [3, 4, 3]
        # [4, 4, 4]

        # Ideas:
            # Bruteforce:
                # scan for min and max value
                # increment every element by 1 except the max element
                # repeat until max element == min element
        
        # Pseudocode:
            # 1. iterate while max != min
                # while max != min
                # 1. find min and max index
                    # nums.index(min(nums))
                    # nums.index(max(nums))
                # 3. iterate and increment nums[i] EXCEPT the max element
                    # for i in range(len(nums)):
                        # if i != max_idx:
                        #     nums[i] += 1
        
        moves = 0
        while True:
            min_idx = nums.index(min(nums))
            max_idx = nums.index(max(nums))

            if nums[max_idx] == nums[min_idx]:
                    return moves

            for i in range(len(nums)):
                if i != max_idx:
                    nums[i] += 1
            
            moves += 1
    


solution = Solution()
start_time = time.time()
answer = solution.minMoves([1,2,3])
print(answer)
print("--- %s seconds ---" % (time.time() - start_time))
