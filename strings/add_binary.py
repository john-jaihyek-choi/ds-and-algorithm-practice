from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set
import time

# Leetcode 415:


class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        """
        Intuition:
            Bruteforce: convert binary strings to int, sum, then convert back to binary string

            No built-in conversion: Elementary sum approach with binary 1 carryover
                - use 2 pointers, p1 for a and p2 for b, starting from the end of each respective string
                - define carry to 0
                - res = []
                - iterate while p1 or p2 are >= 0
                    - digitA = ord(a[p1]) - ord("0") if p1 >= 0 else 0
                    - digitB = ord(b[p2]) - ord("0") if p2 >= 0 else 0
                    - sum_val = (digitA + digitB + carry)
                    - value = sum_val % 2
                        - mod 2 will return 0 for even number and 1 for odd
                    - carry = sum_val // 2
                    - res.append(value)
                    - p1 -= 1
                    - p2 -= 1
                - return reversed, then joined version of res
        """

        # TC: O(max(n, m)) where n is len(a) and m is len(b) / SC: O(max(n, m) + 1)
        p1, p2 = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while p1 >= 0 or p2 >= 0:
            digitA = ord(a[p1]) - ord("0") if p1 >= 0 else 0
            digitB = ord(b[p2]) - ord("0") if p2 >= 0 else 0

            total = digitA + digitB + carry
            value = total % 2
            carry = total // 2

            res.append(value)

            p1 -= 1
            p2 -= 1

        if carry:
            res.append(carry)

        return "".join(str(digit) for digit in res[::-1])


class Solution2:
    def addBinary(self, a: str, b: str) -> str:

        # Alternative approach:
        carry = 0
        a, b = a[::-1], b[::-1]
        res = ""
        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            value = total % 2
            carry = total // 2

            res = str(value) + res

        if carry:
            res = "1" + res

        return res


class Solution3:
    def addBinary(self, a: str, b: str) -> str:
        # Bruteforce:
        return bin(int(a, 2) + int(b, 2))[2:]


solution = Solution1()
start_time = time.time()
print(solution.addBinary("1", "101"))
print("--- %s seconds ---" % (time.time() - start_time))
