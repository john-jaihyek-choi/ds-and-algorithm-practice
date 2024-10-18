import time
import math
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility


class Node:
    def __init__(self, key: int, val: int = 0):
        self.key, self.val = key, val
        self.next = self.prev = None

# Optimized solution:
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru, self.mru = Node(0,0), Node(0,0)
        self.lru.next, self.mru.prev = self.mru, self.lru

    def _insert_cache(self, cache: Node):
        old_mru, mru = self.mru.prev, self.mru
        cache.next, cache.prev = mru, old_mru
        old_mru.next = mru.prev = cache
        
    def _remove_cache(self, cache: Node):
        left, right = cache.prev, cache.next
        left.next, right.prev = right, left

    def get(self, key: int) -> int:
        # return key if key exists
        if key in self.cache:
            # when get operation is called, locate the key in cache, then move the key to most recent used (mru)
            cache = self.cache[key]
            self._remove_cache(cache)
            self._insert_cache(cache)
            return cache.val
        # otherwise return -1
        return -1

    def put(self, key: int, value: int) -> None:
        # update value of the key if key exists
        if key in self.cache:
            # remove then insert cache
            self._remove_cache(self.cache[key])
        # otherwise add key-value pair to the cache
        # create a new node and assign it to the linked list
        cache = Node(key, value)
        self.cache[key] = cache
        self._insert_cache(cache)

        # if new pair cache insert exceeds capacity, remove the lru
        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self._remove_cache(lru)
            del self.cache[lru.key]

        return None
        
# First try solution:
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru, self.mru = Node(0,0), Node(0,0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def _insert_cache(self, cache: Node):
        old_mru, mru = self.mru.prev, self.mru
        cache.next, cache.prev = mru, old_mru
        old_mru.next = mru.prev = cache
        
    def _remove_cache(self, cache: Node):
        left, right = cache.prev, cache.next
        left.next, right.prev = right, left

    def get(self, key: int) -> int:
        # return key if key exists
        if key in self.cache:
            # when get operation is called, locate the key in cache, then move the key to most recent used (mru)
            cache = self.cache[key]
            self._remove_cache(cache)
            self._insert_cache(cache)
            return cache.val
        # otherwise return -1
        return -1

    def put(self, key: int, value: int) -> None:
        # update value of the key if key exists
        if key in self.cache:
            cache = self.cache[key]
            self.cache[key].val = value
            # remove then insert cache
            self._remove_cache(cache)
        # otherwise add key-value pair to the cache
        else:
            # create a new node and assign it to the linked list
            cache = Node(key, value)
            self.cache[key] = cache
            
        self._insert_cache(cache)

        # if new pair cache insert exceeds capacity, remove the lru
        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self._remove_cache(lru)
            del self.cache[lru.key]

        return None