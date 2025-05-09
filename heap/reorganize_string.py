from collections import deque, Counter
import time
import heapq


class Solution1:
    def reorganizeString(self, s: str) -> str:
        """
        Intuition:
            - Bruteforce:
                - NOT A WORKING SOLUTION
                - group s by characters and their frequency (Hash Map)
                - iterate on the hash map while it's non-empty
                    - if len(frequency) == 1 and frequency.values[0] > 1:
                        - return ""
                    - add each character to res string
                    - decrement char's freq (frequency[char] -= 1)
                    - if frequency[char] <= 0:
                        - delete the char from the hash map
            - Using Max Heap and Queue:
                - group s by characters and their frequency (frequency)
                - set max_heap to frequency
                    - max_heap[i] = [frequency, char]
                - heapify the max_heap
                - initialize a deque (q)
                - while max_heap or q:
                    - if max_heap:
                        - heappop from max_heap
                            - freq = item[0] + 1
                            - char = item[1]
                        - if char == res[-1]:
                            - return ""
                        - if freq > 0:
                            - push the (freq, char) pair to queue
                    - else:
                        while q is non-empty:
                            - popleft the q
                            - heappush to max_heap
        """

        # TC: O(n + m) -> O(n) / SC: O(1), but O(n) for output string
        frequency = Counter(s)  # TC: O(n) / SC: O(26) -> O(1)
        max_heap = [
            tuple([-freq, char]) for char, freq in frequency.items()
        ]  # TC: O(26) -> O(1) / SC: O(26) -> O(1)
        heapq.heapify(max_heap)  # TC: O(26) -> O(1) / SC: O(26) -> O(1)

        q = deque()
        res = []

        while max_heap or q:  # TC: O(26 + m) where m == number of items placed in q
            if max_heap:
                item = heapq.heappop(max_heap)  # TC: O(log 26) -> O(1)
                freq, char = item[0] + 1, item[1]

                if res and char == res[-1]:
                    return ""

                res.append(char)

                if q:
                    heapq.heappush(max_heap, q.popleft())  # TC: O(log 26) -> O(1)

                if freq < 0:
                    q.append(tuple([freq, char]))
            else:
                heapq.heappush(max_heap, q.popleft())  # TC: O(log 26) -> O(1)

        return "".join(res)  # TC: O(n)


class Solution2:
    def reorganizeString(self, s: str) -> str:
        """
        Alternative way without using q
        """
        # TC: O(n + m) -> O(n) / SC: O(1), but O(n) for output string
        frequency = Counter(s)  # TC: O(n) / SC: O(26) -> O(1)
        max_heap = [
            tuple([-freq, char]) for char, freq in frequency.items()
        ]  # TC: O(26) -> O(1) / SC: O(26) -> O(1)
        heapq.heapify(max_heap)  # TC: O(26) -> O(1) / SC: O(26) -> O(1)

        hold = None  # [freq, char]
        res = []

        while max_heap or hold:  # TC: O(26) where m == number of items placed in q
            if hold and not max_heap:
                return ""

            if max_heap:
                item = heapq.heappop(max_heap)  # TC: O(log 26) -> O(1)
                freq, char = item[0] + 1, item[1]

                res.append(char)

                if hold:
                    heapq.heappush(max_heap, hold)
                    hold = None

                if freq < 0:
                    hold = tuple([freq, char])

        return "".join(res)  # TC: O(n)


start_time = time.time()
solution = Solution2()
print(solution.reorganizeString("aab"))
print("--- %s seconds ---" % (time.time() - start_time))
