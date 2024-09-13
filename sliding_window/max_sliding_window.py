from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    # Solution 1 Bruteforce (TC: O(n^2) / SC: O(n)) 
    output = []
    l = 0

    for r in range(k, len(nums) + 1): # O(n)
        output.append(max(nums[l:r])) # O(n)
        l+=1

    return output


start_time = time.time()
print(maxSlidingWindow([1,2,1,0,4,2,6], 3))
print("--- %s seconds ---" % (time.time() - start_time))
