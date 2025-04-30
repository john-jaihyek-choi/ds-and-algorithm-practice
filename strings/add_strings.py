from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 415:


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Intuition:
            Bruteforce: convert num1 and num2 to integers and sum it up
                - problem states I use no built-in library

            Alternative: Elementary math approach
                - use two pointers, p1 for num1 and p2 for num2
                - iterate from the back of the num1 and num2 string array
                - compute value of string integer with ord
                - track carryover value and update value on each iteration
                - reverse the array and join each string integers
        """

        # Bruteforce:
        # TC: O(n + m) / SC: O(max(n, m) + 1)
        return str(int(num1) + int(num2))

        # TC: O(max(n, m)) where n is len(num1) and m is len(num2) / SC: O(max(n, m) + 1)
        p1, p2 = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []

        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord("0") if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord("0") if p2 >= 0 else 0

            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10

            res.append(value)

            p1 -= 1
            p2 -= 1

        if carry:
            res.append(carry)

        return "".join(str(digit) for digit in res[::-1])


solution = Solution()
start_time = time.time()
print(solution.addStrings("Hello World"))
print("--- %s seconds ---" % (time.time() - start_time))
