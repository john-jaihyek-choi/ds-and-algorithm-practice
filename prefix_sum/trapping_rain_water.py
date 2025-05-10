from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Intuition:
            Prefix and Suffix Sum:
                - initialize lmax and rmax
                - iterate the height array from start to end and append prefix sum
                - iterate the height array from start to end and append suffix sum
                - iterate len(height) many times:
                    - compute water at ith position by min(lmax[i], rmax[i]) - height[i]
                        - Note: at every ith position, water can only be as tall as min of left max or right max
                            - subtracting min value by height would give actual water level
            Two-pointer:
                - initialize l and r pointers
                - initialize l_max and r_max will store the max value at each ends as l and r moves
                - move smaller of l or r pointers
                - after each move compute how much water can fit by...
                    - compute l_max = max(l_max/r_max, height[l/r])
                    - add the result to res sum
        """

        # Prefix and Suffix sum
        # TC: O(n) / SC: O(n)
        lmax, l_max = [], 0  # SC: O(n)
        for i in range(len(height)):  # TC: O(n)
            lmax.append(l_max)
            l_max = max(height[i], l_max)

        water = r_max = 0
        for i in range(len(height) - 1, -1, -1):  # TC: O(n)
            water += max(min(lmax[i], r_max) - height[i], 0)
            r_max = max(height[i], r_max)

        return water


solution = Solution()
start_time = time.time()
print(solution.trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
print("--- %s seconds ---" % (time.time() - start_time))
