from collections import defaultdict
from typing import List
import time

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # approach 1:
    # initialize a default dictionary which stores integer res_dict
    # iterate over the nums list
        # for each list[i], increment res_dict[list[i]] by 1
    # return the last 2 items of the sorted res_dict

    # res_dict = defaultdict(int)

    # for num in nums:
    #     res_dict[num] += 1

    # print(res_dict)

    # return sorted(res_dict, key=res_dict.get)[-k:]

    # approach 2 (Better runtime):
    # [1,2,2,3,3,3]
    # create an array with length of the total number of possible counts (length of the nums arr) and initialize each index with value 0
        #  0, 1, 2, 3, 4, 5, 6 counts
        # [0, 1, 2, 3, 0, 0, 0] value
    # iterate the nums array to collect the count of each value in a hash map
    # iterate over the hash map that contains value:count
        # append to the res_arr, the value based on the count in the hash map.
    count_map = defaultdict(int)

    for num in nums:
        count_map[num] = 1 + count_map.get(num, 0)

    freq = [[] for i in range(len(nums) + 1)]
    
    for num_val, count in count_map.items():
        freq[count].append(num_val)

    response = []

    for i in range(len(freq) - 1, -0, -1):
        for number in freq[i]:
            response.append(number)
            if len(response) == k:
                return response




start_time = time.time()
# print(topKFrequent([1,2,2,3,3,3], 2))
topKFrequent([1,2,2,3,3,3], 2)
print("--- %s seconds ---" % (time.time() - start_time))
