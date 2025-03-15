from collections import defaultdict, Counter
from typing import List, Dict, DefaultDict, Set
import time


class Solution2:
    def count_sort(self, arr: List[int]) -> int:
        counter = Counter(arr)
        sorted_arr = []
        mn, mx = min(arr), max(arr)
        for i in range(mn, mx + 1):
            while i in counter and counter[i]:
                sorted_arr.append(i)
                counter[i] -= 1

        return sorted_arr

    def heightChecker(self, heights: List[int]) -> int:
        expected_order = self.count_sort(heights)

        output = 0
        for student, height in enumerate(heights):
            if height != expected_order[student]:
                output += 1

        return output


class Solution1:
    def heightChecker(self, heights: List[int]) -> int:
        # objective:
        # get the total number of students that' don't align with strictly non-decreasing order by heigh rule
        # return the number of students that don't fall in the criteria
        # brainstorm:
        # there is an expected order since height of each students are defined
        # sort heights, then comparing would do the job with O(nlogn) Time and O(n) Space
        # first thought solution:
        # define an exp_heights array with value of sorted heights
        # counter = 0
        # iterate len(heights) times:
        # if heights[i] != exp_heights[i]:
        # increment counter
        # return counter

        # TC: O(n log n) / SC: O(n)
        exp_heights = sorted(heights)
        counter = 0
        for i in range(len(heights)):
            if heights[i] != exp_heights[i]:
                counter += 1

        return counter

        # optimal approach:
        # question:
        # how can I eliminate sorting?
        # why did sorting help?
        # need for expected height
        # is there an alternative to use other data structures to store where each height should be in their respective indicies
        # no, for me to get full "expected" heights, I have to make sure I sort the array before
        # Then what can I do in terms of making the sorting more efficient?
        # Instead of built-in sort, how can I make it more efficient?
        # the heights array has lmited range
        # always between min heights and max heights
        # I know:
        # total number of students
        # the tallest (max) and the shortest (min) student
        # What could counting each heighted student help with?
        # ex)
        # {
        #   1: 3
        #   2: 1
        #   3: 1
        #   4: 1
        # }
        # since I access to the absolute range of the heights (min(heights) <= x <= max(heights))
        # when I know the count of each unique height, I can count by decrementing total available unique heights
        # steps:
        # initialize a counter dictionary (counter)
        # use conventional counting method
        # or use Counter library
        # create an empty array (sorted_arr)
        # implement a counting sort:
        # get min and max height of the given heights array (to be used as a range for iteration)
        # initialize index to be used as array index
        # iterate starting at min value, ending at max + 1 value (i = index)
        # while counter[i]:
        # sorted_arr.append(i)
        # counter[i] -= 1
        # instantiate output to 0
        # iterate on heights (i = index, height = heights[i]):
        # if height != sorted_arr[i]:
        # output += 1

        # TC: O(n + (m * k)) -> O(n) / SC: O(n)
        counter = {}

        for height in heights:
            counter[height] = counter.get(height, 0) + 1

        sorted_arr = []
        mininum, maximum = min(heights), max(heights)
        for i in range(mininum, maximum + 1):  # TC: O(m)
            while i in counter and counter[i]:  # TC: O(k)
                sorted_arr.append(i)
                counter[i] -= 1

        output = 0
        for student, height in enumerate(heights):
            if height != sorted_arr[student]:
                output += 1

        return output

        # less code and slightly more optimal
        counter = Counter(heights)

        sorted_arr = []
        mn, mx = min(heights), max(heights)
        for i in range(mn, mx + 1):
            while i in counter and counter[i]:
                sorted_arr.append(i)
                counter[i] -= 1

        output = 0
        for student, height in enumerate(heights):
            if height != sorted_arr[student]:
                output += 1

        return output


start_time = time.time()
solution = Solution()
print(solution.heightChecker([7, 1, 5, 3, 6, 4]))
print("--- %s seconds ---" % (time.time() - start_time))
