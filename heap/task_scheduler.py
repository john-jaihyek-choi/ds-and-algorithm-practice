from typing import List
import time
import heapq
from collections import deque, Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Intuition:
            - Using Hashmap to store frequency of tasks and heapify, then use queue to store the "popped" items
                - store frequency of each tasks (26 unique tasks) in hashmap
                    ex) tasks = ["X","X","Y","Y"]
                    {
                        X: 2,
                        Y: 2
                    }
                - heapify frequency dictionary (max_heap)
                - create a queue
                - while max_heap is non-empty or q is non-empty:
                    - if max_heap:
                        - heappop from the max_heap
                            - this will contain task with highest frequency
                        - store the popped value - 1 to queue to store the order
                    - else:
                        - increment cyle by 1 since iteration is complete
                        while q:
                            - push the q.popleft() to max_heap
        """

        # TC: O(m) / SC: O(1)
        cpu_tasks = Counter(tasks)  # TC: O(n) / SC: O(26) -> O(1)
        max_heap = [
            -freq for freq in cpu_tasks.values()
        ]  # TC: O(26) -> O(1) / SC: O(26) -> O(1)
        heapq.heapify(max_heap)  # TC: O(26)

        q = deque()  # TC: O(m) at max
        cycle = 0
        while max_heap or q:  # TC: O(26 + m)
            cycle += 1

            if max_heap:
                freq = heapq.heappop(max_heap) + 1  # TC: O(log 26) -> O(1)
                if freq < 0:
                    q.append(tuple([freq, cycle + n]))

            while q and q[0][1] == cycle:
                heapq.heappush(max_heap, q.popleft()[0])  # TC: O(log 26) -> O(1)

        return cycle


start_time = time.time()
solution = Solution()
print(solution.leastInterval([[0, 2], [2, 2]]))
print("--- %s seconds ---" % (time.time() - start_time))
