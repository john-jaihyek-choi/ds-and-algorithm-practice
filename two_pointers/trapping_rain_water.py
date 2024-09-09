from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

def trap(height: List[int]) -> int:
    # Brainstorm:
        # 1. How can a water be trapped?
            # it is trapped if there are bars (l,r) surrounding it
        # 2. How can we find out the area of the trapped water?
            # min(l, r) * (l - r)
            # This assumes that there are no bars in between the boundary
        # 3. Then how do we know if the boundary currently being looked at is the largest boundary possible?
            # We can compute the max left and max right value ahead of times at each index
                #  ex) Given the height = [0,2,0,3,1,0,1,3,2,1]
                #           i  [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
                #     max left [ 0, 0, 2, 2, 3, 3, 3, 3, 3, 3 ]
                #    max right [ 3, 3, 3, 3, 3, 3, 3, 2, 1, 0 ]
                #    min(l, r) [ 0, 0, 2, 2, 3, 3, 3, 2, 1, 0 ]
            # Given the max left and max right provided as we iterate, we'll be able to tell if the max boundary of left and right
            # The computation of area at each i could then be made with:
                # min(l, r) - height[i]
                    # where i = the current index
                # One catch with this computation is that it may result in negative value because the current index may have height > 0
                    # Because negative amount of water can't be trapped (means gone), the negative value will be considered 0
            
    # Solution 1 (TC: O(n) / SC: O(n)):
        # initialize an empty array to store the minimum value of the max left and the max right at each index (min_lr)
        # iterate the height array
            # compute the max left and the max right, and append the min of the two to the min_lr
        # initialize the area beginning at 0 to store the area as we iterate the array
        # iterate the height array again
            # compute the area at the current index
                # min(l,r) - height[i]
                # round any negative value to 0
                    # max(0, min(l,r) - height[i])

    # Solution 1:
    # max_left_list, max_right_list = [0], [0]
    
    # l, r = 0, len(height) - 1
    # max_left, max_right = 0, 0

    # while r > 0:
    #     max_left = max(max_left, height[l])
    #     max_right = max(max_right, height[r])

    #     max_left_list.append(max_left)
    #     max_right_list.append(max_right)

    #     l+=1
    #     r-=1

    # max_right_list.reverse()

    # area = 0
    # for i, h in enumerate(height):
    #     area += max(
    #         0,
    #         min(max_left_list[i], max_right_list[i]) - h
    #     )

    # return area

    # Solution 2:
    l, r = 0, len(height) - 1
    max_left, max_right = height[l], height[r]

    area = 0
    while l < r:
        if height[l] <= height[r]:
            l += 1
            max_left = max(max_left, height[l])
            area += max(0, (max_left - height[l]))
        else:
            r -= 1
            max_right = max(max_right, height[r])
            area += max(0, (max_right - height[r]))
        
    return area


start_time = time.time()
print(trap([0,2,0,3,1,0,1,3,2,1]))
print("--- %s seconds ---" % (time.time() - start_time))