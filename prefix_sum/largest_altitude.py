import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 1732:
class Solution2:
    def largestAltitude(self, gain: List[int]) -> int:
        # Note:
            # input:
                # gain: List[int]
            # output:
                # output: int
            # goal:
                # given list of integers, gain, where gain[i] represents the net gain in altitude between i and i+1
                    # return the highest altitude of a point
        # edge-case:
            # all 0's:
                # return 0 since 0 would be the height altitude
            # no trip:
                # 1 <= n <= 100
            # all negative gain[i]
                # return 0 since starting point would be the height altitude a biker has visited
        # idea:
            # initial thought:
                # keep track of altitude points
                    # altitude starts 0
                    # altitude + or - gain[i]
                # keep track of the highest altitude point
                # TC: O(n) / SC: O(1)

        # pseudocode:
        # initialize an altitude and max_altitude at 0
        # iterate the gain array (i = index, g = gain[i])
            # altitude += g
            # max_altitude = max(max_altitude, altitude)
        # return max_altitude

        altitude = max_altitude = 0
        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)
        
        return max_altitude
        
        # possibility of optimization:
            # opportunity terminate early?
                # No, I'll have to iterate the entire gain for me to get the highest possible altitude
            # opportunity not use variable for max_altitude?
                # No, max_altitude and altitude must be kept distinct
            # No possible ways to improve this operation



class Solution1:
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


solution = Solution2()
start_time = time.time()
print(solution.largestAltitude([-5,1,5,0,-7]))
print("--- %s seconds ---" % (time.time() - start_time))