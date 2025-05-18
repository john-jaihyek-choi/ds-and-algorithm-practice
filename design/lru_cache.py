import time
import math
from collections import defaultdict, deque, OrderedDict
from typing import List, Dict, DefaultDict, Set, Optional
from helper.functions import LinkedList, ListNode, Utility

# Leetcode 146


class ListNode:
    """ """

    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key, self.val = key, val
        self.prev = prev
        self.next = next


class LRUCache:
    """
    Intuition:
        - Use Linked List, head and tail, to track lru to mru
            - implement ListNode
                - vars:
                    - val
                    - prev
                    - next
            - initialize head and tail with an empty ListNode
            - initialize cache dictionary to store references to each nodes
            - initialize capacity at 0
            - core functions:
                - get:
                    - if key exists in cache:
                        - update the cache
                            - unlink the node:
                                - prev.next = next
                                - next.prev = prev
                            - add to the end of the node:
                                - mru.prev.next = new_node
                                - new_node.next = mru
                                - new_node.prev = mru.prev
                                - mru.prev = new_node
                    - else:
                        - return -1
                - put:
                    - if key exists in cache:
                        - update the existing key
                        - update position in the cache:
                            -  unlink the node:
                                - prev.next = next
                                - next.prev = prev
                            - add to the end of the node:
                                - mru.prev.next = new_node
                                - new_node.next = mru
                                - new_node.prev = mru.prev
                                - mru.prev = new_node
                    - else:
                        - create a new_node for the new key-value
                        - add to the end of the node
                    - if cache exceeds the capacity, remove the item closest to the head
    """

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = ListNode(), ListNode()
        self.head.next, self.tail.prev = self.tail, self.head

    def remove_cache(self, node: ListNode) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def add_cache(self, node: ListNode) -> None:
        mru = self.tail.prev
        mru.next, node.prev = node, mru
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove_cache(node)
        self.add_cache(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_cache(self.cache[key])

        self.cache[key] = ListNode(key, value)
        self.add_cache(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove_cache(lru)
            del self.cache[lru.key]


class LRUCache1:
    """
    Intuition:
        1. use built-in OrderdDict to store as a cache
            - initialize OrderdDict as a member variable for the class
            - core functions:
                - get:
                    - get value of the key if key exists in cache
                    - else return -1
                - put:
                    - update the value of key if key exists in cache
                    - else add key-valu pair to cache
                    - evict key and if cache size exceeds capacity
    """

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]

        self.cache[key] = value

        if self.capacity < len(self.cache):
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
