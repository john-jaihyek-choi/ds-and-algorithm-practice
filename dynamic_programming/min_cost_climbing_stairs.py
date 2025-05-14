from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Note:
            - find the minimum cost to reach the top floor
            - can only climb one or two steps at a time
            - I can start from index 0 or 1
        Intuition:
            - DFS approach:
                - recurse to n + 1 and n + 2 then add which is smaller of the two
                - recursion base case:
                    - when n reaches len(costs), return 0
            - DP approach:
                - cache ith position and the min value
                - if cache[i] exists, return that value
                - else, recurse and find the path
            - DP space optimized:
                - iterate from end to start of the array, min starting 0
                - update the input array with the sum of min(cost[i + 1], cost[i + 2])
                    - Reason:
                        - because each cost[i] is only dependent on its next two values, i + 1 and i + 2
                        - so if I start from the end of the array, then updating cost[i] with sum of what's smaller of i + 1 th value or i + 2 th value will guarantee that cost[i] is optimal at each given point thereby globally optimal
        """

        # DP space optimized:
        # TC: O(n) / SC: O(1)
        if len(cost) <= 2:
            return min(cost)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

        # DP Approach:
        # TC: O(n) / SC: O(n)
        cache = [-1] * len(cost)

        def dfs(i: int) -> int:
            if i >= len(cost):
                return 0
            if cache[i] != -1:  # cache exists
                return cache[i]
            else:  # cache doesn't exist, so recurse and find one
                cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
                return cache[i]

        return min(dfs(0), dfs(1))

        # TC: O(2^n) / SC: O(n)
        def dfs(i: int) -> int:
            if i >= len(cost):
                return 0

            return cost[i] + min(dfs(i + 1), dfs(i + 2))

        return min(dfs(0), dfs(1))


start_time = time.time()
solution = Solution()
print(solution.minCostClimbingStairs(10))
print("--- %s seconds ---" % (time.time() - start_time))
