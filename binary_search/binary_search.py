from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

class Solution2: # alternative way to calculate mid point in case of overflow
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1
    
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1
    

solution = Solution1()
start_time = time.time()
print(solution.search([-1,0,2,4,6,8], 0))
print("--- %s seconds ---" % (time.time() - start_time))