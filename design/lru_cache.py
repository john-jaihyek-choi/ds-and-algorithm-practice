import time
import math
from collections import defaultdict, deque
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility

# Leetcode 146


class ListNode:
    def __init__(self, key: int = -1, val: int = -1):
        self.next = None
        self.prev = None
        self.val = val
        self.key = key


class LRUCache:
    """
    Linked List Approach:
        - General idea:
            1. implement basic ListNode class
            2. initialize left and right end - left being lru and right being mru
            3. initialize a dictionary that points to the ListNode
            3. implement get:
                - if key in self.items:
                    - update the pointer of the current node to new mru
                    - return the value
                - else return -1
            4. implement put:
                - if key in self.items:
                    - update the pointer of the current node to new mru
                - update the value of the existing key

    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        item = self.cache[key]
        self.removeCache(item)
        self.addCache(item)
        return item.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeCache(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self.addCache(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.removeCache(lru)
            del self.cache[lru.key]

    def addCache(self, cache: ListNode) -> None:
        old_mru, tail = self.tail.prev, self.tail
        cache.next, cache.prev = tail, old_mru
        old_mru.next = tail.prev = cache

    def removeCache(self, cache: ListNode) -> None:
        prev, nxt = cache.prev, cache.next
        prev.next, nxt.prev = nxt, prev


class LRUCache1:
    """
    Intuition:
        1. use built-in data structure
            - use OrderedDict to store cache in HashMap-like object
            - General steps:
                1. initialize construtor vars:
                    - initialize self.cache with OrderedDict()
                    - initialize self.capacity with capacity
                2. Implement get
                    - input: key
                    - if key in self.cache:
                        - return the value of the key
                    - else return -1
                    - every time get is called, remove then add the key-val pair to the OrderedDict
                3. Implement put
                    - input: key, value
                    - if key in self.cache:
                        - update the value
                    - else:
                        - add the key-val pair to the cache
                    - if len(self.cache) exceeds self.capacity:
                        - evict lru item
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  # SC: O(c) where c = capacity

    # TC: O(1)
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]

        return -1

    # TC: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


class Node:
    def __init__(self, key: int, val: int = 0):
        self.key, self.val = key, val
        self.next = self.prev = None


# Optimized solution:
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru, self.mru = Node(0, 0), Node(0, 0)
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
        self.lru, self.mru = Node(0, 0), Node(0, 0)
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
