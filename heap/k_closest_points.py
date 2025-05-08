from collections import defaultdict
from typing import List, Dict, DefaultDict, Set
import math
import time
import heapq


class Solution3:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Optimization Intuition:
            - Use min heap to store points
                - heapify the points and their distance to each heap node
                -
        """

        # TC: O(n + k + k log n) / SC: O(n + k)
        origin = [0, 0]
        distances = []  # SC: O(n)

        for point in points:  # TC: O(n)
            distance = self.calcDistance(origin, point)
            distances.append(tuple([distance, point]))

        heapq.heapify(distances)  # TC: O(n)
        res = []  # SC: O(k)

        while k > 0:  # O(k)
            distance, coord = heapq.heappop(distances)  # O(log n)
            res.append(coord)
            k -= 1

        return res

    def calcDistance(self, coord1: List[int], coord2: List[int]) -> float:
        return math.sqrt(
            pow(coord1[0] - coord2[0], 2) + pow(coord1[1] - coord2[1], 2)
        )  # TC: O(1)


class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Optimization Intuition:
            - Use min heap to store points
                - heapify the points and their distance to each heap node
                - return nsmallest from the heap
        """

        # TC: O(n log k) / SC: O(n)
        origin = [0, 0]
        distances = []  # SC: O(n)

        for point in points:  # TC: O(n)
            distance = self.calcDistance(origin, point)
            distances.append(tuple([distance, point]))

        heapq.heapify(distances)  # TC: O(n)

        res = heapq.nsmallest(k, distances)  # TC: O(n log k)

        return [item[1] for item in res]  # TC: O(k)

    def calcDistance(self, coord1: List[int], coord2: List[int]) -> float:
        return math.sqrt(
            pow(coord1[0] - coord2[0], 2) + pow(coord1[1] - coord2[1], 2)
        )  # TC: O(1)


class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Intuition:
            - Bruteforce:
                - compute distance between origin and every coordinate in points[i]
                - sort the list of distance in increasing order
                - return last kth elements from the sorted list
        """

        # TC: O(n + n log n) -> O(n log n) / SC: O(n)
        origin = [0, 0]  # TC: O(1)
        distances = []  # SC: O(n)
        for point in points:  # TC: O(n)
            distance = self.calcDistance(origin, point)  # TC: O(1)
            distances.append(tuple([distance, [point[0], point[1]]]))  # TC: O(1)

        distances.sort()  # TC: O(n log n)

        return [item[1] for item in distances[:k]]  # TC: O(k)

    def calcDistance(self, coord1: List[int], coord2: List[int]) -> float:
        return math.sqrt(
            pow(coord1[0] - coord2[0], 2) + pow(coord1[1] - coord2[1], 2)
        )  # TC: O(1)


start_time = time.time()
solution = Solution3()
print(solution.kClosest([[0, 2], [2, 2]]))
print("--- %s seconds ---" % (time.time() - start_time))
