import math, time, os, random, sys, re
from collections import defaultdict, OrderedDict
#
# Complete the 'groupSort' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# input:
    # arr: List[int]
        # arr[i] represents a number
# goal:
    # output: List[List[int]]
        # return the 2 dimensional array that contains list length of 2 which contains:
            # the number that appears in the arr on the 0th index
            # the frequency of the 0th index number that appears in arr
# Brainstorm:
    # Bruteforce (TC: O(n log n)):
        # Find out the frequency of each element by iterating the arr using hash map [ O(n) ]
        # iterate on the frequency hash_map and store the [number, frequency] pair to the output array [ O(n) ]
        # sort the output array using built-in sort in python [ O(n log n) ]
    
# Bruteforce Approach:
    # Variables:
        # output : List[ List[int] ] where inner List's length = 2
        # freq_map: Dict[int, int]
            # use default dict for convenient += on counter
    # Pseudocode:
        # 1. Find and register frequency of the elements to hash_map:
            # initialize an empty dictionary to store the frequency (freq_map)
                # key = arr[i]
                # value = frequency of arr[i]
            # iterate on arr (n = arr[i]):
                # freq_map[n] += 1
        # 2. iterate the freq_map and append [number, frequency] pair to the output arr
            # initialize an empty list to store the output (output)
            # iterate on freq_map.items() (num = key, freq = value):
                # output.append(tuple(num, freq))
        # 3. sort twice using output array using built-in sort python [O(n log n)]
            # output.sort()
            # output.sort() 
            # return output

# Optimal:
class Solution2:
    def groupSort(self, arr):
        # Write your code here
        # TC: O(n log n) / SC: O(n)
        freq_map = defaultdict(int)
        for n in arr:
            freq_map[n] += 1
        
        output = []
        for num, freq in freq_map.items():
            output.append(tuple([num, freq]))

        output.sort(key=lambda pair: (-pair[1], pair[0]))
        
        return output
    
# Initial Try:
class Solution1:
    def groupSort(self, arr):
        # Write your code here
        # TC: O(n log n) / SC: O(n)
        freq_map = defaultdict(int)
        for n in arr:
            freq_map[n] += 1
        
        output = []
        for num, freq in freq_map.items():
            print(num, freq)
            output.append(tuple([num, freq]))

        output.sort()
        output.sort(key=lambda x: x[1], reverse=True)
        
        return output

solution = Solution1()
start_time = time.time()
print(solution.groupSort([3, 3, 2, 2, 1, 7, 12, 12, 13]))
print("--- %s seconds ---" % (time.time() - start_time))