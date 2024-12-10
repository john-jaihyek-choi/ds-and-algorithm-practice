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
        
        # TC: O(n^2 * k)
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

        # More efficient approach:
        # Sort then sum up the differences
        # TC: O(nlogn) / SC: O(1)
        moves = 0
        nums.sort(reverse=True)
        maximum, minimum = nums[0], nums[-1]

        for n in nums:
            moves += n - minimum
        
        return moves

        # # better readability and performance:
        # # sum and min using built-in function then calculating the minimum with formula
        #     # Explanation:
        #         # incrementing n - 1 is mathematically equivalent to decrementing MAX value by 1 in terms of relative gap between max and min (max - min) at each level
        #             # ex) incrementing n - 1 elements by 1
        #             # [1, 2, 3]
        #                 # incrementing n - 1 elements by 1:
        #                     #             [1, 2, 3] -> [2, 3, 3] -> [3, 3, 4] -> [4, 4, 4]
        #                     # max - min                    1            1            0
        #             # ex) decrementing max(nums) by 1
        #             # [1, 2, 3]
        #                 # decrementing max element by 1:
        #                     #             [1, 2, 3] -> [1, 2, 2] -> [1, 2, 1] -> [1, 1, 1]
        #                     # max - min                    1            1            0
        #         # So, regardless of the length and the values in the nums array, the changes to the gap between max - min would ALWAYS equal to 1.
        #         # And because above holds true, each operation == 1 move
        #             # Therefore... nums_sum - (min * len(nums)) = minimum required moves

        # TC: O(n) / SC: O(1)
        moves = 0
        nums_sum = sum(nums)
        minimum = min(nums)

        return nums_sum - (minimum * len(nums))


solution = Solution()
start_time = time.time()
answer = solution.minMoves([1,1000000000])
print(answer)
print("--- %s seconds ---" % (time.time() - start_time))
