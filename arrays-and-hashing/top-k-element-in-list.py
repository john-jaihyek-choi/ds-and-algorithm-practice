from collections import defaultdict
from typing import List
import time

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # initiate a default dictionary which stores integer res_dict
    # iterate over the nums list
        # for each list[i], increment res_dict[list[i]] by 1
    # return the last 2 items of the sorted res_dict

    # res_dict = defaultdict(int)

    # for num in nums:
    #     res_dict[num] += 1

    # print(res_dict)

    # return sorted(res_dict, key=res_dict.get)[-k:]

    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    


start_time = time.time()
print(topKFrequent([1,2,2,3,3,3], 2))
print("--- %s seconds ---" % (time.time() - start_time))