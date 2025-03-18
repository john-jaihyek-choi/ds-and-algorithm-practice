from collections import defaultdict, Counter
from typing import List, Dict, DefaultDict, Set
import time


# Leetcode #56
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        # objective:
            # given array of intervals, merge all overlapping intervals, and return the merged intervals that are non-overlapping
        # keywords:
            # intervals:
                # intervals[i] = [start_i, end_i]
            # overlapping intervals:
                # interval[j][start] <= interval[i][start] < interval[j][end]
                    # or
                # interval[i][start] <= interval[j][start] < interval[i][end]
        # intuition:
            # sort by interval start
                # ex) [[1, 3], [2, 6], [8, 10], [15, 18]]
            # initialize an empty set to store "merged" intervals (been_merged)
            # initialize output array
            # iterate on intervals (i = index, interval = intervals[i])
                # initialize an array with intervals[i] (group)
                # add intervals[i] to been_merged set
                # iterate on intervals range(j = i + 1, len(intervals)):
                    # if intervals[i] and intervals[j] overlaps:
                        # add intervals[j] to been_merged set
                        # append intervals[j] to group array
                # append [ group[0][0], group[-1][1] ] to output array
        # pseudocode:
            # been_merged = set()
            # output = []
            # for i, interval in enumerate(intervals):
                # group = [ intervals[i] ]
                # been_merged.add(intervals[i])
                # for j in range(i + 1, len(intervals)):
                    # if
                        # been_merged.add(intervals[j])
                        # group.append(intervals[j])
                # output.append([ group[0][0], group[-1][1] ])
            # return output
        """

        # TC: O(n^2) / SC: O(n)
        intervals.sort()  # TC O(n log n) / SC O(1) average O(n) worst
        been_merged = set()  # SC O(n)
        output = []
        for i, cur_interval in enumerate(intervals):  # O(n)
            if tuple(cur_interval) in been_merged:
                continue

            group = [cur_interval[0], cur_interval[1]]
            been_merged.add(tuple(cur_interval))

            for j in range(i + 1, len(intervals)):  # O(n)
                jth_interval = intervals[j]
                if tuple(jth_interval) not in been_merged and (
                    jth_interval[0] <= group[0] <= jth_interval[1]
                    or group[0] <= jth_interval[0] <= group[1]
                ):
                    been_merged.add(tuple(jth_interval))
                    group[0], group[1] = min(group[0], jth_interval[0]), max(
                        group[1], jth_interval[1]
                    )

            output.append(group)

        return output

        """
        # Optimal Solution:
        #     Is there a way to not visit every element?
        #         using stack structure?
        #             iterate intervals
        #                 if stack[-1] is overlapping with current interval:
        #                     pop stack.pop, create new group, push back to stack
        #     pseudocode:
        #         intervals.sort()
        #         initialize an empty stack (groups)
        #         for cur_interval in intervals:
        #             if stack and (cur_interval[0] <= stack[-1][0] <= cur_interval[1] or stack[-1][0] <= cur_interval[0]) <= stack[-1][1]:
        #                 prev_range = groups.pop()
        #                 groups.append(min(cur_interval[0], prev_range[0]), max(cur_interval[1], prev_range[1]))
        #             else:
        #                 groups.append(cur_interval)
        """

        # TC: O(n log n) / SC: O(n)
        intervals.sort()
        groups = []
        for cur_interval in intervals:
            if groups and self.isOverlapping(cur_interval, groups[-1]):
                prev_range = groups.pop()
                groups.append(
                    [
                        min(cur_interval[0], prev_range[0]),
                        max(cur_interval[1], prev_range[1]),
                    ]
                )
            else:
                groups.append(cur_interval)

        return groups

        # Cleaner and more optimized version (without popping):
        # TC: O(n log n) / SC: O(n)
        intervals.sort()
        groups = []
        for cur_interval in intervals:
            if groups and self.isOverlapping(cur_interval, groups[-1]):
                groups[-1][1] = max(
                    groups[-1][1], cur_interval[1]
                )  # no need to pop since sort guarantees the start will be sorted in ascending order
            else:
                groups.append(cur_interval)

        return groups

    def isOverlapping(self, interval_1: List[int], interval_2: List[int]):
        return (
            interval_1[0] <= interval_2[0] <= interval_1[1]
            or interval_2[0] <= interval_1[0] <= interval_2[1]
        )


start_time = time.time()
solution = Solution()
print(solution.merge([0, 30], [5, 10], [15, 20]))
print("--- %s seconds ---" % (time.time() - start_time))
