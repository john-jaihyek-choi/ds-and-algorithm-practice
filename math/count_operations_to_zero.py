import math


# Leetcode 2169:
class Solution1:
    def countOperations(self, num1: int, num2: int) -> int:
        """
        Note:
            - 2 non-negative integers
                - num1
                - num2
            - in single operation:
                - if num1 >= nums2:
                    num1 -= num2
                - else:
                    num2 -= num1
            - always positive integer
        Intuition:
            - Recursively compute new num1 and num2
            - in each iteration, count += 1
        Idea:
            - use while loop and keep updating num1 and num2 value
                - return operation counts when either number == 0
        """

        # TC: O(max(num1, num2)) / SC: O(1)
        # max(num1, num2) because in the worst case, each subtraction would be 1 which would essentially iterate num1/num2 many times
        ops = 0
        while True:
            if not num1 or not num2:
                return ops

            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1

            ops += 1


class Solution2:
    def countOperations(self, num1: int, num2: int) -> int:
        """
        Recursive solution:
            - base case: if not num1 or not num2
                - return ops
            - use helper function
        """

        # recursive v1:
        # TC: O(max(num1, num2)) / SC: O(1)
        # max(num1, num2) because in the worst case, each subtraction would be 1 which would essentially iterate num1/num2 many times
        def recurse(num1, num2, ops):
            if not num1 or not num2:
                return ops

            if num1 >= num2:
                return recurse(num1 - num2, num2, ops + 1)
            else:
                return recurse(num1, num2 - num1, ops + 1)

        return recurse(num1, num2, 0)


class Solution3:
    def countOperations(self, num1: int, num2: int) -> int:
        """
        Recursive version 2:
            - base case: if not num1 or not num2
                - return ops
            - no helper function
        """
        # recursive v2:
        # TC: O(max(num1, num2)) / SC: O(1)
        # max(num1, num2) because in the worst case, each subtraction would be 1 which would essentially iterate num1/num2 many times
        if not num1 or not num2:
            return 0

        if num1 >= num2:
            return 1 + self.countOperations(num1 - num2, num2)
        else:
            return 1 + self.countOperations(num1, num2 - num1)
