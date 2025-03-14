import math, time
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set

# Leetcode 933:
# 12/11 retried
class RecentCounter3:
    # Goal:
        # counts the number of recent request within a certain time frame
    # Idea:
        # use of deque:
            # 1. initialize an empty deque for self.request
            # 2. implement ping
                # compute the t received - 3000ms (threshold)
                # request.append(t)
                # while self.requests and self.requests[0] < threshold
                    # request.popleft()
        # if use of deque is prohibited:
            # 1. initialize key variables
                # initialize an empty array on init of class
                # initialize recent variable at 0
            # 2. implement ping
                # compute the t received - 3000ms (threshold)
                # request.append(t)
                # while self.requests[self.recent] < threshold:
                    # self.recent += 1
                # return len(self.requests) - self.recent

    # Dequeue approach:
    def __init__(self):
        # initialize counter with 0 recent request
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Input:
            # t: int
        # Output:
            # output: int
                # returns number of request that has happend in the past 3000 ms (including new request)
                    # t - 3000, t
        # guarantess strictly larger t each call
        # adds new request at time t
            # t = time in ms

        # TC: O(k) / SC: O(k)
        # where k is number of requests past the threshold 
        threshold = t - 3000
        self.requests.append(t)

        while self.requests and self.requests[0] < threshold:
            self.requests.popleft()
        
        return len(self.requests)

    # No Deque approach:
    def __init__(self):
        self.requests = []
        self.recent = 0

    def ping(self, t: int) -> int:
        # TC: O(k) / SC: O(n)
            # where k is number of requests past the threshold
            # where n is number of total ping requets
        threshold = t - 3000
        self.requests.append(t)

        while self.requests and self.requests[self.recent] < threshold:
            self.recent += 1
        
        return len(self.requests) - self.recent

# without deque:
class RecentCounter2:
    def __init__(self):
        self.requests = []
        self.latest = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        while self.requests[self.latest] < t - 3000:
            self.latest += 1

        return len(self.requests) - self.latest
    
# without deque and with binary search:
class RecentCounter1:
    def __init__(self):
        self.requests = []
        self.latest = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        self.latest = self.search(self.latest, t)

        return len(self.requests) - self.latest

    def search(self, latest, t):
        l = latest - 1 if latest > 0 else 0
        r = len(self.requests) - 1

        while l <= r:
            m = (l + r) // 2
            if self.requests[m] < t - 3000:
                l = m + 1
            elif self.requests[m] > t - 3000:
                r = m - 1
            else:
                return m

        return l
    

class RecentCounter:
    # Brainstorm:
        # RecentCounter() initializes the counter with 0 recent requests
        # ping(int t) adds new request at time t where t represents some time in ms
            # it returns the number of requests that has happened in the past 3 seconds (3000ms)
                # output: List[int]
            # t input will be strictly larger value than the previous ping call
    # Pseudo code:
        # __init__:
            # initialize self.request with an empty deque
        # ping:
            # append t in to requests
            # while self.requests is non-empty and t - self.requests[0] > 3000:
                # popleft() on the requests queue
            # return length of the self.requests

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        while self.requests and t - self.requests[0] > 3000:
            self.requests.popleft()
        
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))