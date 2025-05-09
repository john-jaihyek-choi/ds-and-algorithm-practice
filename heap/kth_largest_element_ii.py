from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import math
import time
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Intuition:
            - Max Heap:
                - heapify nums
                - while k > 0:
                    - heappop from the heapq
                    - decrement k
            - Min Heap:
                - heapify nums
                - while len(min_heap) > k:
                    heapq.heappop(min_heap)
            - Use built-in nlargest:
                - use heapq.nlargest()
        """
        # Max Heap
        # # TC: O(n + k log n) / SC: O(n)
        max_heap = [-n for n in nums]  # TC: O(n) / SC: O(n)
        heapq.heapify(max_heap)  # TC: O(n)

        res = abs(max_heap[0])
        while k > 0:  # TC: O(k)
            res = heapq.heappop(max_heap)  # TC: O(log n)
            k -= 1

        return -res

        # Min Heap
        # # TC: O(n - k log n) / SC: O(1)
        heapq.heapify(nums)  # TC: O(n)

        while len(nums) > k:  # TC: O(n - k)
            heapq.heappop(nums)  # TC: O(log n)

        return heapq.heappop(nums)  # TC: O(log n)

        # Builtin heapq.nlargest
        # TC: O(n log k) / SC: O(k)
        return heapq.nlargest(k, nums)[-1]


start_time = time.time()
solution = Solution()
print(solution.findKthLargest([2, 3, 1, 5, 4], 2))
print("--- %s seconds ---" % (time.time() - start_time))
