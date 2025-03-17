from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        # objective:
            # given an UNSORTED NUMS, return the length of the longest consecutive elements sequence:
        # Keywords:
            # UNSORTED NUMS input
            # longest consecutive element sequence
                # consecutive element sequence == any collection of consecutive numbers in nums input
            # O(n) time algorithm
        # Brainstorm:
            # bruteforce solution: sorte the nums, then look for consecutive numbers
                # TC: O(n log n) / SC: O(1)
                # general steps:
                    # sort nums in place (or new array), sorted_nums
                        # [1, 2, 3, 4, 100, 200]
                    # initialize counter = 0
                    # initialize output = 0
                    # iterate on sorted_nums (i = index, n = sorted_nums[i])
                        # set prev to the left element
                            # prev = nums[i - 1] if i > 0 else float(-inf)
                        # if prev != n - 1:
                            # counter = 0
                        # increment the counter
                            # counter += 1
                        # output = max(output, counter)
                    # return output
            # optimized solution:
                # TC: O(n) / SC: O(n)
                # intuitively:
                    # how I know series of numbers are consecutive?
                        # find a beginning/starting number
                            # ex) 1 in [100, 4, 200, 1, 3, 2]
                        # store visited number in a set
                            # this allows O(1) time lookup for visited number
                # general steps:
                    # initialize a set to store visted number using nums (nums_set)
                        # ex)
                            # (1, 2, 3, 4, 100, 200)
                    # output = 0
                    # iterate nums (i = index, n = nums[i])
                        # ex) [100, 5, 200, 1, 3, 2]
                        # left = n - 1
                        # if left not in nums_set
                            # counter = 1
                            # nxt = n + 1
                            # while nxt in nums_set
                                # counter += 1
                                # nxt = nxt + 1
                            # output = max(output, counter)
                    # return output
        """

        # TC: O(n * k) / SC: O()
        nums_set = set(nums)  # TC: O(n) / SC: O(n)
        output = 0
        for n in nums_set:  # TC: O(n)
            left = n - 1
            if left not in nums_set:
                nxt = n + 1
                counter = 1
                while (
                    nxt in nums_set
                ):  # TC: O(k), but can be O(1) since this logic only runs when there's no left number of the n we are looking at
                    counter += 1
                    nxt += 1
                output = max(output, counter)
        return output


class Solution1:
    def longestConsecutive(nums: List[int]) -> int:
        """
        # Brainstorm:
            # How can we know if a number is the beginning of the sequence?
                # if the nums[i] - 1 value does not exist in a set, then it means the number is the beginning of a sequence
            # How can we quickly search (O(1) time) if nums[i] - 1 exists?
                # convert the input list to set
                    # Potential concern - does eliminating the duplicate values affect the outcome?
                        # No, because, regardless of how many identical numbers we get, it won't be added as consecutive count since it's the same number

        # Pseudocode:
        # convert the input list to set and store it in a variable for quick search (nums_set)
        # intialize the longest_consecutive at 0 to store the longest_consecutive as iterating the input array (longest_consecutive)
        # iterate over the input list
            # check if nums[i]-1 doesn't exist in a set instantiated above (nums_set)
                # if True
                    # check if nums[i] + x (x starting at 1) exists in nums_set
                        # Repeat while nums[i] + (x+=1) exists in nums_set
                    # check the value of x (we'll call this 'consecutive') is greater than longest_consecutive
                        # if True
                            # replace longest_consecutive
            # after the completion of the loop, return the longest_consecutive variable
        """

        # Solution 1
        # nums_set = set(nums)

        # longest_consecutive = 0

        # for i in range(len(nums)):
        #     consecutive = 1

        #     if (nums[i] - 1) not in nums_set: # checking for start of a sequence
        #         while nums[i] + consecutive in nums_set: # checking for continuous sequence while found
        #             consecutive += 1

        #     if longest_consecutive < consecutive:
        #         longest_consecutive = consecutive

        # return longest_consecutive

        # Solution 2 (Same concept, cleaner)
        nums_set = set(nums)
        longest_consecutive = 0

        for i in range(len(nums)):

            if (nums[i] - 1) not in nums_set:  # checking for start of a sequence
                consecutive = 1

                while (
                    nums[i] + consecutive in nums_set
                ):  # checking for continuous sequence while found
                    consecutive += 1

                longest_consecutive = max(consecutive, longest_consecutive)

        return longest_consecutive


start_time = time.time()
solution = Solution1()
print(solution.longestConsecutive([2, 20, 4, 10, 3, 4, 5]))
print(solution.longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))
print("--- %s seconds ---" % (time.time() - start_time))
