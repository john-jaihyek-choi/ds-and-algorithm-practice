from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # create a hash map to store the compliment number at each index of nums
    # create a list to store the sum match
    # calculate compliment (target - nums[i]) each iteration
        # if compliment exists in the hash map created
            # push the two numbers (small to large) to the sum match list
            # return the list

    # return 
    compliment_map = {}

    for i, num in enumerate(nums):
        compliment = target - num

        if compliment in compliment_map:
            return [compliment_map[compliment], i]
        
        compliment_map[num] = i



print(twoSum([3,4,5,6], 7))
print(twoSum([4,5,6], 10))