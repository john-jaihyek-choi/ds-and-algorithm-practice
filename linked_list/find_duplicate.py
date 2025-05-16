import time
import math
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility


class Solution3:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Note:
            - every integer appears EXACTLY ONCE EXCEPT FOR ONE
        Intuition:
            - Store visited item to a set
                - if value exists in visited set
                    - return the value
                - else:
                    - add the value to the set
            - sort then find repeated occurance:
                - sort the array
                - iterate the array
                    - if nums[cur] == nums[cur - 1]:
                        - return nums[cur]
            - Iterate array with fast and slow pointer (Floyd's algorithm)
                - locate the cycle in the array
                - locate the intersection and return the value at the intersection
        """

        # Floyd's algorithm:
        # TC: O(n) / SC: O(1)
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        head = 0
        while True:
            slow = nums[slow]
            head = nums[head]
            if slow == head:
                return slow

        # TC: O(n log n) / SC: O(1)
        nums.sort()
        for i, n in enumerate(nums):
            if n == nums[i - 1]:
                return n

        # TC: O(n) / SC: O(n)
        visited = set()
        for n in nums:
            if n in visited:
                return n
            visited.add(n)


class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        # Fast and slow pointer to detect cycle, then using 2 pointers to find the beginning of the cycle
        # initialize a fast and slow pointer
        # slow = 0
        # fast = 0
        # while True:
        # slow = nums[slow]
        # fast = nums[nums[fast]]
        # Note: nums[nums[fast]] DOES NOT literally jump 2 indicies at a time, it simply COVERS MORE GROUND than slow
        # So at some point, the fast and slow will intersect
        # set a head starting point (beginning of a linked list)
        # head = 0
        # set a detected cycle point
        # cycle_pointer = slow
        #  while cycle_pointer != head:
        # set head to nums[head]
        # set cycle_pointer to nums[cycle_pointer]

        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        head, cycle_head = 0, slow
        while head != cycle_head:
            head = nums[head]
            cycle_head = nums[cycle_head]

        return cycle_head


class Solution1:

    def findDuplicate(self, nums: List[int]) -> int:
        # Obvious solution: store the num in a set, then detect duplicate
        # initialize an empty set (or set(nums) since nums is guaranteed to be List[int]) (num_set)
        # iterate the nums array (n = nums[i])
        # if n in num_set:
        # return n
        # add n to nums_set
        # return 0

        # TC: O(n) / SC: O(n)
        nums_set = set()
        for n in nums:
            if n in nums_set:
                return n
            nums_set.add(n)
        return 0


# input1 = LinkedList([1,2,3,4])
# Utility.print_linked_list(input1.head)

solution = Solution2()
start_time = time.time()
answer = solution.findDuplicate([1, 2, 3, 2, 2])
print("--- %s seconds ---" % (time.time() - start_time))

print(answer)
