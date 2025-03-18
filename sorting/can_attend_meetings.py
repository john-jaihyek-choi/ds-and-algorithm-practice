from collections import defaultdict, Counter
from typing import List, Dict, DefaultDict, Set
import time


# Leetcode #252
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        # objective:
            # given an array of intervals, determine if person could attend ALL meetings
        # keywords:
            # intervals:
                # intervals[i] = [start_i, end_i]
            # person MUST attend all meetings
        # Human-like thought process
            # align the intervals sorted based on their staring interval
                # intervals[i] is attendable meeting if intervals[i][start] AND intervals[i][end] occurs before immediately next interval
        # First-thought solution: sort intervals based on starting interval, then iterate and compare the current interval with next interval
            # general steps:
                # sort intervals based on interval start time (sorted_intervals)
                # iterate len(sorted_intervals) - 1 times (exclude the last interval as it's won't have "next" meeting)
                    # if current_end <= next_start (next_start = intervals[i + 1][0])
                        # continue to next iteration
                    # else:
                        # return False
                # return True
            # pseudocode:
                # intervals.sort()
                # for i in range(len(intervals) - 1)
                    # if not intervals[i] <= intervals[i + 1][0]:
                        # return False
                # return True"
        """

        # TC: O(n log n) / SC: O(1) in average
        intervals.sort()
        for i in range(len(intervals) - 1):
            if not intervals[i][1] <= intervals[i + 1][0]:
                return False

        return True

        """
        # Brute-force solution:
            # check every possible interval pairs:
            # general steps:
                # iterate on intervals
                    # if jth_start <= cur_start < jth_end or cur_start <= jth_start < cur_end
                    # False
                # return True 
        """

        # TC: O(n^2) / SC: O(1)
        for [i, [cur_start, cur_end]] in enumerate(intervals):

            for j in range(i + 1, len(intervals)):
                [jth_start, jth_end] = intervals[j]

                if jth_start <= cur_start < jth_end or cur_start <= jth_start < cur_end:
                    return False

        return True


start_time = time.time()
solution = Solution()
print(solution.canAttendMeetings([[1, 5], [2, 4], [6, 10], [10, 15]]))
print("--- %s seconds ---" % (time.time() - start_time))
