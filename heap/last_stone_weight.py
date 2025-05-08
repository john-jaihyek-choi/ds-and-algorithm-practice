from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import time
import heapq


class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Heap approach:
            - heapify the stones array
                - negate the the stones[i]
                - then heapify
            - iterate while len(stones) > 1:
                - pop 2 largest in the heapq
                - compare the two items
                    - if x == y:
                        continue
                    - elif x > y:
                        heapq.heappush(stones, x - y)
                    - else:
                        heapq.heappush(stones, y - x)
            - return stones[0] if stones else 0
        """
        # TC: O(n * log n) / SC: O(n)
        copy = [-w for w in stones]  # TC: O(n) / SC: O(n)
        heapq.heapify(copy)  # TC: O(n)

        while len(copy) > 1:  # TC: O(n - 1) -> O(n)
            x, y = abs(heapq.heappop(copy)), abs(heapq.heappop(copy))  # TC: O(log n)

            if x == y:
                continue
            elif x > y:
                heapq.heappush(copy, -(x - y))  # TC O(log n)
            else:
                heapq.heappush(copy, -(y - x))  # TC O(log n)

        return abs(copy[0]) if copy else 0  # TC: O(1)


class Solution1:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Intuition:
            Bruteforce:
                - sort the stones
                - while len(stones) > 1:
                    - pop the last 2 elements as long as num is non-empty
                        - x = stones.pop()
                        - y = stones.pop()
                    - if x == y:
                        continue to next iteration
                    - elif x < y:
                        y = y - x
                        stones.append(y)
                        sort stones
                    - else:
                        x = x - y
                        stones.append(x)
                        sort stones
                - return stones[0]
        """
        # TC: O(n * n log n) / SC: O(1)
        stones.sort()  # TC: O(n log n)
        while len(stones) > 1:  # TC: O(n - 1) -> O(n)
            x, y = stones.pop(), stones.pop()

            if x == y:
                continue
            elif x < y:
                stones.append(y - x)
            else:
                stones.append(x - y)

            stones.sort()  # TC: O(n log n)

        return stones[0] if stones else 0


start_time = time.time()
solution = Solution2()
print(solution.lastStoneWeight([7, 1, 5, 3, 6, 4]))
print("--- %s seconds ---" % (time.time() - start_time))
