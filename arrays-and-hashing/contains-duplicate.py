from typing import List


def hasDuplicate(nums: List[int]) -> bool:
    # iterate over the array list
        # create a hashmap which stores List indicies as key
        # check if the key exists in hashmap
            # if exists, return true
            # otherwise, continue checking
    # return false

    hashMap = set()
    for num in nums:
        if num in hashMap:
            return True
        hashMap.add(num)
        
    return False


print(hasDuplicate([1,2,3,3]))
print(hasDuplicate([1,2,3,4]))