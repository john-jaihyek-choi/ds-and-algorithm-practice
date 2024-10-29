import math, time, os, random, sys, re
from collections import defaultdict, OrderedDict

# Leetcode 451:

# Optimal:
class Solution1:
    def groupSort(self, s):
        # TC: O(n log n) / SC: O(n)
        freq_map = defaultdict(int)
        for c in s:
            freq_map[c] += 1
        
        output = []
        for char, freq in freq_map.items():
            output.append(char * freq)

        output.sort(key=lambda x: -len(x))
        
        return ''.join(output)



solution = Solution1()
start_time = time.time()
print(solution.groupSort([3, 3, 2, 2, 1, 7, 12, 12, 13]))
print("--- %s seconds ---" % (time.time() - start_time))