from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time
from functools import reduce

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:


    # INVALID SOLUTION
        # Brainstorm:
        # Main problems of bruteforce solution that are causing O(n^2)
            # Max function - O(n) operation to find max of a substring
            # Substring retrieval (ex: nums[l:r])
        # What are some parts of a window within a loop we have O(1) access to?
            # where:
                # l is the left edge of the window
                # r is the right edge of the window
            # 1. nums[l] and nums[r] are O(1) access
            # 2. l and r is directly accessible
        # at point L and R, how do we know what is the max value within the given window?
            # Can we tell somehow by looking at nums[L] and nums[R] to determine if there's bigger value contained between it?
                # Logically:
                    # if nums[L] and nums[R] is smaller than whatever the value is between it, the max value between the L and R window is the max value
                    # if nums[L] is greater than nums[R], then nums[L] is the max value
                    # if nums[R] is greater than nums[L], then nums[R] is the max value
            # If we store the left and right max boundary at each given nums[i], then we know exactly what the maximum is with respect to nums[L] and nums[R]
                # ex)
                #  nums  = [  1,  6,  4,  2,  7, 10,  2,  0,  1 ] where k = 3
                #  l_max = [  1,  6,  6,  6,  7, 10, 10, 10, 10 ] max value (including value at i) with respect to values to the left of i
                #  r_max = [ 10, 10, 10, 10, 10, 10,  2,  1,  1 ] max value (including value at i) with respect to values to the right of i
                    # *** NOTE ***
                    # It won't be possible to achieve O(n) as easy as l_max because we need to iterate from the back of the array to 0
                        # In the process, the order in which the right max values get stored in will be reversed
                            # We can use built in sort, but it will be O(n log n)
                        # ** Workaround **
                            # instead of generating r_max, we can start the window to search from the end of the nums array instead of going from 0
                #  output = [ 6, 6, 7, 10, 10, 10, 2]
            # Given the above pattern, we can derive the max value within the L and R by taking the min of l_max[r] and r_max[l]
                # If put in words:
                    # l_max[r] is the largest number at nums[r] with respect to all values to the left of it
                    # r_max[l] is the largest number at nums[l] with respect to all values to the right of it
                    # Visualization:
                        # If l_max[r] = 10 and l_max[r] = 6
                            #   0    1     2     3     4  5  6  7  8
                            #     r_max[l] = 10 -> means the biggest value to the right of it is 10     
                            # [ ?,   6,    ?,    2,    ?, ?, ?, ?, ? ]
                            #                  l_max[r] = 6 -> means the biggest value to the left of it is 6
                        # Based on the above, logic above - since l_max[r] value is 6, we know for sure that any value between 6 and 2 could only ever be 6
        # *** Flaw with the solution ***:
            # When combining the min of the maximums using min(l_max[r], r_max[l]), I'm not necessarily getting the maximum for each sliding window. Instead, I'm computing the minimum of the maximums, which isn't the desired outcome.
                # For each sliding window of size k, I must find the maximum element in that window.
        # Pseudocode:
            # initialize an empty array to store the result (output)
            # initialize l_max list to store the maximum values with respect to nums[i]'s left values (l_max)
            # initialize r_max list to store the maximum values with respect to nums[i]'s right values (r_max)
                # initialize it to empty array with 0s with length of nums
            # set maximum = 0
            # iterate nums array starting from 0
                # compute the maximum
                # collect left max values with respect to nums[i]
            # set maximum = nums[-1]
            # iterate nums array again starting from the end of the array
                # compute the maximum
                # collect right max values with respect to nums[i]
            # initialize the l pointer at 0 (l)
            # iterate the nums array starting at k until the end of the array (r = current index)
                # append the smaller value between l_max[r] and r_max[l] to the output array
                # increment the l by 1

    # INVALID SOLUTION
    if k == 1:
        return nums
    
    output, l_max = [], []
    r_max = [0] * len(nums)

    maximum = 0
    for num in nums:
        maximum = max(maximum, num)
        l_max.append(maximum)

    maximum = nums[-1]
    for i in range(len(nums) - 1, -1, -1):
        maximum = max(maximum, nums[i])
        r_max[i] = maximum

    l = 0
    for r in range(k - 1, len(nums)):
        output.append(min(l_max[r], r_max[l]))
        l += 1

    return output
    
    # Solution 1 Bruteforce (TC: O(n^2) / SC: O(n)) 
    output = []
    l = 0

    for r in range(k, len(nums) + 1): # O(n)
        output.append(max(nums[l:r])) # O(n)
        l+=1

    return output


start_time = time.time()
print(maxSlidingWindow([1,3,1,2,0,5], 3))
print("--- %s seconds ---" % (time.time() - start_time))
