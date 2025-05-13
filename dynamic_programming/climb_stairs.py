from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time


class Solution4:
    def climbStairs(self, n: int) -> int:
        """
        Intuition:
            1. Recursion (Bruteforce):
                - starting at n = 0, take 2 paths - n + 1 and n + 2
                - recursinon base case:
                    - when > n:
                        - return False
                    - when == n:
                        - return True
            2. DP top-bottom:
                - think fibonacci sequence:
                    - all possible permutation of ways to climb to n is...
                        - all possible permutations of n - 1
                        - plus
                        - all possible permutation of n - 2
                - use an array to remember value at each place
            3. DP top-bottom (optimized):
                - use 2 variables to maintain first and second items before current
        """

        # DP top-bottom:
        cache = [-1] * n

        def dfs(num: int) -> int:
            if num >= n:
                return num == n
            if cache[num] != -1:
                return cache[num]
            cache[num] = dfs(num + 1) + dfs(num + 2)
            return cache[num]

        return dfs(0)


class Solution1:
    def climbStairs(self, n: int) -> int:
        """
        Intuition:
            - Calculate every permutation of 2
                - ex) n = 2
                    2 main permutations:
                        1. 1 step, then 1 step
                        2. 2 step
                - ex) n = 3
                    1. (1, 1, 1)
                    2. (1, 2)
                    3. (2, 1)
            - Fibonacci sequence:
                - aggregate sum of possibilities of f(n - 1) and f(n - 2), starting at 3
                    - sum = f(n - 1) + f(n - 2)
                    - ex) n = 5
                        at f(0), 0 possibilities
                        at f(1), 1 possibilities
                        at f(2), 2 possibilities
                        at f(3), f(3 - 1) + f(3 - 2) = f(2) + f(1) = 1 + 2 = 3 possibilities
                        at f(4), f(4 - 1) + f(4 - 2) = f(3) + (2) = 3 + 2 = 5 possibilities
                        at f(5), f(5 - 1) + f(5 - 2) = f(4) + f(3) = 5 + 3 possibilities
        """
        # dynamic programming - space optimized:
        # TC: O(n) / SC: O(1)
        if n <= 2:
            return n

        first, second = 1, 2
        for i in range(3, n + 1):
            cur = first + second
            first, second = second, cur

        return second


class Solution2:
    def climbStairs(self, n: int) -> int:
        # dynamic programming:
        # TC: O(n) / SC: O(n)
        if n <= 2:
            return n

        array = [0] * (n + 1)
        array[1], array[2] = 1, 2

        for i in range(3, n + 1):
            array[i] = array[i - 1] + array[i - 2]

        return array[n]


class Solution3:
    def climbStairs(self, n: int) -> int:
        # recursion:
        # TC: O(2^n) / SC: O(1)
        def dfs(i: int):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)


start_time = time.time()
solution = Solution1()
print(solution.climbStairs(10))
print("--- %s seconds ---" % (time.time() - start_time))
