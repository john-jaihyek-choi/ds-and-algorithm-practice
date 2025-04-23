from typing import List


class Solution1:
    def twoSum(nums: List[int], target: int) -> List[int]:
        """
        # create a hash map to store the compliment number at each index of nums
        # create a list to store the sum match
        # calculate compliment (target - nums[i]) each iteration
            # if compliment exists in the hash map created
                # push the two numbers (small to large) to the sum match list
                # return the list
            # return
        """
        compliment_map = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in compliment_map:
                return [compliment_map[compliment], i]

            compliment_map[num] = i


class Solution2:
    def twoSum(nums: List[int], target: int) -> List[int]:
        # WONT WORK FOR THIS SPECIFIC QUESTION SINCE RETURN VALUE SHOULD BE INDICIES PAIR RATHER THAN THE VALUES
        nums.sort()
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                return [l, r]


solution = Solution2()
print(solution.twoSum([3, 4, 5, 6], 7))
print(solution.twoSum([4, 5, 6], 10))
