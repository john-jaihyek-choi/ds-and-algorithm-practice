from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

# Retried 10/22/2024 - Leetcode 11
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # input:
            # height: List[int]
        # goal: find the maximum possible area the water can be contained
            # can't have slant the container
        # Note:
            # Because water can't be stored slanted:
                # min(height[l], height[r]) is the max height possible of the given container
        # Two-pointer approach:
            # start l and r from each end of the height list
            # calculate of the given bars:
                # area = w * h
                # w = r - l
                # h = min(height[l], height[r])
            # store the max area as iterating
            # move the pointer based on their given height:
                # if height[l] (current height of l) is less than or equal to height[r] (current height of r)
                    # move l pointer
                # otherwise:
                    # move r pointer
        # Variables to track:
            # l: int
            # r: int
            # max_area
        # Pseudocode:
            # initialize a max_area to 0 (max_area)
            # initialize two pointers
                # l = 0
                # r = len(height) - 1
            # iterate while l < r:
                # calculate the area:
                    # find width
                        # width = r - l
                    # find height
                        # height = min(height[l], height[r])
                    # find area
                        # area = width * height
                    # set max_area to max(max_area, area)
                # if height[l] is less than or equal to height[r]
                    # move l pointer
                # else:
                    # move r pointer
            # return max_area

        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = w * h
            max_area = max(max_area, area)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return max_area

class Solution:
    def maxArea(heights: List[int]) -> int:
        # Note:
            # input, heights, is an array of integers where heights[i] represents the height of the bar in a 2d bar graph
            # function must return the maximum possible area of the water that can be contained inside 2 bars (height[a] and height[b])

        # Brainstorm:
            # smaller of the two bars determines the maximum height of the water for that unique pair
            # Which of the two pointers to shift when needed?
                # Since the objective is to maximize the area of the war between the two bars can contain:
                    # compare the heights[l] and heights[r] and shift the pointer where the value is smaller
        
        # Pseudocode:
            # initialize a variable to store the max area (max_area)
            # initialize the left and the right pointer (l and r)
                # left pointer to begin from 0
                # right pointer to begin from the length of the input array, heights - 1
            # while left pointer is less than the right pointer
                # compare the max_area with the product of minimum of the left and right bars and difference between the right and left (max_area = max(max_area, min(l, r) * r - l ))
                # if height[l] > height[r]
                    # decrement r by 1
                # else:
                    # increment l by 1
            # return max_area

        max_area, l, r = 0, 0, len(heights) - 1

        while l < r:
            max_area = max(max_area, min(heights[l], heights[r]) * (r - l) )

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_area

solution = Solution()
start_time = time.time()
print(solution.maxArea([1,7,2,5,4,7,3,6]))
print("--- %s seconds ---" % (time.time() - start_time))