import time
from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Input:
            # boxTypes: List[List[int]]
            # truckSize: int
        # Output:
            # output: int
                # output = maximum total number of units that can be put on the truck
        # Goal:
            # given the 2d array boxTypes and an integer truckSize
                # return the maximum total number of units that can be put on the truck
        # Note:
            # always more optimal to add boxes with the most units
        # Idea:
            # Intuition:
                # sort the boxTypes by the number of units
                # iterate on the boxTypes[i][1] value (units per box)
                    # in each iteration, keep track of remaining box counts (from 0)
                        # if boxTypes[i][0] <= remaining box counts:
                            # compute the product of boxTypes[i][0] and boxTypes[i][1]
                        # else:
                            # compute the product using remaining box count remaining_box_count * boxTypes[i][1]
        # Variables:
            # remaining_box_ct: int
            # max_total_units: int

        # Pseudocode:
            # initialize a remaining_box_count at 0
            # initialize a max_total_units at 0
            # boxTypes.sort(key=lambda x:x[1])
            # iterate on the sorted box type (boxType = boxType[i])
                # if boxType[0] <= remaining_box_ct:
                    # remaining_box_ct += boxType[0] * boxType[1]
                # else:
                    # remaining_box_ct += remaining_box_ct * boxType[1]
            # return max_total_units

        # TC: O(nlogn + n) / SC: O(1)
        remaining_box_ct, max_total_units = truckSize, 0

        boxTypes.sort(key=lambda x:x[1], reverse=True) # O(n logn)
        
        for boxType in boxTypes: # O(n)
            if boxType[0] <= remaining_box_ct:
                max_total_units += boxType[0] * boxType[1]
                remaining_box_ct -= boxType[0]
            else:
                max_total_units += remaining_box_ct * boxType[1]
                break
        
        return max_total_units

        # Cleaner solution - TC: O(nlogn + n) / SC: O(1)
        remaining_box_ct, max_total_units = truckSize, 0

        boxTypes.sort(key=lambda x:x[1], reverse=True) # O(n logn)
        
        for boxes, units in boxTypes: # O(n)
            max_total_units += min(boxes,remaining_box_ct) * units
            remaining_box_ct -= boxes
            if remaining_box_ct <= 0:
                break
        
        return max_total_units

solution = Solution()
start_time = time.time()
answer = solution.maximumUnits([[1,3],[2,2],[3,1]])
print("--- %s seconds ---" % (time.time() - start_time))