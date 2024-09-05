from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

def longestConsecutive(nums: List[int]) -> int:
    # Brainstorm:
        # How can we know if a number is the beginning of the sequence?
            # if the nums[i] - 1 value does not exist in a set, then it means the number is the beginning of a sequence
        # How can we quickly search (O(1) time) if nums[i] - 1 exists?
            # convert the input list to set
                # Potential concern - does eliminating the duplicate values affect the outcome?
                    # No, because, regardless of how many identical numbers we get, it won't be added as consecutive count since it's the same number
    
    # Pseudocode:
    # convert the input list to set and store it in a variable for quick search (nums_set)
    # intialize the longest_consecutive at 0 to store the longest_consecutive as iterating the input array (longest_consecutive)
    # iterate over the input list
        # check if nums[i]-1 doesn't exist in a set instantiated above (nums_set)
            # if True
                # check if nums[i] + x (x starting at 1) exists in nums_set 
                    # Repeat while nums[i] + (x+=1) exists in nums_set
                # check the value of x (we'll call this 'consecutive') is greater than longest_consecutive
                    # if True
                        # replace longest_consecutive
        # after the completion of the loop, return the longest_consecutive variable
                

    # Solution 1 
    # nums_set = set(nums)

    # longest_consecutive = 0

    # for i in range(len(nums)):
    #     consecutive = 1
        
    #     if (nums[i] - 1) not in nums_set: # checking for start of a sequence  
    #         while nums[i] + consecutive in nums_set: # checking for continuous sequence while found
    #             consecutive += 1
            
    #     if longest_consecutive < consecutive:
    #         longest_consecutive = consecutive
    
    # return longest_consecutive
    
    # Solution 2 (Same concept, cleaner)
    nums_set = set(nums)
    longest_consecutive = 0

    for i in range(len(nums)):
        
        
        if (nums[i] - 1) not in nums_set: # checking for start of a sequence  
            consecutive = 1

            while nums[i] + consecutive in nums_set: # checking for continuous sequence while found
                consecutive += 1
            
            longest_consecutive = max(consecutive, longest_consecutive)
    
    return longest_consecutive

start_time = time.time()
print(longestConsecutive([2,20,4,10,3,4,5]))
print(longestConsecutive([0,3,2,5,4,6,1,1]))
print("--- %s seconds ---" % (time.time() - start_time))