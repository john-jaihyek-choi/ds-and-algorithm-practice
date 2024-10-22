import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 1732:
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # input:
            # gain: List[int]
                # gain[i] represents the net gain (or loss) in altitude between i and i + 1 point
        # goal: return the highest altitude of a point
            # highest altitude = max altitude value at gain[i]
        # Note:
            # biker begins at 0 altitude
            # I need to track the actual altitude based on the net gain/los in altitude at each i
                # track the altitude at each point
        # Variable:
            # max_altitude: int
            # cur_altitude: int
        # Pseudocode:
            # initialize the max_altitude at 0
            # initialize the cur_altitude at 0
            # iterate the gain array (i = index, change_in_altitude = gain[i])
                # cur_altitude += change_in_altitude
                # max_altitude = max(max_altitude, cur_altitude)
            # return max_altitude
        
        # TC: O(n) / SC: O(1)
        max_altitude, cur_altitude = 0, 0 
        for i, change_in_altitude in enumerate(gain):
            cur_altitude += change_in_altitude
            max_altitude = max(max_altitude, cur_altitude)
        return max_altitude


solution = Solution()
start_time = time.time()
print(solution.largestAltitude([-5,1,5,0,-7]))
print("--- %s seconds ---" % (time.time() - start_time))