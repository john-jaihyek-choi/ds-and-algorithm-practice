from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time

def threeSum(nums: List[int]) -> List[List[int]]:
    # Note:
        # indicies i, j, and k are distinct
            # we don't necessarily need to revisit every possibility of the sequence
                #     i1  i2 i3
                # ex) [0, 0, 0], [0, 0, 1] [0, 0, 2] ...
        # value at nums[i, j, or k] can be identical to each other
            # 0 would be the only case where the all triplet values are identical to each other
        # may return the array in ANY order
        # the output should not contain any duplicate triplets (regardless of the order)
        # *** IMPORANT ***
            # Since the question is asking to get a SUM of 3 numbers to equal to 0:
                # If list is sorted from smallest to largest, then any nums[i] > 0 can form 0 as there are only positive integers
            # This also means if last item of the sorted array is less than or equal to 0, there aren't any triplets that could sum to 0
    
    # Brainstorm:
        # Potential bruteforce solution:
            # This won't work because we can't use the value from the same index multiple times
            # visit each and every possible sequence (including the duplicates) (3 loops, all starting from the same index)
            # ex) [0, 0, 0], [0, 0, 1] [0, 0, 2] ... [n, n, n]
            # time complexity = O(n^3)
            # space complexity = O(1)
        # Potential slightly better solution:
            # This won't also work since there might be same value in different elements
            # visit every non-identical index
            # ex) [0,1,2], [0,1,3], [0,1,4] ... [n-2, n-1, n]

    # Pseudocode:
        # Solution 1 (Sort, then search):
            # initialize an empty list to store the triplet sum match (res_arr)
            # sort the input array
            # then create a loop which iterates the sorted array from the 0th index until length of the array - 2 times (considering the l and r pointer to be used)
                # If nums[i] > 0
                    # return the array output
                # check if nums[i] == nums[i-1]
                    # if true, continue to next iteration
                # create l and r pointers where:
                    # l is initialized at i + 1
                    # r is initialized at the length of the input array - 1
                # While l < r
                    # check if nums[l] == nums[l-1]
                        # if true, increment l by 1
                    # check if nums[r] == nums[r+=]
                        # if true, decrement r by 1
                    # evaluate if the sum of num[i], num[l], and num[r] can sum to 0
                    # if sum is > than 0, decrement the r pointer by 1
                    # if sum is < than 0, increment the l pointer by 1
                    # if sum is = to 0, store the triplet to an empty array, then append it to the res_arr, then increment l by 1
                        # compare the new num[l] with num[l-1] to check for identical num[l] with the previous value
                            # if it's identical, it means it's will create a duplicate
        # Solution 2 (Search and check duplicate using hashmap and set)
            # initialize an empty list to store the triplet sum match (res_arr)
            # create an empty hashmap with a default value of set to store the visited number at i, l, r index repectively (repeat_map)
            # Iterate the input array from the 0th index until the length of the array - 2 times (considering the l and r pointer to be used)
                # check if the num[i] exists in repeat_map[a]
                    # if exists, continue to next iteration
                # create l and r pointers where:
                    # l is initialized at i + 1
                    # r is initialized at the length of the input array - 1
                # While l < r
                    # check if the num[l] exists in repeat_map[l]
                        # if exists, increment l by one
                    # check if the num[r] exists in repeat_map[r]
                        # if exists, decrement r by one
                    # evaluate if the sum of nums[i], num[l], and num[r] can sum to 0
                    # if sum is > than 0, decrement the r pointer by 1
                    # if sum is < than 0, increment the l pointer by 1
                    # if sum is = to 0, store the triplet to an empty array, then append it to the res_arr

    # Solution 1:
    res_arr = []
    nums.sort()

    for i, a in enumerate(nums):
        if a > 0:
            break

        if a == nums[i - 1] and i > 0:
            continue
        
        l, r = i + 1, len(nums) - 1

        while l < r:
            abc_sum = sum((a, nums[l], nums[r]))

            if abc_sum > 0:
                r -= 1
            elif abc_sum < 0:
                l += 1
            else:
                res_arr.append([a, nums[l], nums[r]])
                l += 1
                r -= 1

                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res_arr

    # Solution 2 (WIP)
    # res_arr = []
    # repeat_map = defaultdict(set)
    # nums.sort()

    # for i, a in enumerate(nums):
    #     if a > 0:
    #         break

    #     if a in repeat_map['a']:
    #         continue
        
    #     l, r = i + 1, len(nums) - 1

    #     while l < r:
    #         if(
    #             i == 1 and
    #             l == 5 and
    #             r == 9
    #         ):
    #             print('bug')
    #         b = nums[l]
    #         c = nums[r]

    #         abc_sum = sum((a, nums[l], nums[r]))

    #         if abc_sum > 0:
    #             r -= 1
    #         elif abc_sum < 0:
    #             l += 1
    #         else:
    #             while (
    #                 nums[a] in repeat_map['a'] and
    #                 nums[l] in repeat_map['b'] and
    #                 nums[r] in repeat_map['c'] and
    #                 l < r
    #             ):
    #                 l += 1

    #             res_arr.append([a, nums[l], nums[r]])

    #             repeat_map['a'].add(a)
    #             repeat_map['b'].add(nums[l])
    #             repeat_map['c'].add(nums[r])

    #             l += 1
    #             # r -= 1

    # return res_arr


#       1   2   3   4  5  6  7  8  9  10
# [-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]
1, 5, 9
start_time = time.time()
# print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum())
print("--- %s seconds ---" % (time.time() - start_time))