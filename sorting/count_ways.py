from collections import defaultdict, Counter
from typing import List, Dict, DefaultDict, Set
import time


# Leetcode 2580
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        """
        # objective:
            # given array ranges, return the total number of ways to split ranges into 2 groups
        # keywords:
            # ranges:
                # ranges[i] = [start, end]
                    # start and end both inclusive
            # overlapping:
                # given 2 ranges:
                    # range1 = [1, 3]
                    # range2 = [2, 5]
                # two ranges are overlapping if (assuming ranges is sorted):
                    # range1[0] <= range2[0] <= range1(1)
                        # or
                    # range2[0] <= range1[0] <= range2[1]
        # ideas:
            # first thought solution:
                # sort the ranges
                # iterate and group the ranges that are overlapping
                # compute total number of ways using pow(2, n) where n == size of unique/merged groups
            # Pseudocode:
                # ranges.sort()
                # groups = []
                # for rng in ranges:
                    # if groups and rng overlaps with groups[-1]:
                        # groups[-1][1] = max(groups[-1][1], rng[1])
                    # else:
                        # groups.append(rng)
                # return pow(2, len(groups)) % (pow(10, 9) + 7)
        """
        # TC: O(n log n) / SC: O(n)
        ranges.sort()
        groups = []
        for rng in ranges:
            if groups and self.isOverlapping(rng, groups[-1]):
                groups[-1][1] = max(groups[-1][1], rng[1])
            else:
                groups.append(rng)
        return pow(2, len(groups)) % (pow(10, 9) + 7)

    def isOverlapping(self, interval_1: List[int], interval_2: List[int]):
        return (
            interval_1[0] <= interval_2[0] <= interval_1[1]
            or interval_2[0] <= interval_1[0] <= interval_2[1]
        )


start_time = time.time()
solution = Solution()
print(solution.countWays([[1, 3], [10, 20], [2, 5], [4, 8]]))
print("--- %s seconds ---" % (time.time() - start_time))
